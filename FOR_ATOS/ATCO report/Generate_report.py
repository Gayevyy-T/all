from selenium import webdriver
from selenium.webdriver.support.select import Select  # Select class needed for drop-down list
import time, os, yaml

path = os.getcwd()
os.mkdir("new_reports")
new_path = f"{path}\\new_reports"

browser = webdriver.Chrome(f'{path}\\chromedriver')

'''defining credentials'''
with open(f'{path}\\cred.yml') as config:
    config_file = yaml.load(config, Loader=yaml.BaseLoader)

login = config_file['credentials_config']['login']
password = config_file['credentials_config']['password']

'''generationg report'''
def create_rep(type, r_name):

    browser.get(f'https://{login}:{password}@mstoolbe.it-solutions.myatos.net/MDR/Report')

    elem = browser.find_element_by_id('customer')
    elem.click()

    time.sleep(1)

    atco = Select(browser.find_element_by_name('Available'))
    atco.select_by_value('27')

    time.sleep(1)

    add_button = browser.find_element_by_id('add')
    add_button.click()

    time.sleep(1)

    hosts = Select(browser.find_element_by_name('ReportTypeID'))
    hosts.select_by_value(type)###########hosts=1 / IPs=5 / Services=2

    time.sleep(1)

    csv = Select(browser.find_element_by_name('ReportFormatID'))
    csv.select_by_value('2')

    time.sleep(1)

    go = browser.find_element_by_id('submit')
    go.click()

    time.sleep(15)


    text = browser.find_element_by_tag_name('pre').text
    with open(f'{new_path}\\{r_name}.csv', 'w', encoding='utf-8') as f:
        f.write(text)


#if __main__ == __name__:
create_rep('1', 'Hosts')
create_rep('5', 'IPs')
create_rep('2', 'Services')

browser.close()

########################################################################################
'''Retrieving data from generated .csv files'''
import csv, re

pat_OS = r"Windows"
pat_SER = r"Application|IIS|TomCat|http"
pat_STATE = r"Up|Down"
pat_OFF = r"L3 - ROM|L1-L2 - ROM|L3 - PL"
pat_IPs = r'ADMIN|admin|Admin|Production'

hosts = []
fqdn = []
FQDN = []
out_scope = []
missing_hosts = []
t_dict = {}

'''Filtering Services.csv'''
with open(f'{new_path}\\Services.csv', encoding="utf8") as file:
    reader = csv.DictReader(file, delimiter=',')
    for row in reader:
        if re.search(pat_OS, row['OS']) and re.search(pat_SER,row['SERVICETYPE'])and re.search(pat_STATE,row['STATE'])and re.search(pat_OFF,row['OFFSHORE']):
            if row['HOSTNAME'] in hosts:
                pass
            else:
                hosts.append(row['HOSTNAME'].strip())
        else:
            if row['HOSTNAME'] in out_scope:
                pass
            else:
                out_scope.append(row['HOSTNAME'])
#print('hosts = ',len(hosts))
'''Filtering Hosts.csv and adding FQDN'''
with open(f'{new_path}\\Hosts.csv', encoding="utf8") as h_file:
    reader = csv.DictReader(h_file)
    for row in reader:
        for host in hosts:
            if re.search('^'+host+'$', row['HOSTNAME']):
                FQDN.append(row['HOSTNAME'].strip()+"."+row['DOMAINNAME'].strip())
                fqdn.append(row['HOSTNAME'].strip())
#print(len(fqdn),len(FQDN))
'''Finding missing servers'''
for x in hosts:
    if x in fqdn:
        pass
    else:
        print('missng hosts = ',x)
        missing_hosts.append(x)

'''Adding IPs'''
for host in hosts:
    t_dict[host] = []

with open(f'{new_path}\\IPs.csv') as file:
    reader = csv.DictReader(file, delimiter=',')
    for row in reader:
        if row['HOSTNAME'].strip() in hosts:

#'''set the filter which IPs addr should be added (don't forget to put spaces in the line below 't_dict ...')'''
#            if re.search(pat_IPs, row['DESCRIPTION']):

            t_dict[row['HOSTNAME']].append(row['IPADDR'].split())
#print(len(with_IP))
#print('t_dict = ', len(t_dict))

'''Witing to CSV'''
#FQDN_list = ' '.join(FQDN)

field_name = ['Hostnames','FQDN', 'IP' ]

with open(f'{new_path}\\report.csv', 'w', newline='') as report:
    writer1 = csv.DictWriter(report, fieldnames=field_name)
    writer1.writeheader()
with open(f'{new_path}\\report.csv', 'a', newline='') as report:
    writer2 = csv.writer(report)
    for k,v in t_dict.items():
        for item in FQDN:
            if re.search('^'+k+'\.', item):
                writer2.writerow([k,item,v])
    for missing_host in missing_hosts:
        writer2.writerow([missing_host,'no FQDN', 'no IP'])

print("Finished. Now you can close the window")

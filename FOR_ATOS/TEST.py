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


test_fqdn = []
#common_hosts_fqdn = []


'''Filtering Services.csv'''
with open('C:\\Users\\A645674\\Downloads\\Services.csv', encoding="utf8") as file:
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
print('hosts = ',len(hosts))
'''Filtering Hosts.csv and adding FQDN'''
with open('C:\\Users\\A645674\\Downloads\\Hosts.csv', encoding="utf8") as h_file:
    reader = csv.DictReader(h_file)
    for row in reader:


#        for host in hosts:
#            if re.search('^'+host+'$', row['HOSTNAME']):
#                FQDN.append(row['HOSTNAME'].strip()+"."+row['DOMAINNAME'].strip())
#                fqdn.append(row['HOSTNAME'].strip())
#print(len(fqdn),len(FQDN))


        if row['HOSTNAME'].strip() in test_fqdn:
            pass
        else:
            test_fqdn.append(row['HOSTNAME'])
#print(len(test_fqdn))
a = set(test_fqdn)
b = set(hosts)
fqdn = a.union(b)
print(len(fqdn))   #<class 'set'>
           












'''Finding missing servers'''#not needed if use set(set combene 2 lists)
#for x in hosts:
#    if x in fqdn:
#        pass
#    else:
#        print('missng hosts = ',x)
#        missing_hosts.append(x)
        
'''Adding IPs'''
for host in hosts:
    t_dict[host] = []

with open('C:\\Users\\A645674\\Downloads\\IPs.csv') as file:
    reader = csv.DictReader(file, delimiter=',')
    for row in reader:
        if row['HOSTNAME'].strip() in hosts:
        
#'''set the filter which IPs addr should be added (don't forget to put spaces in the line below 't_dict ...')'''        
#            if re.search(pat_IPs, row['DESCRIPTION']):

            t_dict[row['HOSTNAME']].append(row['IPADDR'].split())
#print(len(with_IP))
print('t_dict = ', len(t_dict))

'''Witing to CSV'''
#FQDN_list = ' '.join(FQDN)

field_name = ['Hostnames','FQDN', 'IP' ]

with open('C:\\Users\\A645674\\Downloads\\report.csv', 'w', newline='') as report:
    writer1 = csv.DictWriter(report, fieldnames=field_name)
    writer1.writeheader()
with open('C:\\Users\\A645674\\Downloads\\report.csv', 'a', newline='') as report:    
    writer2 = csv.writer(report)
    for k,v in t_dict.items():
        for item in FQDN:
            if re.search('^'+k+'\.', item):
                writer2.writerow([k,item,v])
    for missing_host in missing_hosts:
        writer2.writerow([missing_host,'no FQDN', 'no IP'])

            
    












from selenium import webdriver
from selenium.webdriver.support.select import Select  # Select class needed for drop-down list
import time
import PY
##########################REPORT_FROM_ATCO##################################################################
#chrome_options = webdriver.ChromeOptions()
#prefs = {"download.default_directory": 'C:\\Users\\A645674\\'}
#chrome_options.add_experimental_option("prefs", prefs)
#browser = webdriver.Chrome(executable_path='C:\\Users\\A645674\\Downloads\\chromedriver', options=chrome_options)

browser = webdriver.Chrome('C:\\Users\\A645674\\Downloads\\chromedriver')
browser.get('https://A645674:vmvRjcKi4!92barepaPPP@mstoolbe.it-solutions.myatos.net/MDR/Report')

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
hosts.select_by_value('1')

time.sleep(1)

csv = Select(browser.find_element_by_name('ReportFormatID'))
csv.select_by_value('2')

time.sleep(1)

go = browser.find_element_by_id('submit')
go.click()

#time.sleep(20)

html_source = browser.page_source

#with open('C:\\Users\\A645674\\host.csv', 'w', encoding='utf-8') as f:
#    s1 = html_source.replace('<html><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">', '')
#    s2 = s1.replace('</pre></body></html>', '')
    
##    soup = BeautifulSoup(html_source, 'html.parser')
##    for x in soup:
##        f.write(str(x))
#    f.write(html_source)

text = browser.find_element_by_tag_name('pre').text
with open('C:\\Users\\A645674\\host.csv', 'w', encoding='utf-8') as f:
     f.write(text)

############################Authentication_&_write_file_with_selenium########################################
'''r = requests.get('https://A645674:PASSWORD@mstoolbe.it-solutions.myatos.net/MDR/Report/Hosts.txt', stream=True)
r = requests.get('https://mstoolbe.it-solutions.myatos.net/MDR/Report/Hosts.txt', auth=('A645674', 'password'))
r = requests.get('https://mstoolbe.it-solutions.myatos.net/MDR/Report/Hosts.txt', auth=HTTPBasicAuth('A645674','password'))

open('C:\\Users\\A645674\\host.csv', 'wb').write(r.content)'''
##############################################################################################################


# path = 'C:\\Users\\A645674\\Desktop\\Atom\\FOR_ATOS\\'
# # Load config
# with open(path + 'servers.yml') as config:
#     config_file = yaml.load(config, Loader=yaml.BaseLoader)
#
# for x in config_file:
#
#     browser = webdriver.Chrome('C:\\Users\\A645674\\Downloads\\chromedriver')
#     browser.get('https://defthw99w6fsrv.ww930.my-it-solutions.net/pilotCfg/?page=configurator')
#
#     host = config_file[x]['host']
#     IP = config_file[x]['IP']
#     MASK = config_file[x]['MASK']
#     GW = config_file[x]['GW']
#     dns = config_file[x]['dns']
#     FIRSTDNS_DNS_IP = config_file[x]['FIRSTDNS_DNS_IP']
#     SECOND_DNS_IP = config_file[x]['SECOND_DNS_IP']
#     is_VPS = config_file[x]['is_VPS']
#     is_USA = config_file[x]['is_USA']
#     DNS_IP = FIRSTDNS_DNS_IP + "," + SECOND_DNS_IP
# #==========================================
#     if dns == 'ad001':
#         DNS = 'ad001.siemens.net'
#     elif dns == 'ad101':
#         DNS = 'AD101.siemens-energy.net'
#     else:
#         DNS = dns
#         print('not correct data --> ', DNS)
# #==========================================
#     if is_VPS == 'yes':
#         Office_scan = 'not_needed'
#     elif is_VPS == 'no':
#         Office_scan = 'needed'
#     else:
#         Office_scan = is_VPS
#         print('Invali data --> ',Office_scan)
# #==========================================
#     if is_USA == 'yes':
#         NAGIOS = '161.134.149.219:8080'
#     elif is_USA == 'no':
#         NAGIOS = '139.22.145.110'
#     else:
#         NAGIOS = is_USA
#         print('Invali data --> ',NAGIOS)
# #=======================Drop-down menu========================================
#     def select_el(name):
#         for x,y in DROP_EL.items():
#             obj = Select(browser.find_element_by_name(x))
#             obj.select_by_value(y)
#
#     DROP_EL = {
# 'windows_vendor_id':'7',
# 'windows_system_id':'221',
# 'id_cfg_windows_customer':'9_Siemens',
# 'windows_keyboardlayout':'en-US_0409:00000409_1',
# 'windows_locals':'en-US_1_0409'
# }
#
#     select_el(DROP_EL)
# #=========================TabBar/SearchBar=======================================
#     def SearchBar(name):
#         for x,y in element.items():
#             TabBar = browser.find_element_by_name(x)
#             TabBar.send_keys(y)
#
#     element = {
#     'cfg_windows_memory':'8192',
#     'cfg_windows_contact_name':'Angelika Schmid',
#     'cfg_windows_computername':host,
#     'cfg_windows_localadminpasswd':'loc4dmCAP313!wintel',
#     'localadminpasswdcon':'loc4dmCAP313!wintel',
#     'cfg_NetAdapter1_IPAddress':IP,
#     'cfg_NetAdapter1_Subnet':MASK,
#     'cfg_NetAdapter1_Gateway':GW,
#     'cfg_NetAdapter1_DNSDomain':DNS,
#     'cfg_NetAdapter1_DNSServer':DNS_IP
#     }
#
#     SearchBar(element)
# #==========================Click on 'Continue to packages' button=====================
#     elem = browser.find_element_by_id('CreateConfig')
#     elem.click()
# #===========================Page_2=====================================
# #==========================Check_BOX===================================
#     '''Monitoring = ASE Nagios Client'''
#     box = browser.find_elements_by_name('chkb_pkg_nacl-ase_nacl-ase')
#     box[1].click()
#     '''if office_scan is needed'''
#     if Office_scan == 'not_needed':
#         scan = browser.find_elements_by_name('chkb_pkg_ofcscancl_officescan')
#         scan[1].click()
#     else:
#         pass
#     '''Crowdstrike'''
#     CS = browser.find_elements_by_name('chkb_pkg_falconsensor_falconsensor-x64')
#     CS[1].click()
#     button = browser.find_elements_by_id('popup_ok')
#     button[0].click()
#     '''NAGIOS'''
#     nag = browser.find_element_by_name('pkgp_nacl-ase_server')
#     nag.send_keys(NAGIOS)
#     '''Security_Package'''
#     security = browser.find_element_by_name('cfg_sccmosd_CertSecureInstallIP')
#     security.send_keys(IP)
#     '''Timeserver'''
#     time = browser.find_element_by_name('pkgp_w32time_TimeServer')
#     time.send_keys(FIRSTDNS_DNS_IP)
# #==========BUTTON CREATE=======================
#     create = browser.find_element_by_id('button')
#     create.click()
#
#     end = input("Do you want to continue? ")
#     while end != 'yes':
#         end = input("Do you want to continue? ")

    #conf = browser.find_elements_by_id('popup_ok')
    #config.click()

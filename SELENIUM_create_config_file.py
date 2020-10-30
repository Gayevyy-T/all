from selenium import webdriver
from selenium.webdriver.support.select import Select  # Select class needed for drop-down list

browser = webdriver.Chrome('C:\\Users\\A645674\\Downloads\\chromedriver')
browser.get('https://defthw99w6fsrv.ww930.my-it-solutions.net/pilotCfg/?page=configurator')
#tab = browser.find_element_by_link_text('Download')
#print(tab.text)   #--> Download
#print(tab.get_attribute('href')) # output - link to the Download page
#tab.click() #--> will do to the indicated TAB

'''Variables'''
host = input("Enter Hostname: ")
password = 'loc4dmCAP313!wintel'
IP = input("Enter IP: ")
MASK = input("Enter MASK: ")
GW = input("Enter GateWay: ")

'''DNS'''
count = 0
while count != 1:
    dns = input("Enter 'ad001' or 'ad101': ")
    #dns = 'ad001'
    if dns == 'ad001':
        DNS = 'ad001.siemens.net'
        count+=1
    elif dns == 'ad101':
        DNS = 'AD101.siemens-energy.net'
        count += 1
    else:
        DNS = dns
        print('not correct data --> ', DNS)

FIRSTDNS_DNS_IP = input("Enter 1st DNS IP: ")
SECOND_DNS_IP = input("Enter 2nd DNS IP: ")
DNS_IP = FIRSTDNS_DNS_IP + "," + SECOND_DNS_IP

'''TrendMicro'''
count2 = 0
while count2 != 1:
    office_scan = input('is the server VPS (yes/no)? ')
    if office_scan == 'yes':
        Office_scan = 'not_needed'
        count2 += 1
    elif office_scan == 'no':
        Office_scan = 'needed'
        count2 += 1
    else:
        Office_scan = office_scan
        print('Invali data --> ',Office_scan)
'''Nagios'''
count3 = 0
while count3 != 1:
    nagios = input('is it USA server (yes/no)? ')
    if nagios == 'yes':
        NAGIOS = '161.134.149.219:8080'
        count3 += 1
    elif nagios == 'no':
        NAGIOS = '139.22.145.110'
        count3 += 1
    else:
        Office_scan = office_scan
        print('Invali data --> ',Office_scan)
#=======================Drop-down menu========================================
'''Hardware Vendor = VMWare'''
obj = Select(browser.find_element_by_name('windows_vendor_id'))
obj.select_by_value('7')
'''Hardware System = ESX6'''
obj = Select(browser.find_element_by_name('windows_system_id'))
obj.select_by_value('221')
'''Customer = Siemens'''
obj = Select(browser.find_element_by_name('id_cfg_windows_customer'))
obj.select_by_value('9_Siemens')
'''Keyboardlayout = US'''
obj = Select(browser.find_element_by_name('windows_keyboardlayout'))
obj.select_by_value('en-US_0409:00000409_1')
'''Locale Settings = US'''
obj = Select(browser.find_element_by_name('windows_locals'))
obj.select_by_value('en-US_1_0409')
#=========================TabBar/SearchBar=======================================
'''Memory Size: (MB) = 8192 (for VM)'''
TabBar = browser.find_element_by_name('cfg_windows_memory')
TabBar.send_keys('8192')
'''Contact Name = Angelika Schmid'''
TabBar = browser.find_element_by_name('cfg_windows_contact_name')
TabBar.send_keys('Angelika Schmid')
'''Computer Name'''
TabBar = browser.find_element_by_name('cfg_windows_computername')
TabBar.send_keys(host)
'''PASSWORD'''
TabBar = browser.find_element_by_name('cfg_windows_localadminpasswd')
TabBar.send_keys(password)
TabBar = browser.find_element_by_name('localadminpasswdcon')
TabBar.send_keys(password)
'''IP Address'''
TabBar = browser.find_element_by_name('cfg_NetAdapter1_IPAddress')
TabBar.send_keys(IP)
'''Subnet Mask'''
TabBar = browser.find_element_by_name('cfg_NetAdapter1_Subnet')
TabBar.send_keys(MASK)
'''Gateway'''
TabBar = browser.find_element_by_name('cfg_NetAdapter1_Gateway')
TabBar.send_keys(GW)
'''DNS Domain'''
TabBar = browser.find_element_by_name('cfg_NetAdapter1_DNSDomain')
TabBar.send_keys(DNS)
'''DNS Server Adresses'''
TabBar = browser.find_element_by_name('cfg_NetAdapter1_DNSServer')
TabBar.send_keys(DNS_IP)
#==========================Click on 'Continue to packages' button=====================
elem = browser.find_element_by_id('CreateConfig')
elem.click()
#===========================Page_2=====================================
#==========================Check_BOX===================================
'''Monitoring = ASE Nagios Client'''
box = []
box = browser.find_elements_by_name('chkb_pkg_nacl-ase_nacl-ase')
box[1].click()
'''if office_scan is needed'''
if Office_scan == 'not_needed':
    scan = []
    scan = browser.find_elements_by_name('chkb_pkg_ofcscancl_officescan')
    scan[1].click()
else:
    pass
'''Crowdstrike'''
CS = browser.find_elements_by_name('chkb_pkg_falconsensor_falconsensor-x64')
CS[1].click()
button = browser.find_elements_by_id('popup_ok')
button[0].click()
'''NAGIOS'''
nag = browser.find_element_by_name('pkgp_nacl-ase_server')
nag.send_keys(NAGIOS)
'''Security_Package'''
security = browser.find_element_by_name('cfg_sccmosd_CertSecureInstallIP')
security.send_keys(IP)
'''Timeserver'''
time = browser.find_element_by_name('pkgp_w32time_TimeServer')
time.send_keys(FIRSTDNS_DNS_IP)
#==========BUTTON CREATE=======================
create = browser.find_element_by_id('button')
create.click()


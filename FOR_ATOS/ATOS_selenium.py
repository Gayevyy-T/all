from selenium import webdriver
from selenium.webdriver.support.select import Select  # Select class needed for drop-down list

browser = webdriver.Chrome('C:\\Users\\A645674\\Downloads\\chromedriver')
browser.get('https://defthw99w6fsrv.ww930.my-it-solutions.net/pilotCfg/?page=configurator')

'''Variables'''
host = input("Enter Hostname: ")
#password = 'loc4dmCAP313!wintel'
IP = input("Enter IP: ")
MASK = input("Enter MASK: ")
GW = input("Enter GateWay: ")

'''DNS'''
count = 0
while count != 1:
    dns = input("Enter 'ad001' or 'ad101': ")
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
def select_el(name):
    for x,y in DROP_EL.items():
        obj = Select(browser.find_element_by_name(x))
        obj.select_by_value(y)

DROP_EL = {
'windows_vendor_id':'7',
'windows_system_id':'221',
'id_cfg_windows_customer':'9_Siemens',
'windows_keyboardlayout':'en-US_0409:00000409_1',
'windows_locals':'en-US_1_0409'
}

select_el(DROP_EL)
#=========================TabBar/SearchBar=======================================
def SearchBar(name):
    for x,y in element.items():
        TabBar = browser.find_element_by_name(x)
        TabBar.send_keys(y)

element = {
'cfg_windows_memory':'8192',
'cfg_windows_contact_name':'Angelika Schmid',
'cfg_windows_computername':host,
'cfg_windows_localadminpasswd':'loc4dmCAP313!wintel',
'localadminpasswdcon':'loc4dmCAP313!wintel',
'cfg_NetAdapter1_IPAddress':IP,
'cfg_NetAdapter1_Subnet':MASK,
'cfg_NetAdapter1_Gateway':GW,
'cfg_NetAdapter1_DNSDomain':DNS,
'cfg_NetAdapter1_DNSServer':DNS_IP
}

SearchBar(element)
#==========================Click on 'Continue to packages' button=====================
elem = browser.find_element_by_id('CreateConfig')
elem.click()
#===========================Page_2=====================================
#==========================Check_BOX===================================
'''Monitoring = ASE Nagios Client'''
box = browser.find_elements_by_name('chkb_pkg_nacl-ase_nacl-ase')
box[1].click()
'''if office_scan is needed'''
if Office_scan == 'not_needed':
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



















# def sum_divisors(n):
#     sum = 0
#     x = 1
#
#     while n != 0 and x < n:
#         if n % x == 0:
#             sum += x
#         x += 1
#     return sum
#
# print(sum_divisors(0))
# # 0
# print(sum_divisors(3)) # Should sum of 1
# # 1
# print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# # 55
# print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# # 114


#============================
#def sum_of_divisors(num):
#    return sum([i for i in range(1, num) if num % i == 0])
from selenium import webdriver
from bs4 import BeautifulSoup
import json
import time
import itertools


def get_brands():

    chromedriver = "//chromedriver"
    driver = webdriver.Chrome(chromedriver)
    driver.get("http:gsmarena.com")
    html_source = driver.page_source

    soup = BeautifulSoup(html_source, 'html.parser')
    brands = {}

    brand_menu = soup.find('div', class_='brandmenu-v2 light l-box clearfix')

    brand_list = brand_menu.find('ul').find_all('li')
    for li in brand_list:
        brands[li.a.text]=li.a['href']

    with open('brands_urls.json', 'w') as f:
        json.dump(brands, f)
    
    driver.quit()
    return brands  

def get_devices(brand_dic):
    devices = {}
    brand_dict = dict(itertools.islice(brand_dic.items(), 3))  #slicing number of brands upto crawler runs

    for brand_name, link in brand_dict.items():

        chromedriver = "/home/khizer/Downloads/chromedriver"
        driver = webdriver.Chrome(chromedriver)
        driver.get("http:gsmarena.com/"+link)
        html_source = driver.page_source

        devices_links = []
        
        soup = BeautifulSoup(html_source, 'html.parser')
        device_menu = soup.find('div', class_='makers')

        device_list = device_menu.find('ul').find_all('li')

        for li in device_list:
            devices_links.append(li.a['href'])
            print(li.a['href'])

        devices[brand_name] = devices_links  
        print("\nLIST DONE FOR "+brand_name) 
        driver.quit()

    with open('devices_urls.json', 'w') as f:
        json.dump(devices, f)
    return devices    


def get_specs(devices_dic):

    all_spec = {}
    devices_dict = dict(itertools.islice(devices_dic.items(), 3))  #slicing number of brands upto crawler runs
    for brand_name, linkss in devices_dict.items():
        links = linkss[0:3]   # slicing number of devices in each brand
        brand_specs_dict = {}

        for link in links:

    
            chromedriver = "/home/khizer/Downloads/chromedriver"
            driver = webdriver.Chrome(chromedriver)
            driver.get("http:gsmarena.com/"+link)
            html_source = driver.page_source
                    
            soup = BeautifulSoup(html_source, 'html.parser')
            specs_menu = soup.find('div', id='specs-list').find_all('table')
            for i,sp in enumerate(specs_menu):
                if sp.find('tbody').find("tr").find("th").text == 'Display':
                    display_index = i
                    break

            display_table =  specs_menu[display_index]
            single_specs_dict = {} 
            for sp in display_table.find("tbody").find_all("tr"):
                single_specs_dict[sp.find('td',class_= 'ttl').text] = sp.find('td',class_= 'nfo').text

            link1 = link.split('-')[0]     
            brand_specs_dict[link1] = single_specs_dict
            print(single_specs_dict)
            driver.quit()

        with open(brand_name+'_allDevices_specs.json', 'w') as f:
            json.dump(brand_specs_dict, f)
        all_spec[brand_name] = brand_specs_dict  

    return all_spec    

      



brand_dict = get_brands()
devices_dict = get_devices(brand_dict)
spec_dict = get_specs(devices_dict)
print (spec_dict)

with open('GsmArena.json', 'w') as f:
    json.dump(spec_dict, f)

import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest
import lxml

laptops_name = []
laptops_price = []
laptops_time_left = []
laptops_sec_info = []
links = []
details = []
page_num = 1

#while True:
result = requests.get(
        f"https://www.ebay.de/sch/i.html?_from=R40&_nkw=dell+laptop&_sacat=0&rt=nc&LH_Auction={page_num}")
src = result.content
soup = BeautifulSoup(src, "lxml")
    #page_limit = (1)
   # if (page_num > page_limit):
      #  print("pages ended ,terminate")
        #break
laptop_name = soup.find_all("a", {"class": "s-item__link"})
laptop_price = soup.find_all("span", {"class": "s-item__price"})
laptop_time_left = soup.find_all("span", {"class": "s-item__time-left"})
laptop_sec_info = soup.find_all("span", {"class": "SECONDARY_INFO"})

for i in range(len(laptop_name)):
        laptops_name.append(laptop_name[i].text)
        links.append(laptop_name[i].get('href'))
        laptops_price.append(laptop_price[i].text)
        laptops_time_left.append(laptop_time_left[i].text)
        laptops_sec_info.append(laptop_sec_info[i].text)
print(laptops_time_left)
for link in links:
    result = requests.get(link)
    src = result.content
    soup = BeautifulSoup(src, "lxml")
    laptop_details = soup.find_all("table", {"width": "100%", "role": "presentation"})
    details.append(laptop_details)

    print(details)
    page_num += 1
    print("page switched")

file_list = [laptops_name, laptops_price, laptops_time_left, laptops_sec_info, links, details]
exported = zip_longest(*file_list)

with open("C:/Users/Marwa/LaptopEbayDell.csv", "w") as myfile:
    wr = csv.writer(myfile)
    wr.writerow(["Laptop_name", "Laptop_price", "Laptop_time_left", "Laptop_sec_info", "Links", "Details"])
    wr.writerows(exported)

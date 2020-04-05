from bs4 import BeautifulSoup
from urllib.request import urlopen as ureq

#country list

def show_countries(c):
    for i in range(len(c)):
        print("({0})".format(i+1), c[i])

# WORLDOMETER.INFO
url ="https://www.worldometers.info/coronavirus/"

#sending request to worldometer
client = ureq(url)
page= client.read()
client.close()   #connection closed

#parsing the page
page_soup = BeautifulSoup(page,'html.parser')

#getting data present in table celles
container = page_soup.findAll("td")

#geting data from the page
data = [i.text.strip() if i.text.strip() else "0" for i in container ]
countries = [data[i] for i in range(len(data)) if data[i][0].isalpha()]
json_format_data ={}
for i in range(len(data)):
    if data[i][0].isalpha():
        ele=data[i].lower()
        json_format_data[ele]=[]
    else:
        json_format_data[ele].append(data[i])
print("---------Corona Case Details---------")
label=["Total Cases", "New Cases","Total Deaths","New Deaths", "Total Recovered", "Active Cases", "Serious Critical","Tot Cases/1M pop", "Tot Deaths/1M pop"]
for i in range(9):
    print(label[i],"-------->",json_format_data["total:"][i])
enter = int(input("Enter 1 to see the country List or 0 to skip: "))
if enter ==1:
    show_countries(countries)
country_name =input("Enter the Country Name, To See its Corona Cases: ").lower()
print("\n\n ------Corona Cases in {0}--------".format(country_name))
for i in range(9):
    print(label[i],"-------->",json_format_data[country_name][i])
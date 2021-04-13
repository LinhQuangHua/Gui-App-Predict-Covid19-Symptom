
import pandas as pd
import requests
from bs4 import BeautifulSoup

def case():
    page = requests.get('https://www.worldometers.info/coronavirus/country/viet-nam/')
    soup = BeautifulSoup(page.content, 'html.parser')
    week = soup.find(class_='col-md-8')

    item = week.find_all(id='maincounter-wrap')
    items = week.find_all(class_='maincounter-number')
    
##    print(item[0].find('h1').get_text())
##    print(items[0].find('span').get_text())
    x = items[0].find('span').get_text()
    print(x)
    return x


def dead():

    page = requests.get('https://www.worldometers.info/coronavirus/country/viet-nam/')
    soup = BeautifulSoup(page.content, 'html.parser')
    week = soup.find(class_='col-md-8')

    item = week.find_all(id='maincounter-wrap')
    items = week.find_all(class_='maincounter-number')
    
##    print(item[1].find('h1').get_text())
##    print(items[1].find('span').get_text())
    x = items[1].find('span').get_text()
    print(x)
    return x

def cover():

    page = requests.get('https://www.worldometers.info/coronavirus/country/viet-nam/')
    soup = BeautifulSoup(page.content, 'html.parser')
    week = soup.find(class_='col-md-8')

    item = week.find_all(id='maincounter-wrap')
    items = week.find_all(class_='maincounter-number')
    
##    print(item[2].find('h1').get_text())
    x = items[2].find('span').get_text()
    print(x)
    return x

def main():
    case()
    dead()
    cover()
main()


                   























from bs4 import BeautifulSoup
import requests
import phonezameen
from openpyxl import Workbook, load_workbook

wb = load_workbook('ZameenScrap.xlsx')
ws = wb.active
ws.append(['Title', 'Location', 'Price', 'Agency', 'Agent', 'Mobile Number', 'Name', 'Verifying Names'])

x1 = 1
for page_number in range(1,3):
    web = requests.get(f'https://www.zameen.com/Homes/Lahore-1-{page_number}.html').text
    soup = BeautifulSoup(web,'lxml')
    #here i have have complete text  of the first page i hit.
    #now i am going to open sub links and then scraping title,desription, price, features
    print('HITTING PAGE NUMBER = ',page_number)

    for article in soup.find_all('article'):
        incomplete_link = article.find('a')['href']
        proper_sub_link = f'https://www.zameen.com/{incomplete_link}'

        web = requests.get(proper_sub_link).text
        sub_soup = BeautifulSoup(web,'lxml')

        print('hitting card number =  ',x1)
        x1 += 1


        for x in sub_soup.find_all('main'):
            # title
            try:
                title = x.find('h1',class_='_64bb5b3b').text
            except Exception as e:
                title = 'Its an advertisement'

            #location
            try:
                location = x.find('div',class_='cbcd1b2b').text
            except Exception as e:
                location = None

            #price
            try:
                price = x.find('div',class_='c4fc20ba').text
            except Exception as e:
                price = None

            # agency
            try:
                agency = x.find('div', class_='_5a588edf').text
            except Exception as e:
                agency = None

            # agent name
            try:
                agent = x.find('span', class_='_725b3e64').text
            except Exception as e:
                agent = None

            agent2,mobile,phone = phonezameen.table_data(proper_sub_link)

            print(title,location,price,agency,agent,mobile,phone,agent2, sep='\n')
            print()

            ws.append([title,location,price,agency,agent,mobile,phone,agent2])
            wb.save('ZameenScrap.xlsx')
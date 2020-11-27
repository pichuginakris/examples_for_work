import requests
from bs4 import BeautifulSoup
import time
import logging
import telebot
import psycopg2


TOKEN = '*'
bot = telebot.TeleBot(TOKEN)
CHANNEL_NAME = '*'


@bot.message_handler(content_types=['text'])
def mes(text):
    bot.send_message(CHANNEL_NAME, text)


def creating_bd(data, pointer):
    try:
        connect_str = "dbname='jooble' user='jooble' password='*' host='*'"
        conn = psycopg2.connect(connect_str)
        cursor = conn.cursor()
        conn.commit()
        if pointer == 0:
            cursor.execute('DELETE FROM tables_jooblesingapore;')
            conn.commit()
        try:
            print(data)
            cursor.execute("INSERT INTO tables_jooblesingapore(vacancy, link_to_a_vacancy, salary, company, " +
                                                      "short_description, location, date_from_creation, " +
                                                      "full_description, link_to_a_company) values (" +
                           "'" + (data['vacancy']).replace("'", "") + "','" + (data['href']).replace("'", "")
                           + "','" + (data['salary']).replace("'", "") + "','" + (data['company']).replace("'", "")
                           + "','" + (data['short_description']).replace("'", "") + "','" +
                           (data['location']).replace("'", "") + "','" + (data['date']).replace("'", "") + "','" +
                           (data['full_description']).replace("'", "") + "','" +
                           (data['company_href']).replace("'", "") + "')")
            conn.commit()
        except Exception as ex:
            logging.error(
                'Exception of type {!s} in jooble_parser_singapore.py creating_bd(data, pointer): {!s}'.format(type(ex).__name__,  str(ex)))
            mes('Data base error in jooble_parser_singapore.py. See file logging_jooble_singapore.log for details')
        cursor.close()
        conn.close()
    except Exception as ex:
        logging.error(
            'Exception of type {!s} jooble_parser_singapore.py creating_bd(data, pointer): {!s}'.format(type(ex).__name__, str(ex)))
        mes('Data base error in jooble_parser_singapore.py. See file logging_jooble_singapore.log for details')


def transfer_to_dollar(salary, all_money):
    all_symbols = ['₹', 'R', '£', '€']
    pointer = "False"
    sum1 = ''
    sum2 = ''
    money = str(salary).replace(',', '')
    print(salary)
    salary_v2 = salary
    if len(money) > 0:
        for one_sym in all_symbols:
            if money[0] == one_sym:
                pointer = 'True'
        if pointer == 'True':
            k = 1
            the_rest = ''
            while k < (len(money)):
                if sum1 == '' and sum2 == '':
                    while '0' <= money[k] <= '9':
                        sum1 = sum1 + (money[k])
                        k = k + 1
                if sum1 != '' and sum2 == '':
                    while '0' <= money[k] <= '9':
                        sum2 = sum2 + (money[k])
                        k = k + 1
                if money[k] != money[0] and money[k] != '-':
                    the_rest = the_rest + money[k]
                k = k + 1
            if money[0] == all_symbols[0]:
                sum1 = float(sum1) * all_money[0] / all_money[4]
                if sum2 != '':
                    sum2 = float(sum2) * all_money[0] / all_money[4]
            if money[0] == all_symbols[1]:
                sum1 = float(sum1) * all_money[1] / all_money[4]
                if sum2 != '':
                    sum2 = float(sum2) * all_money[1] / all_money[4]
            if money[0] == all_symbols[2]:
                sum1 = float(sum1) * all_money[2] / all_money[4]
                if sum2 != '':
                    sum2 = float(sum2) * all_money[2] / all_money[4]
            if money[0] == all_symbols[3]:
                sum1 = float(sum1) * all_money[3] / all_money[4]
                if sum2 != '':
                    sum2 = float(sum2) * all_money[3] / all_money[4]
            sum1 = round(sum1, 0)
            if sum2 != '':
                sum2 = round(sum2, 0)
                salary_v2 = '$' + str(sum1) + ' - $' + str(sum2) + the_rest
            else:
                salary_v2 = '$' + str(sum1) + the_rest
    print(salary_v2)
    return salary_v2


def searching(url, all_money):  # parsing
    logging.basicConfig(filename='logging_jooble_singapore.log', filemode='a',
                        format='%(process)s - %(asctime)s - %(levelname)s - %(message)s')
    pattern = url + '&p={}'
    pointer = 0
    for i in range(1, 50):
        print(i)
        url = pattern.format(str(i))
        print(url)
        time.sleep(2)
        try:
            response = requests.get(url)
            html = response.text
            soup = BeautifulSoup(html, 'lxml')
            vacancies = soup.find_all('div', class_='left-static-block')
            for vacancy in vacancies:
                vacancy_name = vacancy.find('h2', class_='position').text
                vacancy_name = vacancy_name.strip()
                vacancy_href = vacancy.find('a').get('href')
                try:
                    b = str(vacancy_href).split('away')
                    ref = b[0] + 'desc' + b[1]  # getting full vacancy page in jooble
                except:
                    ref = vacancy_href
                time.sleep(2)
                response_two = requests.get(ref)  # open full vacancy page in jooble to get full description
                html_two = response_two.text
                soup_two = BeautifulSoup(html_two, 'lxml')
                description_full = ''
                try:
                    reference = soup_two.find('div', class_='bc32c bf012').find('a').get('href')
                    response2 = requests.get(reference)  # finding original vacancy link
                    html2 = response2.text
                    soup2 = BeautifulSoup(html2, 'lxml')
                    original_link = soup2.find('div', class_='redirect_container').find('a').get('href')
                    original_link = 'h' + original_link[1:]
                    original_link = original_link.split('utm_source')  # delete jooble from a link
                    original_link = original_link[0]
                except:
                    logging.warning('The vacancy reference is missing in ' + ref)
                    reference = ''
                print(reference)
                try:
                    full_descriptions = soup_two.find_all('div', class_='a708d')
                    for des in full_descriptions:
                        description_full = description_full + (des.text).strip()
                    print(description_full)
                except:
                    logging.warning('The full description is missing in ' + ref)
                    description_full = ''
                try:
                    salary = vacancy.find('span', class_='salary').text
                    salary = transfer_to_dollar(salary, all_money)
                except:
                    logging.warning('The salary is missing in ' + ref)
                    salary = ''
                try:
                    organization = vacancy.find('span', class_='gray_text company-name').text
                except:
                    logging.warning('The company name is missing in ' + ref)
                    organization = ''
                location = vacancy.find('div', class_='serp_location').find('span').text
                location = location.strip()
                try:
                    date = vacancy.find('div', class_='date_from_creation').text
                    date = date.strip()
                except:
                    logging.warning('The date is missing in ' + ref)
                    date = ''
                data = {'vacancy': vacancy_name,
                        'href': ref,
                        'salary': salary,
                        'company': organization,
                        'short_description': description_full,
                        'location': location,
                        'date': date,
                        'full_description': description_full,
                        'company_href': original_link
                        }
                creating_bd(data, pointer)
                pointer = pointer + 1
        except Exception as ex:
            logging.error('Exception of type {!s} in jooble_parser_singapore searching(url, all_money): {!s}'.format(type(ex).__name__, str(ex)))
            mes('Wrong site url in jooble_parser_singapore.py. See file logging_jooble_singapore.log for details')


def main():
    url1 = 'http://www.cbr.ru/scripts/XML_daily.asp?'
    try:
        response = requests.get(url1)
        html = response.text
        soup = BeautifulSoup(html, 'lxml')
        valutes = soup.find('html').find_all('valute')
        for valute in valutes:
            id = valute.find('numcode').text
            nominal = valute.find('nominal').text
            if id == '356':
                rupiy = float(valute.find('value').text.replace(',', '.')) / float(nominal)
            if id == '826':
                funt = float(valute.find('value').text.replace(',', '.')) / float(nominal)
            if id == '978':
                euro = float(valute.find('value').text.replace(',', '.')) / float(nominal)
            if id == '710':
                rend = float(valute.find('value').text.replace(',', '.')) / float(nominal)
            if id == '840':
                dollar = float(valute.find('value').text.replace(',', '.')) / float(nominal)
        all_money = [rupiy, rend, funt, euro, dollar]
        reference = 'https://sg.jooble.org/jobs?rt=1'
        searching(reference, all_money)
    except Exception as ex:
        logging.error(
            'Exception of type {!s} in jooble_parser_singapore.py main(): {!s}'.format(type(ex).__name__,
                                                                                         str(ex)))
        mes('Wrong site url in jooble_parser_singapore.py See file logging_jooble_singapore.log for details')


if __name__ == '__main__':
    main()

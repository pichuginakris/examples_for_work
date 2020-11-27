import requests
from bs4 import BeautifulSoup
import time
import logging
import telebot
import psycopg2

# Параметры бота (токен и наименование канала)
TOKEN = '*'
bot = telebot.TeleBot(TOKEN)
CHANNEL_NAME = '*'


# Обработчик сообщений
@bot.message_handler(content_types=['text'])
def mes(text):
    bot.send_message(CHANNEL_NAME, text)


# Заполнение таблиц из базы данных
def creating_bd(data, pointer):
    try:
        # Параметры базы данных и соединение с ней
        connect_str = "dbname='jooble' user='jooble' password='*' host='*'"
        conn = psycopg2.connect(connect_str)
        # Создание курсора для выполнения команд PostgreSQL в сеансе базы данных.
        cursor = conn.cursor()
        # Удаление старых данных из таблицы в случае, если программа только начала работать
        if pointer == 0:
            # Выполнение команды PostgreSQL DELETE
            cursor.execute('DELETE FROM tables_joobleusa;')
            # Внесение команды в бд (без него команда не будет выполнена на уровне базы данных)
            conn.commit()
        try:
            # Вставка данных
            cursor.execute("INSERT INTO tables_joobleusa(vacancy, link_to_a_vacancy, salary, company, " +
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
            # Отправление отчета об ошибки в файл  logging_jooble_usa.log в случае неполадок со вставкой
            logging.error(
                'Exception of type {!s} in jooble_parser_usa.py creating_bd(data, pointer): {!s}'.format(type(ex).__name__,  str(ex)))
            # Отправление отчета об ошибки в телеграм в случае неполадок со вставкой
            mes('Data base error in jooble_parser_usa.py. See file logging_jooble_usa.log for details')
        # Закрытие курсора
        cursor.close()
        # Закрытие соединения
        conn.close()
    except Exception as ex:
        # Отправление отчета об ошибки в файл  logging_jooble_usa.log в случае неполадок с бд
        logging.error(
            'Exception of type {!s} jooble_parser_usa.py creating_bd(data, pointer): {!s}'.format(type(ex).__name__, str(ex)))
        # Отправление отчета об ошибки в телеграм в случае неполадок с бд
        mes('Data base error in jooble_parser_usa.py. See file logging_jooble_usa.log for details')


# Перевод валют в доллары (принимает сведения о заплате в формате, например, ₹134-₹1424 in a month и значения валют
def transfer_to_dollar(salary, all_money):
    all_symbols = ['₹', 'R', '£', '€']
    # Счетчик для проверки, присутствует ли один из символов в сведениях о зарплате
    pointer = "False"
    # Объявление первого и второго числа из сведений о зарплате
    sum1 = ''
    sum2 = ''
    # Удаление лишних символов
    money = str(salary).replace(',', '')
    # Объявление второй версии сведений о зарплате. Переведенная валюта в доллары
    salary_v2 = ''
    # Определяет, не пустое ли значение в сведениях о зарплате
    if len(money) > 0:
        # Сравнение первого символа с имеющимся списком символов валют
        for one_sym in all_symbols:
            if money[0] == one_sym:
                pointer = 'True'
        # Если есть необходимость в переводе в доллары (т.е. первоначальная зарплата представлена в иных валютах)
        if pointer == 'True':
            # Номер символа в строке зарплаты
            k = 1
            # Оставшаяся часть от зарплаты, например, in a month
            the_rest = ''
            # Посимвольный разбор
            while k < (len(money)):
                # Запись числа в переменную sum1 посимвольно
                if sum1 == '' and sum2 == '':
                    # Пока символы являются цифрами, идет запись в sum1
                    while '0' <= money[k] <= '9':
                        sum1 = sum1 + (money[k])
                        k = k + 1
                # Запись числа в переменную sum2 посимвольно происходит при заполнении sum1
                if sum1 != '' and sum2 == '':
                    # Пока символы являются цифрами, идет запись в sum2
                    while '0' <= money[k] <= '9':
                        sum2 = sum2 + (money[k])
                        k = k + 1
                # Запись остатка (не должен содержать символ валюты и -)
                if money[k] != money[0] and money[k] != '-':
                    the_rest = the_rest + money[k]
                k = k + 1
            # В зависимости от типа валюты происходит перевод в доллары (цифра умножается на значения курса валюты к
            # рублям, затем рубли переводятся в доллары (делятся на значение курса рубля к доллару)
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
            # Округление значений
            sum1 = round(sum1, 0)
            # Второй порог зарплаты может отсутствовать, проводится провека на наличие
            if sum2 != '':
                sum2 = round(sum2, 0)
                # Запись зарплаты в формате $14 - $50 in a month
                salary_v2 = '$' + str(sum1) + ' - $' + str(sum2) + the_rest
            else:
                # Запись зарплаты в формате $14 in a month
                salary_v2 = '$' + str(sum1) + the_rest
    print(salary_v2)
    return salary_v2


# Сбор данных с сайта Jooble
def searching(url, all_money):
    # Объявление формата лог файла
    logging.basicConfig(filename='logging_jooble_usa.log', filemode='a',
                        format='%(process)s - %(asctime)s - %(levelname)s - %(message)s')
    # Шаблон
    pattern = url + '&p={}'
    # Счетчик количества вакансий
    pointer = 0
    # Цикл по страницам с 1 по 50
    for i in range(1, 50):
        # Подстановка номера страницы в шаблон ссылки
        url = pattern.format(str(i))
        time.sleep(2)
        try:
            # Получение текста страницы и преобразование его в lxml формат
            response = requests.get(url)
            html = response.text
            soup = BeautifulSoup(html, 'lxml')
            # Нахождение всех вакансий на страницы
            vacancies = soup.find_all('div', class_='left-static-block')
            # Разбор по одной вакансии
            for vacancy in vacancies:
                # Наименование вакансии
                vacancy_name = vacancy.find('h2', class_='position').text
                vacancy_name = vacancy_name.strip()
                # Ссылка на вакансию
                vacancy_href = vacancy.find('a').get('href')
                try:
                    # Удаление из ссылки слова "away" для подстановки "desc". Результат - ссылка на вакансию
                    b = str(vacancy_href).split('away')
                    ref = b[0] + 'desc' + b[1]  # getting full vacancy page in jooble
                except:
                    # Иначе в ссылке уже стоит "desc" заместо "away"
                    ref = vacancy_href
                time.sleep(2)
                # Получение html страницы одной вакансии и преобразование её в lxml формат
                response_two = requests.get(ref)
                html_two = response_two.text
                soup_two = BeautifulSoup(html_two, 'lxml')
                description_full = ''
                try:
                    # Нахождение "оригинальной" ссылки на компанию
                    reference = soup_two.find('div', class_='bc32c bf012').find('a').get('href')
                    response2 = requests.get(reference)
                    html2 = response2.text
                    soup2 = BeautifulSoup(html2, 'lxml')
                    original_link = soup2.find('div', class_='redirect_container').find('a').get('href')
                    original_link = 'h' + original_link[1:]
                    # Удаление части "jooble" из ссылки
                    original_link = original_link.split('utm_source')
                    original_link = original_link[0]
                except:
                    # Отправление отчета об ошибки в файл  logging_jooble_usa.log в случае отсутсвия данных
                    logging.warning('The vacancy reference is missing in ' + ref)
                    reference = ''
                print(reference)
                try:
                    # Полное описание вакансии (представлено в виде словаря, поэтому соединяем воедино части описания)
                    full_descriptions = soup_two.find_all('div', class_='a708d')
                    for des in full_descriptions:
                        description_full = description_full + (des.text).strip()
                    print(description_full)
                except:
                    # Отправление отчета об ошибки в файл  logging_jooble_usa.log в случае отсутсвия данных
                    logging.warning('The full description is missing in ' + ref)
                    description_full = ''
                try:
                    # Сведения о зарплате
                    salary = vacancy.find('span', class_='salary').text
                    salary = transfer_to_dollar(salary, all_money)
                except:
                    # Отправление отчета об ошибки в файл  logging_jooble_usa.log в случае отсутсвия данных
                    logging.warning('The salary is missing in ' + ref)
                    salary = ''
                try:
                    # Сведения о наименовании организации
                    organization = vacancy.find('span', class_='gray_text company-name').text
                except:
                    # Отправление отчета об ошибки в файл  logging_jooble_usa.log в случае отсутсвия данных
                    logging.warning('The company name is missing in ' + ref)
                    organization = ''
                # Наименование города
                location = vacancy.find('div', class_='serp_location').find('span').text
                location = location.strip()
                try:
                    # Сведения о дате добавления вакансии на jooble
                    date = vacancy.find('div', class_='date_from_creation').text
                    date = date.strip()
                except:
                    # Отправление отчета об ошибки в файл  logging_jooble_usa.log в случае отсутсвия данных
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
            # Отправление отчета об ошибки в файл  logging_jooble_usa.log в случае невозможности подключения
            logging.error('Exception of type {!s} in jooble_parser_usa searching(url, all_money): {!s}'.format(type(ex).__name__, str(ex)))
            # Отправление отчета об ошибки в телеграм в случае невозможности подключения
            mes('Wrong site url in jooble_parser_usa.py. See file logging_jooble_usa.log for details')


def main():
    # Сайт курса обмена валют
    url1 = 'http://www.cbr.ru/scripts/XML_daily.asp?'
    try:
        # Получение html страницы в формате lxml
        response = requests.get(url1)
        html = response.text
        soup = BeautifulSoup(html, 'lxml')
        # Объявление названий валют
        rupiy = ''
        funt = ''
        euro = ''
        rend = ''
        dollar = ''
        # Нахождение всех имеющихся валют
        valutes = soup.find('html').find_all('valute')
        for valute in valutes:
            # Нахождение id валюты
            id = valute.find('numcode').text
            # Нахождение номинала валют (может быть представлен курс за 1 валюту, может быть за 10 валют)
            nominal = valute.find('nominal').text
            # Id 356 соответствует рупиям
            if id == '356':
                # Нахождение значения одного номинала
                rupiy = float(valute.find('value').text.replace(',', '.')) / float(nominal)
            # Id 826 соответствует рупиям
            if id == '826':
                funt = float(valute.find('value').text.replace(',', '.')) / float(nominal)
            # Id 978 соответствует рупиям
            if id == '978':
                euro = float(valute.find('value').text.replace(',', '.')) / float(nominal)
            # Id 710 соответствует рупиям
            if id == '710':
                rend = float(valute.find('value').text.replace(',', '.')) / float(nominal)
            # Id 840 соответствует рупиям
            if id == '840':
                dollar = float(valute.find('value').text.replace(',', '.')) / float(nominal)
        # Хранение всех значений
        all_money = [rupiy, funt, euro, rend, dollar]
        reference = 'https://jooble.org/jobs?rt=1'
        searching(reference, all_money)
    except Exception as ex:
        # Отправление отчета об ошибки в файл  logging_jooble_usa.log в случае невозможности подключения
        logging.error(
            'Exception of type {!s} in jooble_parser_usa.py main(): {!s}'.format(type(ex).__name__,
                                                                                         str(ex)))
        # Отправление отчета об ошибки в телеграм в случае невозможности подключения
        mes('Wrong site url in jooble_parser_usa.py See file logging_jooble_usa.log for details')


if __name__ == '__main__':
    main()

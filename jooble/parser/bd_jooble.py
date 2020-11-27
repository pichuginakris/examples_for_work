import psycopg2
import csv
import telebot
import logging


TOKEN = '*'
bot = telebot.TeleBot(TOKEN)
CHANNEL_NAME = '*'


@bot.message_handler(content_types=['text'])
def mes(text):
    bot.send_message(CHANNEL_NAME, text)


def creating_bd(country):
    logging.basicConfig(filename='logging_jooble.log', filemode='a',
                        format='%(process)s - %(asctime)s - %(levelname)s - %(message)s')
    try:
        connect_str = "dbname='jooble' user='jooble' password='*' host='*'"
        # use our connection values to establish a connection
        conn = psycopg2.connect(connect_str)
        # create a psycopg2 cursor that can execute queries
        cursor = conn.cursor()
        # create a new table with a single column called "name"
        #cursor.execute("""CREATE TABLE """ + country + """ (
        #            vacancy char(20000),
        #            link_to_a_vacancy char(20000),
        #            salary char(20000),
        #            company char(20000),
        #            short_description char(20000),
        #            location char(20000),
        #            date_from_creation char(10000),
        #            full_description char(30000),
        #            link_to_a_company char(20000)
        #            );""")
        with open(country + '.csv', encoding='utf-8') as file:
            order = ['Vacancy', 'Link to a vacancy', 'Salary', 'Company', 'Short description', 'Location',
                     'Date from creation', 'Full description', 'Link to a company']
            reader = csv.DictReader(file)
            number_of_lines = list(reader)
            country = country.replace('_', '')
            cursor.execute('DELETE FROM tables_' + country + ";")
            conn.commit()
            for line in number_of_lines:
                try:
                    print(line)
                    cursor.execute("INSERT INTO tables_" + country + "(vacancy, link_to_a_vacancy, salary, company, " +
                                                              "short_description, location, date_from_creation, " +
                                                              "full_description, link_to_a_company) values (" +
                                   "'" + (line['Vacancy']).replace("'", "") + "','" + (line['Link to a vacancy']).replace("'", "")
                                   + "','" + (line['Salary']).replace("'", "") + "','" + (line['Company']).replace("'", "")
                                   + "','" + (line['Short description']).replace("'", "") + "','" +
                                   (line['Location']).replace("'", "") + "','" + (line['Date from creation']).replace("'", "") + "','" +
                                   (line['Full description']).replace("'", "") + "','" + (line['Link to a company']).replace("'", "") + "')")
                    conn.commit()
                except Exception as e:
                    logging.error(
                        'Exception of type {!s} in creating_bd(country): {!s}'.format(type(ex).__name__,
                                                                                      str(ex)))
                    mes('Data base error in bd_jooble.py. See file logging_indeed.log for details')
        cursor.close()
        conn.close()
    except Exception as ex:
        logging.error(
            'Exception of type {!s} in creating_bd(country): {!s}'.format(type(ex).__name__,
                                                                          str(ex)))
        mes('Data base error in bd_jooble.py. See file logging_indeed.log for details')


def main():
    list_of_countries = ['India']
    list_of_countries = ['India', 'Philippines', 'Malaysia', 'Canada', 'New_Zealand', 'Australia', 'Nigeria',
                         'South_Africa', 'United_Kingdom', 'Ireland', 'Singapore', 'Pakistan', 'USA']

    for country in list_of_countries:
        country = 'Jooble_' + country
        creating_bd(country)


if __name__ == '__main__':
    main()

import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import quote
from selenium import webdriver

languages = {
    'Українська': 'uk',
    'Англійська': 'en',
    'Німецька': 'de',
    'Французька': 'fr',
    'Іспанська': 'es',
    'Італійська': 'it',
    'Японська': 'ja',
    'Китайська (спрощена)': 'zh-CN',
    'Португальська': 'pt',
    'Польська': 'pl'
}
while True:
    try:
        translate_lang = input('Введіть мову з якої хочете перекладати: ')
        language_value = languages[translate_lang]
        tranlate_language = quote(language_value, safe='')

        translater_lang = input('Введіть мову на яку хочете перекладати: ')
        languages_value = languages[translater_lang]
        translater_language = quote(languages_value, safe='')

        word = input('Напишіть слово яке хочете перекласти: ')
        words_output_value = quote(word, safe='')

        driver = webdriver.Chrome()
        driver.get(
                f'https://translate.google.com/?hl=uk&sl={tranlate_language}&tl={translater_language}&text={words_output_value}&op=translate')
        time.sleep(1)
        html = driver.page_source
        soup = BeautifulSoup(html, 'lxml')

        translate = soup.find('span', class_='ryNqvb').text
        print(translate)
        time.sleep(1)
        driver.quit()
        break
    except Exception:
        print('Така мова не знайдена')







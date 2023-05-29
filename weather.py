from bs4 import BeautifulSoup
import requests


def weather_check(city):
    headers = {
        'User-Agent': ''
    }

    res = requests.get(
        f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',
        headers=headers
    )

    soup = BeautifulSoup(res.text, 'html.parser')

    time = soup.select('#wob_dts')[0].getText().strip()
    precipitation = soup.select('#wob_dc')[0].getText().strip()
    weather = soup.select('#wob_tm')[0].getText().strip()

    print(f'''Day of the week and time: {time}
              Precipitation Information: {precipitation}
              Temperature: {weather}°C''')


if __name__ == '__main__':
    city_input = input('Enter name of the city: ')
    weather_check(f'{city_input} weather')
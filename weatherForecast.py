import requests
import json
import os
from bs4 import BeautifulSoup
from unicodedata import normalize


with open('states.json') as file:
    states = json.load(file)


def removeAccents(txt):
    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')


def getState():
    txt = input("State: ").replace(" ", "").lower()
    state = removeAccents(txt)
    return states[state] if state in states else None


def getCidade():
    txt = input("City: ").replace(" ", "").lower()
    return removeAccents(txt)


def printWeather(soup):
    title = soup.find_all("title")[0].get_text()
    if title != 'Previsão do Tempo para - - Tempo Agora':
        print('\n')
        print(title.replace("Previsão do Tempo para", "Weather Forecast for"))
        print("Temperature: ", soup.find_all("span")[5].get_text())
        print("Thermal sensation: ", soup.find_all("span")[7].get_text())
        print("Wind Speed: ", soup.find_all("span")[9].get_text())
        print("Pressure: ", soup.find_all("span")[11].get_text())
        print("Humidity: "+soup.find_all("span")[13].get_text())

    else:
        print("City not Found")


def weather():
    url_base = "http://www.tempoagora.com.br/previsao-do-tempo"
    while True:
        os.system('clear')

        print("Checking the weather forecast on tempoagora.com.br")
        print("Input the data")

        state = getState()

        if state:
            city = getCidade()
        else:
            print("State not Found\n\n\n")

        url = "{}/{}/{}/".format(url_base, state, city)
        site = requests.get(url)
        printWeather(BeautifulSoup(site.content, 'html.parser'))

        continuar = ''
        while continuar != 'y' and continuar != 'n':
            continuar = input("Do you wish to continue? [Y/n]:  ").lower()
        if continuar == 'n':
            return


if __name__ == '__main__':
    weather()

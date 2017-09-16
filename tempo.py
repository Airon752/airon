import requests
import json
import os
from bs4 import BeautifulSoup
from unicodedata import normalize


with open('states.json') as file:
    estados = json.load(file)


def removeAcentos(txt):
    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')


def getEstado():
    txt = input("Estado: ").replace(" ", "").lower()
    estado = removeAcentos(txt)
    return estados[estado] if estado in estados else None


def getCidade():
    txt = input("Cidade: ").replace(" ", "").lower()
    return removeAcentos(txt)


def printTempo(soup):
    title = soup.find_all("title")[0].get_text()
    if title != 'Previsão do Tempo para - - Tempo Agora':
        print('\n')
        print(title)
        print("Temperatura: ", soup.find_all("span")[5].get_text())
        print("Sesação: ", soup.find_all("span")[7].get_text())
        print("Velocidade do Vento: ", soup.find_all("span")[9].get_text())
        print("Pressão: ", soup.find_all("span")[11].get_text())
        print("Umidade: "+soup.find_all("span")[13].get_text())

    else:
        print("Cidade não encontrada")  # o estado já foi checado


def tempo():
    url_base = "http://www.tempoagora.com.br/previsao-do-tempo"
    while True:
        os.system('clear')

        print("Consultando a previsão do tempo em tempoagora.com.br")
        print("Entre com os dados para")

        estado = getEstado()

        if estado:
            cidade = getCidade()
        else:
            print("Estado não encontrado\n\n\n")

        url = "{}/{}/{}/".format(url_base, estado, cidade)
        site = requests.get(url)
        printTempo(BeautifulSoup(site.content, 'html.parser'))

        continuar = ''
        while continuar != 's' and continuar != 'n':
            continuar = input("Deseja continuar pesquisando? [S/n]:  ").lower()
        if continuar == 'n':
            return


if __name__ == '__main__':
    tempo()

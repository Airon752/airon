import requests
from bs4 import BeautifulSoup

def tempo():

    site = requests.get("http://www.tempoagora.com.br/previsao-do-tempo"+"/"+str(input("Digite a sigla do estado onde se localiza a cidade que você que consulta o tempo: "))+"/"+str(input("Digite o nome da cidade: "))+"/")
    soup = BeautifulSoup(site.content, 'html.parser')

    titulo = soup.find_all("title")[0].get_text()
    temperatura = soup.find_all("span")[5].get_text()
    sensacao = soup.find_all("span")[7].get_text()
    velocidade = soup.find_all("span")[9].get_text()
    pressao = soup.find_all("span")[11].get_text()
    umidade = soup.find_all("span")[13].get_text()

    print(titulo)
    print("Temperatura: "+temperatura)
    print("Sesação: "+sensacao)
    print("Velocidade do Vento: "+velocidade)
    print("Pressão: "+pressao)
    print("Umidade: "+umidade)

tempo()

print(str(input("pressione Enter para SAIR")))

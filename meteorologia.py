import requests

API_KEY = ""
cidade = input("Informe o nome da cidade: ")
link = f"https://api.openweathermap.org/data/2.5/forecast?q={cidade}&appid={API_KEY}&lang=pt_br"

#Capturando os dados da API em um arquivo json:
requisicao = requests.get(link)
requisicao_dic = requisicao.json()

#Contador utilizado para iterar entre os dados da lista:
contador = 0

#Utilizado para controle e validação/auditar.
rain_qtd = 0

alerta = 0

#For loop para popular e imprimir as variáveis
for i in requisicao_dic['list']:

    #Obtendo temperatura:
    temperatura = requisicao_dic['list'][contador]['main']['temp'] - 273.15
    temperatura_min = requisicao_dic['list'][contador]['main']['temp_min'] - 273.15
    temperatura_max = requisicao_dic['list'][contador]['main']['temp_max'] - 273.15

    # Obtendo Data/Hora da previsão:
    data_hora = requisicao_dic['list'][contador]['dt_txt']

    #Obtendo percentual de chance de chuva e testando, no caso de não haver previsão, será retornado 0:
    rain_percent = requisicao_dic['list'][contador]['pop'] * 100

    #Obtendo quantidade de chuva em mm e testando, no caso de não haver previsão, será retornado 0:
    try:
        rain = requisicao_dic['list'][contador]['rain']['3h']
        rain_qtd += 1
        if(rain > 2):
            alerta +=1
            print(f'ALERTA DE RISCO DE CALAMIDADE EM: {data_hora} ')

        #Imprimindo os resultados:
        # print(requisicao_dic)
        print(f'########################   PREVISÃO DE TEMPO PARA A DATA: {data_hora}   ########################')
        print('')
        print('Cidade: ', cidade)
        print(f'Hora: {data_hora}')
        print(f'Temperatura: {temperatura:.0f}°C')
        # print(f'Temperatura mínima: {temperatura_min:.0f}°C')
        # print(f'Temperatura máxima: {temperatura_max:.0f}°C')
        print(f'Percentual de chance de chuva: {rain_percent:.2f}%')
        print(f'Quantidade de chuva prevista: {rain:.2f}mm')
        print('')
        print('########################################################################################################')
        print('')
        contador += 1
        # print(contador)
        # print(i)

    except:
        print(f"Sem previsão de chuva para o dia: {data_hora}")
        # print(contador)
        rain = 0
        contador += 1

print(f'Quantidade de chuva: {rain_qtd}')
print(f'Alerta: {alerta}')
print(f'Contador: {contador}')
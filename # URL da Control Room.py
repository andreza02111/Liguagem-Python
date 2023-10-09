import requests

import pandas as pd

 

# URL da Control Room

control_room_url = "https://senac-1dev.my.automationanywhere.digital"

 

# Informações de autenticação

username = "powerbi"

password = "Senac@2023"

 

# Endpoint para obter o token de autenticação

auth_endpoint = f"{control_room_url}/v1/authentication"

 

# Parâmetros da solicitação

data = {

    "username": username,

    "password": password

}

 

# Realizar a solicitação POST para autenticar o usuário e obter um token JWT

response = requests.post(auth_endpoint, json=data)

 

# Verificar se a solicitação de autenticação foi bem-sucedida

if response.status_code == 200:

    # A resposta contém o token JWT

    auth_response = response.json()

    auth_token = auth_response.get("token")

    print(f"Token JWT de autenticação: {auth_token}")

 

    # URL da API do Bot Insight

    bot_insight_api_url = "https://senac-1dev.my.automationanywhere.digital/v2/botinsight"

 

    # Endpoint para obter dados de log de tarefa

    bot_run_endpoint = f"{bot_insight_api_url}/data/api/getbotrundata"

 

    # Cabeçalho de autenticação com o token JWT

    headers = {

        "X-Authorization": auth_token

    }

 

    # Realizar a solicitação GET sem parâmetros de consulta

    response = requests.get(bot_run_endpoint, headers=headers)

 

    # Verificar se a solicitação foi bem-sucedida

    if response.status_code == 200:

        # A resposta contém os dados de execução de bots em formato JSON

        bot_run_data = response.json()

 

        # Converter a coluna 'botRunDataList' em um DataFrame separado

        bot_run_df = pd.DataFrame(bot_run_data['botRunDataList'])

 

        # Exibir o DataFrame Pandas

        print(bot_run_df)

    else:

        print(f"Erro na solicitação de execução de bots: {response.status_code} - {response.text}")

else:

    print(f"Erro na solicitação de autenticação: {response.status_code} - {response.text}")
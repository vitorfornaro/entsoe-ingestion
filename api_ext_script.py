import requests
from datetime import datetime 

# Defina as constantes e parâmetros da API
API_KEY = '6b330f32-ab33-4f26-a38d-ce03e6fc5546'
BASE_URL = 'https://web-api.tp.entsoe.eu/api'
DOCUMENT_TYPE = 'A75'  # Código para geração de energia
PROCESS_TYPE = 'A16'  # Código para mercado em tempo real
IN_DOMAIN = '10YES-REE------0'  # Código para Espanha
PSR_TYPE = 'B16'  # Código para energia solar fotovoltaica

# Função para formatar a data no padrão esperado pela API
def format_date(date):
    return date.strftime('%Y%m%d%H%M')

# Datas de início e fim para o dia 1 de julho de 2024
start_date = datetime(2024, 7, 1, 0, 0)
end_date = datetime(2023, 8, 2, 0, 0)

# Parâmetros da requisição
params = {
    'securityToken': API_KEY,
    'documentType': DOCUMENT_TYPE,
    'processType': PROCESS_TYPE,
    'in_Domain': IN_DOMAIN,
    'outBiddingZone_Domain': IN_DOMAIN,
    'psrType': PSR_TYPE,
    'periodStart': format_date(start_date),
    'periodEnd': format_date(end_date)
}

# Realiza a requisição
response = requests.get(BASE_URL, params=params)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    print("Requisição bem-sucedida!")
    xml_data = response.content
    
    # Caminho para salvar o arquivo XML localmente
    file_path = "bucket/api_data.xml"
    
    # Salvando o XML localmente
    with open(file_path, "wb") as file:  # Usar "wb" para escrever bytes
        file.write(xml_data)
    
    print(f"Arquivo XML salvo em: {file_path}")
else:
    print(f"Erro: {response.status_code}")
    print(response.text)
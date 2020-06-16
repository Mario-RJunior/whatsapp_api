# Importar pacotes necessarios
from time import sleep
from whatsapp_api import WhatsApp
import pandas as pd

# Criando Dataframe com os contatos
df = pd.read_excel('Contatos.xlsx')

# Inicializar o whatsapp
wp = WhatsApp()

# Esperar que enter seja pressionado
input("Pressione enter apos escanear o QR Code")

# Lista de nomes ou nomeros de telefone a serem pesquisados
# IMPORTANTE: O nome deve ser nao ambiguo pois ele retornara o primeiro resultado
nomes_palavras_chaves = df['Contato']

# Lista com as mensagens a serem enviadas
mensagens = df['Mensagem']

# Loop para mandar mensagens para os clientes
for nome_pesquisar, mensagem in zip(nomes_palavras_chaves, mensagens):
    
    # Pesquisar pelo contato e esperar um pouco
    wp.search_contact(nome_pesquisar)
    sleep(2)
    
    # Enviar mensagem
    wp.send_message(mensagem)

# Esperar 10 segundos e fechar
sleep(10)
wp.driver.close()

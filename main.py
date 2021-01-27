import os 
import requests
os.system("color a")
os.system("cls")
print(f'''

  ██████╗ ██████╗  ███╗  ██╗███████╗██╗  ██╗██╗  ████████╗ █████╗      ██████╗███████╗██████╗ 
██╔════╝██╔═══██╗████╗  ██║██╔════╝██║   ██║██║  ╚══██╔══╝██╔══██╗    ██╔════╝██╔════╝██╔══██╗
██║     ██║   ██║██╔██╗ ██║███████╗██║   ██║██║     ██║   ███████║    ██║     █████╗  ██████╔╝
██║     ██║   ██║██║╚██╗██║╚════██║██║   ██║██║     ██║   ██╔══██║    ██║     ██╔══╝  ██╔═══╝ 
╚██████╗╚██████╔╝██║ ╚████║███████║╚██████╔╝███████╗██║   ██║  ██║    ╚██████╗███████╗██║     
 ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝  ╚═╝     ╚═════╝╚══════╝╚═╝     


######################################
####  Coded by: Iboy-Exploitado   #### 
######################################


   ''')

cep = input("Insira o CEP: ")
reques = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
json = reques.json()
print(f"""

CEP: {cep}
Logradouro: {json['logradouro']}
Complemento: {json['complemento']}
Bairro: {json['bairro']}
Localidade: {json['localidade']}
Estado: {json['uf']}
Ibge: {json['ibge']}
Gia: {json['gia']}
DDD: {json['ddd']}
Siafi: {json['siafi']}

      By: Iboy-Exploitado 
	""")



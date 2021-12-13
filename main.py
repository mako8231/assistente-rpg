from os import close
import discord
import os.path
import json

filename = "config.json"

#Verificar se o arquivo de configuração existe  
if not os.path.isfile(filename):
    print("O arquivo não existe, criando uma nova configuração na pasta do programa:")
    with open(filename, "w") as nf:
        token = input("Insira o token do seu bot")
        nf.write('{"token":"'+token+'"}')


#se o arquivo existe, leia 
file = open(filename, "r")
conf_str = file.readlines()
json_parsed = json.loads(conf_str[0])

cli = json_parsed["token"]


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

client = MyClient()
client.run(cli)    

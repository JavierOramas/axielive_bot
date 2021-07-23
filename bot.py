import os
from data import get_data
from pyrogram import Client, filters
from read_config import read_config


config_data = read_config('./config/config_bot.json')
app = Client(config_data['bot_user_name'], config_data['api_id'], config_data['api_hash'])

@app.on_message(filters.command('fee'))
def see_fee(client, message):
    message.reply(get_data())
    pass

@app.on_message(filters.command('help'))
@app.on_message(filters.command('start'))
def help(client, message):
    
    message.reply_text("""
                       Hola, Si deseas saber los costos de axie.live sin salir de telegram te voy a ser muy util
                        envia /fee para saber estos precios, tardo unos segundos en procesarlo, esto es culpa del tiempo decarga de la pagin>
                       """)
    pass

app.run()
import os

import discord
from dotenv import load_dotenv
from discord.ext import commands

import pika


############ CONEXION RABBITMQ ##############

HOST = os.environ['RABBITMQ_HOST']
print("rabbit:"+HOST)

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=HOST))
channelMQ = connection.channel()

#Creamos el exchange 'cartero' de tipo 'fanout'
channelMQ.exchange_declare(exchange='cartero', exchange_type='topic', durable=True)



#############################################

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content == 'pizza' or message.content == 'cerveza' or message.content == 'donuts':
        response = "!mmm..."+message.content+"!"
        await message.channel.send(response)

    await bot.process_commands(message)

@bot.command(name='birthday', help='Muestra la fecha de cumpleaño del miembro de la GUILD que se pasa en parámetro. Ejemplo: !birthday MatthieuVernier')
async def cumpleaños(ctx):
    message =  ctx.message.content
    print("send a new mesage to rabbitmq: "+message)
    channelMQ.basic_publish(exchange='cartero', routing_key="birthday", body=message)

@bot.command(name='add-birthday', help='Permite añadir el cumpleaño de un nuevo miembro de la GUILD que se pasa en parámetro. Ejemplo: !birthday MatthieuVernier 1985-02-13')
async def cumpleaños(ctx):
    message =  ctx.message.content
    print("send a new mesage to rabbitmq: "+message)
    channelMQ.basic_publish(exchange='cartero', routing_key="birthday", body=message)
    

bot.run(TOKEN)

client = discord.Client()
channel = client.get_channel(GUILD)
channel.send("test")



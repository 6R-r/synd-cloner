mytitle = "synd cloner"
from os import system
system("title "+mytitle)
import psutil
from pypresence import Presence
import time
import sys
client_id = 'account id'
import discord
import asyncio
import colorama
from colorama import Fore, init, Style
import serverside import stuff

syndrome = discord.Client()
os = platform.system()
if os == "Windows":
    system("cls")
else:
    system("clear")
    print(chr(27) + "[2J")
print(f"""{Fore.RED}

                                    ▄▀▀▀▀▄  ▄▀▀▄ ▀▀▄  ▄▀▀▄ ▀▄  ▄▀▀█▄▄   ▄▀▀▄▀▀▀▄  ▄▀▀▀▀▄   ▄▀▀▄ ▄▀▄  ▄▀▀█▄▄▄▄  
                                    █ █   ▐ █   ▀▄ ▄▀ █  █ █ █ █ ▄▀   █ █   █   █ █      █ █  █ ▀  █ ▐  ▄▀   ▐ 
                                       ▀▄   ▐     █   ▐  █  ▀█ ▐ █    █ ▐  █▀▀█▀  █      █ ▐  █    █   █▄▄▄▄▄  
                                    ▀▄   █        █     █   █    █    █  ▄▀    █  ▀▄    ▄▀   █    █    █    ▌  
                                     █▀▀▀       ▄▀    ▄▀   █    ▄▀▄▄▄▄▀ █     █     ▀▀▀▀   ▄▀   ▄▀    ▄▀▄▄▄▄   
                                     ▐          █     █    ▐   █     ▐  ▐     ▐            █    █     █    ▐   
                                                ▐     ▐        ▐                           ▐    ▐     ▐        
{Style.RESET_ALL}
                                                            {Fore.MAGENTA}the mastermind{Style.RESET_ALL}
        """)
token = input(f'token:\n ')
guild_s = input('guild id you want to copy:\n ')
guild = input('guild id where you want to copy:\n ')
input_guild_id = guild_s  # <- input guild id
output_guild_id = guild  # <- output guild id
token = token  # <-- your account token


print("  ")
print("  ")

@syndrome.event
async def on_ready():
    extrem_map = {}
    print(f"logged in as: {client.user}")
    print("cloning the server...")
    guild_from = client.get_guild(int(input_guild_id))
    guild_to = client.get_guild(int(output_guild_id))
    await stuff.guild_edit(guild_to, guild_from)
    await stuff.roles_delete(guild_to)
    await stuff.channels_delete(guild_to)
    await stuff.roles_create(guild_to, guild_from)
    await stuff.categories_create(guild_to, guild_from)
    await stuff.channels_create(guild_to, guild_from)
    print(f"""{Fore.GREEN}


                                            ▄▀▀█▄▄   ▄▀▀█▀▄    ▄▀▀█▄▄       ▄▀▀█▀▄    ▄▀▀▀█▀▀▄ 
                                           █ ▄▀   █ █   █  █  █ ▄▀   █     █   █  █  █    █  ▐ 
                                           ▐ █    █ ▐   █  ▐  ▐ █    █     ▐   █  ▐  ▐   █     
                                             █    █     █       █    █         █        █      
                                            ▀▄▄▄▄▀  ▄▀▀▀▀▀▄   ▄▀▄▄▄▄▀      ▄▀▀▀▀▀▄   ▄▀       
                                            █     ▐  █       █ █     ▐      █       █ █         
                                            ▐        ▐       ▐ ▐            ▐       ▐ ▐  

    {Style.RESET_ALL}""")
    await asyncio.sleep(5)


syndrome.run(token, bot=False)

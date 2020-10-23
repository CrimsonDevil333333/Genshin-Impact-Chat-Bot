import discord
from discord.ext import commands
import random
from random import randrange
import json
import asyncio
import praw
import datetime
import threading
from difflib import get_close_matches

""" Predefined lists :- """
global character_list
character_list = ["diluc","fischl","keqing","klee","qiqi","venti","jean","mona","xiao","razor","xiangling","barbara","bennett","chongyun","xingqiu","beidou","Kaeya","lisa","ningguang","noelle","sucrose","amber"]


""" Some imp functions :-"""
def closeMatches(patterns, word): 
    return get_close_matches(word, patterns)
    
global character




""" Token/Prefex reader :- """
def read_token():
    with open("token.txt","r") as f:
        lines =f.readlines()
        return lines[0].strip()
token = read_token()
def read_prefex():
    with open("prefex.txt","r") as f:
        lines = f.readlines()
        return lines[0].strip()
prefex = read_prefex()
bot = commands.Bot(command_prefix=prefex , case_insensitive=True)
#bot.remove_command("help")

""" Bot events :- on bot ready """
@bot.event
async def on_ready():
    print("Logged in as: " + bot.user.name + "\n")
    global character
    
    character = "database/characters.json"
    with open(character, "r") as read_file:
        character = json.load(read_file)
    
    return await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching , name=f"Prefix is '{prefex}'(.help)"))


@bot.command(pass_context=True, aliases=["list","tl"])
async def tier(ctx, * , reason=None):
    if reason == None:
        await ctx.send("https://media.discordapp.net/attachments/769078033901682698/769078807973462026/unknown.png?width=716&height=702")
    elif reason == "DPS" or reason == "Dps" or reason == "dps":
        await ctx.send("https://media.discordapp.net/attachments/769078033901682698/769078140873080882/unknown.png")
    elif reason == "Support" or reason == "support" or reason== "SUPPORT":
        await ctx.send("https://media.discordapp.net/attachments/769078033901682698/769078252290965504/unknown.png?width=706&height=702")
    elif reason == "healer" or reason == "Healer" or reason == "HEALER":
        await ctx.send("https://media.discordapp.net/attachments/769078033901682698/769079656640020510/unknown.png")
    else :
        await ctx.send("Enter valid reason like dps,support or healer.")

@bot.command(pass_context=True, aliases=["constellation","c","constel","con"])
async def constellations(ctx, * , reason=None):
    if reason == None:
        await ctx.send("https://media.discordapp.net/attachments/769048747123408928/769060854443671592/unknown.png")
    else:
        try:
            global character
            global character_list

            name = closeMatches(character_list,reason)
            toon = character[name[0]]
            constellation = toon["constellation"]
            await ctx.send(constellation)
        except:
            await ctx.send("Please type correct name if ya wan't to see constellations for any particular character...")


@bot.command(pass_context=True, aliases=['toon','build',"builds", "t","b"])
async def character(ctx, *, reason=None):
    if reason == None:
        await ctx.send("https://media.discordapp.net/attachments/769048747123408928/769060854443671592/unknown.png")
    else:
        try:
            global character
            global character_list
            

            name = closeMatches(character_list,reason)
            toon = character[name[0]]
            icon_png = toon["png"]
            typo = toon["type"]
            weapon = toon["weapons"]
            siteLink = toon["site link"]
            star = toon["star"]
            #constellation = toon["constellation"]
            uses = toon["uses"]
            overview = toon["overview"]
            uses = uses.split(",")
            no_of_uses = len(uses)
            if no_of_uses == 1:
                bestWeapon1 = toon[f"best weapon {uses[0].lower()}"]
                artifact1 = toon[f"artifacts {uses[0].lower()}"]
                bestWeapon2 = None
                artifact2 = None
                
            elif no_of_uses == 2:
                bestWeapon1 = toon[f"best weapon {uses[0].lower()}"]
                artifact1 = toon[f"artifacts {uses[0].lower()}"]
                bestWeapon2 = toon[f"best weapon {uses[1].lower()}"]
                artifact2 = toon[f"artifacts {uses[1].lower()}"]
                
            elif no_of_uses == 3:
                bestWeapon1 = toon[f"best weapon {uses[0].lower()}"]
                artifact1 = toon[f"artifacts {uses[0].lower()}"]
                bestWeapon2 = toon[f"best weapon {uses[1].lower()}"]
                artifact2 = toon[f"artifacts {uses[1].lower()}"]
                """bestWeapon3 = toon[f"best weapon {uses[2].lower()}"]
                artifact3 = toon[f"artifacts {uses[2].lower()}"]"""

            embed = discord.Embed(
                title= f"{name[0]}",
                url= siteLink ,
                description= overview,
                color=0x55B80B)
            embed.set_thumbnail(url= icon_png)
            embed.add_field(name="Type", value=typo, inline=True)
            embed.add_field(name="Weapon Type", value=weapon, inline=True)
            embed.add_field(name="Uses", value=uses, inline=True)
            
            if no_of_uses == 1:
                embed.add_field(name=f"{uses[0]} Build", value=f"Weapon :- {bestWeapon1}\nArtifact :- {artifact1}", inline=False)
            elif no_of_uses == 2:
                embed.add_field(name=f"{uses[0]} Build", value=f"Weapon :- {bestWeapon1}\nArtifact :- {artifact1}", inline=False)
                embed.add_field(name=f"{uses[1]} Build", value=f"Weapon :- {bestWeapon2}\nArtifact :- {artifact2}", inline=False)
#  3 isn't added yet coz no need so far .....
            await ctx.send(embed=embed)
        except:
            await ctx.send("Please type correct name")
















bot.run(token)
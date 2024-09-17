import discord
from discord.ext import commands

# Crée un bot avec un préfixe de commande, ici "!"
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Événement déclenché quand le bot est prêt
@bot.event
async def on_ready():
    print(f'Le bot est connecté en tant que {bot.user}')

# Commande pour supprimer tous les messages dans un channel
@bot.command(name='clearall')
@commands.has_permissions(administrator=True)
async def clearall(ctx):
    await ctx.channel.purge()  # Supprime tous les messages dans le channel
    await ctx.send("Tous les messages ont été supprimés.", delete_after=5)  # Message temporaire de confirmation

# Remplace TON_TOKEN par le token de ton bot
bot.run('TOKEN')

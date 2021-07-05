import discord
import os

TOKEN = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
  print(f'{client.user} has connected to Discord!')

# Media channel system
@client.event
async def on_message(message):
  if message.author == client.user: # dont respond to self
    return

  if message.channel.id == 850810760703639643:
    if "http" in message.content or message.attachments:
      await message.add_reaction('<a:tickgreen:850803068110766120>')
      await message.add_reaction('<a:tickred:850803121491017728>')
    else:
      await message.delete()

# Reaction roles
@client.event
async def on_raw_reaction_add(payload):
  message_id = payload.message_id
  if message_id == 851274652688056361: # Reaction role message id
    guild_id = payload.guild_id
    guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

    if payload.emoji.name == 'redtick': # Name of emoji you react with
      role = discord.utils.get(guild.roles, name='red') # Name of the role you get
    elif payload.emoji.name == 'greentick':
      role = discord.utils.get(guild.roles, name='green')
    else:
      role = discord.utils.get(guild.roles, name=payload.emoji.name) # If reacted emoji is same as name of role, it'll give them that role

    if role is not None:
      member = payload.member
      if member is not None:
        await member.add_roles(role)
        print("Done.")
      else:
        print("Member not found.")
    else:
      print("Role not found.")
       
@client.event
async def on_raw_reaction_remove(payload):
  message_id = payload.message_id
  if message_id == 851274652688056361: # Reaction role message id
    guild_id = payload.guild_id
    guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)

    if payload.emoji.name == 'redtick': # Name of emoji you react with
      role = discord.utils.get(guild.roles, name='red') # Name of the role you get
    elif payload.emoji.name == 'greentick':
      role = discord.utils.get(guild.roles, name='green')
    else:
      role = discord.utils.get(guild.roles, name=payload.emoji.name) # If reacted emoji is same as name of role, it'll give them that role

    if role is not None:
      member = await(await client.fetch_guild(payload.guild_id)).fetch_member(payload.user_id)
      if member is not None:
        await member.remove_roles(role)
        print("Done.")
      else:
        print("Member not found.")
    else:
      print("Role not found.")

client.run(TOKEN)
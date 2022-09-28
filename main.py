import discord
import os
from keep_alive import keep_alive


Routine = discord.Client()

@Routine.event
async def on_ready() 
      print('Hi.. I am in')

@Routine.event 
async def on_message(message) 
  if message.author == Routine.user 
    return

  if message.content.startswith('$saturday') 
    await message.channel.send('1. EEE theory 1050am to 1140am')
    await message.channel.send('2. Compiler Theory 1140am to 1230pm')
    await message.channel.send('3. Internet programming 250pm to 340pm')
  
  if message.content.startswith('$sunday') 
    await message.channel.send('1. Microcontroller Lab 1050am to 1140am')
    await message.channel.send('2. Computer Architecture 1140am to 1230pm')
    await message.channel.send('3. URED-3503 200pm to 250pm')
    await message.channel.send('4. EEE Lab 250pm to 340pm')

  if message.content.startswith('$monday') 
    await message.channel.send('1. Internet programming 1050am to 1140am')
    await message.channel.send('2. System analysis 1140am to 1230pm')
    await message.channel.send('3. Microcontroller theory 200pm to 250pm')
    await message.channel.send('4. MDP 250pm to 340pm')
  
  if message.content.startswith('$tuesday') 
    await message.channel.send('1. Microcontroller theory 1050am to 1140am')
    await message.channel.send('2. Computer Architecture 1140am to 1230pm')
    await message.channel.send('3. URED-3503 200pm to 250pm')
    await message.channel.send('4. Compiler Lab 250pm to 340pm')
    
  if message.content.startswith('$wednesday') 
    await message.channel.send('1. System analysis 1050am to 1140am')
    await message.channel.send('2. Compiler 1140am to 1230pm')
    await message.channel.send('3. EEE theory 250pm to 340pm')

  if message.content.startswith('$thursday') 
    await message.channel.send('Eto class tokas ka lehafora koille nije nije korgoi')
    await message.channel.send('Sobor gor kon sir e extra class de saiya thak')

  if message.content.startswith('$friday') 
    await message.channel.send('Jumar din ekkana khema dee')



keep_alive()
Routine.run(os.getenv('TOMIEKTAVODAI')) #Not the original

# github.com/wacutils/wacutils
# 2018

import discord
import sys

prepend = "%"

client = discord.Client()
token = '<INSERT TOKEN HERE>'

def stringIsNum(string):
	for char in string:
		if char not in "0123456789":
			return False
	return True

@client.event
async def on_message(message):
	# We do not want the bot to reply to itself
	if message.author == client.user:
		return

	content = message.content # Could possibly be faster

	if content == prepend+"status":
		verInfo = sys.version_info
		versionStr = str(info[0])+"."+str(info[1])+"."+str(info[2]) # format: major.minor.micro
		await client.send_message(message.channel, "Online, running on Python " + versionStr)

	elif content == prepend+"help":
		msg = "Commands (prepended with " + prepend + "):\n\thelp - Displays this page\n\tstatus - Tells you the Python version\n\tbinary [number] - Gives you binary representation of a base 10 number"
		await client.send_message(message.channel, msg)

	elif content.startswith(prepend+"binary "):
		argument = content.split(' ')[1]
		if !stringIsNum(argument):
			await client.send_message(message.channel, "Usage: " + prepend + "binary [number]")
			return
		await client.send_message(message.channel, "Binary value of " + argument + " is " + binary(int(argument)))


@client.event
async def on_ready():
	print("Logged in as " + client.user.name)
	print("Client ID: " + client.user.id)

client.run(token)

# python3.6 wacutils_bot.py

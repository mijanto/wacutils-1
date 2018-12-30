# github.com/wacutils/wacutils
# 2018

import discord
import socket
import sys # For getting python version
import os

prepend = '%'

client = discord.Client()
token = "<INSERT TOKEN HERE>"

def binary(n):
	return bin(n)[2:] # Slice off the "0b" part bin leaves behind

def string_is_num(string):
	for char in string:
		if char not in "0123456789":
			return False
	return True

def is_valid_ip(ip):
	try:
		socket.inet_aton(ip) # Source: http://www.cs.cmu.edu/afs/cs/academic/class/15213-f00/unpv12e/libfree/inet_aton.c
		return True
	except socket.error:
		return False

def ip_up(ip):
	# Ping only once, only allow ipv4, and timeout after 1 second.
	return os.system("ping -c 1 -4 -W 1 " + ip)==0

@client.event
async def on_message(message):
	# We do not want the bot to reply to itself
	if message.author == client.user:
		return

	content = message.content
	if content[0] is not prepend:
		return

	# Ignore commands that are too long, these are likely not to be real commands
	if len(content) > 50:
		await client.send_message(message.channel, "Length of command exceeds max length of 50 (" + str(len(content)) + ")")
		return

	args = content.split(' ')

	if content == prepend+"status":
		verInfo = sys.version_info
		versionStr = str(verInfo[0])+"."+str(verInfo[1])+"."+str(verInfo[2]) # format: major.minor.micro
		await client.send_message(message.channel, "Online, running on Python " + versionStr)

	elif content == prepend+"help":
		msg = "Commands (prepended with " + prepend + "):\n\thelp - Displays this page\n\tstatus - Tells you the Python version\n\tbinary [number] - Gives you binary representation of a base 10 number\n\tping [ip] - pings ip, and gives whether its up or not"
		await client.send_message(message.channel, msg)

	elif content.startswith(prepend+"ping "):
		if not is_valid_ip(args[1]):
			await client.send_message(message.channel, args[1] + " is not a valid IP address")
			return

		await client.send_message(message.channel, "IP " + args[1] + " is " + ("up" if ip_up(args[1]) else "down"))

	elif content.startswith(prepend+"binary "):
		if not string_is_num(args[1]):
			await client.send_message(message.channel, "Usage: " + prepend + "binary [number]")
			return
		await client.send_message(message.channel, "Binary value of " + args[1] + " is " + binary(int(args[1])))


@client.event
async def on_ready():
	print("Logged in as " + client.user.name)
	print("Client ID: " + client.user.id)

client.run(token)

# python3.6 wacutils_bot.py

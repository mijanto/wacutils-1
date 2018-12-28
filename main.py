import discord
import socket
import os

client = discord.Client()
token = '<INSERT TOKEN HERE>'

#operationToRuletable="and1xor6or7nor8nand14"
operationToRuletable=[["and",1],["xor",6],["or",7],["nor",8],["nand",14]]

def is_valid_ip_address(ip):
	try:
		socket.inet_aton(ip)
		return True
	except socket.error:
		return False

def ip_up(ip):
	return os.system("ping -c 1 " + ip)==0
	
def operationBit(a,b,rule):
	return bin(rule)[(2*a+b)]

def operationNumber(a,b,rule):
	binary1 = bin(a)
	binary2 = bin(b)

#	while len(binary1) > len(binary2):
#		binary2 = '0' + binary2
	if len(binary1) > len(binary2):
		binary2 = ('0'*(len(binary1)-len(binary2))) + binary2
	elif len(binary1) < len(binary2):
		binary1 = ('0'*(len(binary2)-len(binary1))) + binary1

	out=""
	for b1, b2 in zip(a,b):
		out += operationBit(bit,)
		
# Same as operationNumber(), except the rule can be a string like "and" or "xor", and they will map to their corresponding ruletables (0001 and 0110 for "and" and "xor")
# Maps stored in operationToRuletable list
def operationWithMap(a,b,rule):
	if type(rule) is str:
		return 

@client.event
async def on_message(message):
	# we do not want the bot to reply to itself
	if message.author == client.user:
		return

	if message.content.startswith('&hello'):
		msg = 'Hello {0.author.mention}'.format(message)
		await client.send_message(message.channel, msg)

	elif message.content.startswith("%ping "):
		argument = message.content.split(" ")[1]
		
		if not is_valid_ip_address(argument):
			await client.send_message(message.channel, argument + " is not a valid IP address")
			return
		
		if ip_up(argument):
			await client.send_message(message.channel, "IP " + argument + " is up")
		else:
			await client.send_message(message.channel, "IP " + argument + " is down")

	elif message.content.startswith('&status'):
		msg = 'Im fine, thank you. How are you? {0.author.mention}'.format(message)
		await client.send_message(message.channel, msg)
        
	elif message.content.startswith('&develop'):
		msg = 'This is our github page where you can help us developing the bot: https://github.com/wacutils/wacutils. We also  have a server, you can join us on: https://discord.gg/aGkx98q '.format(message)
		await client.send_message(message.channel, msg)

	elif message.content.startswith('&wavetome'):
		msg = ':wave: {0.author.mention}'.format(message)
		await client.send_message(message.channel, msg)

	elif message.content.startswith('&commands'):
		msg = 'Here is what {0.author.mention} wanted:\n\n&hello\n&status\n&wawetome'.format(message)
		await client.send_message(message.channel, msg)
	

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

client.run(token)

# python3.6 wacutils_bot.py

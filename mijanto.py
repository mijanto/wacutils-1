# just put this between commands and reactions
    if message.content.startswith('&wawetome'):
        msg = ':wawe: {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
        return

    if message.content.startswith('&commands'):
        msg = 'Here is what {0.author.mention} wanted:\n\n&hello\n&status\n&wawetome'.format(message)
        await client.send_message(message.channel, msg)
        return 

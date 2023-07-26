import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    # Ignore the message made by bot itself
    if message.author == client.user:
        return

    if message.content.startswith("hello"):
        await message.channel.send("Hello!")


client.run("MTEzMzgxMjQ4NDk1MjgyNTg4Nw.GUvYZL.8KZiDg2sEAIeZ_8N8wzFboSXCm41NAYGzKMK6s")

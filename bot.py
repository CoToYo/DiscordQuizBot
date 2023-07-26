import discord
from dotenv import load_dotenv
import os
import requests
import json
import asyncio

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


def get_question():
    qs = ""
    id = 1
    answer = 0
    response = requests.get("http://127.0.0.1:8000/api/random")
    json_data = json.loads(response.text)
    qs += "Question: \n"
    qs += json_data[0]["title"] + "\n"

    for item in json_data[0]["answer"]:
        qs += str(id) + ". " + item["answer"] + "\n"

        if item["is_correct"]:
            answer = id

        id += 1

    return (qs, answer)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    # Ignore the message made by bot itself
    if message.author == client.user:
        return

    if message.content.startswith("$question"):
        qs, answer = get_question()
        await message.channel.send(qs)

        def check(m):
            return m.author == message.author and m.content.isdigit()

        try:
            guess = await client.wait_for("message", check=check, timeout=10.0)
        except asyncio.TimeoutError:
            return await message.channel.send("Sorry, you took too long")

        if int(guess.content) == answer:
            await message.channel.send("You are right!")
        else:
            await message.channel.send("Oops. That is not right")


client.run(os.getenv("Token"))

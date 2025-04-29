from discord import Intents
from discord.ext import commands
from ollama import chat
from ollama import ChatResponse
import time

BOT_TOKEN = "InsertYourTokenHere"
intents = Intents.all()
bot = commands.Bot(command_prefix="/", intents=intents)

# Models: deepseek-r1, Qwen2:0.5B, sroecker/sauerkrautlm-7b-hero, ...
model = 'sroecker/sauerkrautlm-7b-hero'


@bot.event
async def on_message(message):
    if not message.content.startswith("Bot: "):
        try:
            response: ChatResponse = chat(model=model, messages=[
                {
                    'role': 'user',
                    'content': message.content + "Your final response must be shorter than 2000 characters. "
                                                 "Answer in the language of the user input.",
                },
            ])
            if model == 'deepseek-r1':
                result = response.message.content.split("</think>")[1]
            elif model == 'sroecker/sauerkrautlm-7b-hero':
                result = response.message.content.replace("</s>", "")
            else:
                result = response.message.content
            print(result)
            await message.channel.send(("Bot: " + result).replace("\n\n", "\n")[0:1999])  # Max length protection

        except:
            await message.channel.send("Bot: Internal server error")


bot.run(BOT_TOKEN)

import discord
from discord.ext import commands
import os
import asyncio

# Create intents instance and enable necessary intents
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

# Create the bot instance with the command prefix and the necessary intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Define phrases, their corresponding role IDs, and custom messages
role_phrases = {
    "silence": (1293152696488165396, "The word 'Silence' echoes through the hallway. The house starts rumbling and the ground shakes. The door infront of you opens revealing another dark hallway."),
    "give me testing role": (1293158853784899584, "You now have the Testing Role!"),
    "jackyolanty": (1300421318503829547, "As you reach for the hidden pumpkin, a chill runs down your spine. The air thickens, and whispers echo around you, warning of the spirits that linger close. The pumpkin’s grin seems to widen as you lift it, revealing a rolled parchment tucked away inside. With each word you read, you feel the shadows draw nearer, urging you onward to uncover the next hidden secret of this haunted night."),
    "fear": (1300477535708254218, "As the word 'fear' comes through your mouth sending shivers down your spine, u hear some cackling noises from another room."),
    "spookyscaryskeletons": (1301180103564333106, "All the bones in the room start gathering, forming into 5 skeletons which start dancing??? (heheh). The door behind you opens into another room...Hmmm this one looks more...*royal*."),
    "thequeenofthedamned": (1301214352355098634, "You speak her title....and thus she awakens...BLOOD FILLS UP EVERYWHERE.....YOU START TO DROWN UNDER ALL THE BLOOD AS YOU HEAR A DEMONIC YET FEMININE VOICE LAUGHING.......***YOU ARE DEAD***."),
    "ecclesiastes": (1301217713099640975, "As you say the holy name a serene power starts surrounding you....the powerful aura condenses into your hands turning into a scroll.),
    "jehovah": (1301222698634055780, "The true name of god fills up your holy karma...you soul starts starts to ascend away from limbo into the paradise.")
}

# Define the required roles for each phrase
required_roles = {
    "silence": 1293138788494872606,  # Replace with the required role ID for "silence"
    "give me testing role": 1293136619993432128,  # Required role for "give me testing role"
    "jackyolanty": 1293152696488165396, #rq role for "jackyolanty"
    "fear": 1300421318503829547 #rg role for "fear"
    "spookyscaryskeletons": 1300477535708254218 #rq role for "spookyscaryskeletons"
    "thequeenofthedamned": 1301180103564333106 #rq role for "thequeenofthedamned"
    "ecclesiastes": 1301214352355098634 #rq role for "ecclesiastes"
    "jehovah": 1301217713099640975 #rq role for "jehovah"
}
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello, {ctx.author.mention}!')

# Listen for specific phrases in chat and assign roles
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return  # Ignore the bot's own messages

    for phrase, (role_id, custom_message) in role_phrases.items():
        if phrase in message.content.lower():
            try:
                # Check for the required role
                required_role_id = required_roles.get(phrase)
                if required_role_id:
                    required_role = discord.utils.get(message.guild.roles, id=required_role_id)
                    if required_role not in message.author.roles:
                        return  # Stop further processing if the user lacks the required role

                # Assign the new role
                role = discord.utils.get(message.guild.roles, id=role_id)
                if role:
                    await message.author.add_roles(role)
                    await message.channel.send(f"{message.author.mention}, {custom_message}")
                else:
                    await message.channel.send("Role not found!")
            except discord.Forbidden:
                await message.channel.send("I do not have permission to assign that role.")
            except discord.HTTPException as e:
                await message.channel.send(f"An error occurred: {e}")
            break  # Exit the loop after processing the message

    await bot.process_commands(message)

# Run the bot
if __name__ == "__main__":
    bot.run('MTI5MzE0NzQxMDExMzIzMjk0Nw.GiboDV.f3VWsFrRG-kfTKcyqoFHs9M_yFah95ngt6J73o')

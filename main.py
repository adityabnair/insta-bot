import discord
import instaloader
import os
import shutil
from discord.ext import commands

from dotenv import load_dotenv
load_dotenv()
# Obtain the token from the .env file
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

# Create the bot with no command prefix (triggered by tagging)
intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix='', intents=intents)

# Initialize Instaloader
L = instaloader.Instaloader()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')

@bot.event
async def on_message(message):
    # Check if the bot is tagged in the message
    if bot.user.mentioned_in(message):
        # Extract the URL from the message content
        content = message.content.split()
        url = None
        for word in content:
            if "instagram.com" in word:
                url = word
                break
        
        if url:
            # Extract the shortcode from the URL
            shortcode = url.split("/")[-2]
            
            try:
                # Download the Instagram post
                post = instaloader.Post.from_shortcode(L.context, shortcode)
                download_directory = 'downloads'
                
                # Ensure the download directory exists
                if not os.path.exists(download_directory):
                    os.makedirs(download_directory)
                    print(f"Created download directory: {download_directory}")
                
                # Download the post
                print(f"Starting download for shortcode: {shortcode}")
                L.download_post(post, target=download_directory)
                
                # Debug: List all files in the download directory
                print(f"Files in download directory: {os.listdir(download_directory)}")
                
                # Ensure there are files in the download directory
                files_in_directory = os.listdir(download_directory)
                if files_in_directory:
                    files_sent = False
                    for file_name in files_in_directory:
                        file_path = os.path.join(download_directory, file_name)
                        print(f"Found file: {file_path}")
                        if file_name.endswith(('.mp4', '.jpg')):
                            try:
                                # Send the video or image file to the Discord channel
                                await message.channel.send(file=discord.File(file_path))
                                files_sent = True
                            except Exception as e:
                                # Log file send errors
                                print(f"Failed to send file: {file_path}, Error: {e}")
                    
                    # Send the caption to Discord
                    if post.caption:
                        await message.channel.send(f"Caption: {post.caption}")
                    
                    # Clean up the download directory if files were sent
                    if files_sent:
                        # Remove all files in the downloads directory
                        for file_name in files_in_directory:
                            file_path = os.path.join(download_directory, file_name)
                            if os.path.isfile(file_path):
                                os.remove(file_path)
                        # Optionally remove the downloads directory if empty
                        if not os.listdir(download_directory):
                            os.rmdir(download_directory)
                    else:
                        await message.channel.send("No downloadable media found in the post.")
                else:
                    await message.channel.send("No files found in the download directory.")
            
            except Exception as e:
                # Debug: Print the exception message
                print(f"Exception occurred: {e}")
                # Send an error message if something goes wrong
                await message.channel.send(f'Failed to download post: {e}')
        else:
            await message.channel.send('Please provide a valid Instagram link.')

# Run the bot
bot.run(TOKEN)

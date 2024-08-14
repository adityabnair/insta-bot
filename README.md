# insta-bot
This is a simple setup for a locally running private discord bot that can download and display Instagram pictures, posts and videos, provided the bot has the link tagged alongside it. 
It runs using the python instaloader library to download the Instagram content (by extracting the shortcode from the provided hyperlink) and sends the files, thumbnails along with captions (if any) to the discord channel where it was tagged. It cleans up the downloads by deleting the local directory after it has succcessfully managed to send the files. It also prints error messages dealing with why the file wasn't downloaded in case of specific exceptions such as no files present, no media found in post, or the link being invalid; thus dealing well with error handling. 

_Note : Do not make too many requests in a fixed time interval using the bot as that could lead to Instagram blocking the IP address temporarily from accessing content._

## Screenshots

![image](https://github.com/user-attachments/assets/4606d7e8-a642-4f53-953e-778c31821bc2)
![image](https://github.com/user-attachments/assets/f5a1ad29-a1f4-4da7-b028-64155b0bf95b)
![image](https://github.com/user-attachments/assets/7ce8afde-ec45-488f-b2a7-d6241edd41ff)


## Main Prerequisites

1. At least Python 3.10
2. Access to your Discord's bot's token

### Running

1. Use pipenv to install python libraries from requirements.txt (a virtual environemnt is always recommended)
2. Setup the discord bot environment on the [Discord developer portal](https://discord.com/developers/applications)
3. Create a new application and add a bot
4. Go to the Bot section and customise the bot settings including the name
5. Add the environment variable in a .env file to hold the Discord bot's token (as copied from the bot menu)
6. Under the OAuth2 settings, scroll down to the URL generator and select the "bot" scope. Proceed to add all the necessary permissions.
7. Copy the URl and paste it on a browser to invite the bot to a discord server. (these settings are only for private usage)
8. Run main.py of the script
9. Tag the bot using @ and include the link

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

import os
import re
import sys
import json
import time
import asyncio
import requests
import subprocess

import core as helper
from utils import progress_bar
from vars import API_ID, API_HASH, BOT_TOKEN
from aiohttp import ClientSession
from pyromod import listen
from subprocess import getstatusoutput

from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram.errors.exceptions.bad_request_400 import StickerEmojiInvalid
from pyrogram.types.messages_and_media import message

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

bot = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN)

authorized_users = [5850397219, 7856557198]

help_button_keyboard = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("Help", callback_data="help")],
    ]
)

# Define the start command handler
@bot.on_message(filters.command("start"))
async def start(client: Client, msg: Message):
    user = await client.get_me()
    
    start_message = await client.send_message(
        msg.chat.id,
        "Initializing Uploader bot... 🤖\n\n"
        "Progress: [🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍] 0%\n\n"
    )

    await asyncio.sleep(1)
    await start_message.edit_text(
        "Loading features... ⏳\n\n"
        "Progress: [🩵🩵🩵🤍🤍🤍🤍🤍🤍🤍] 25%\n\n"
    )
    
    await asyncio.sleep(1)
    await start_message.edit_text(
        "This may take a moment, sit back and relax! 😊\n\n"
        "Progress: [🩵🩵🩵🩵🩵🤍🤍🤍🤍🤍] 50%\n\n"
    )

    await asyncio.sleep(1)
    await start_message.edit_text(
        "Checking subscription status... 🔍\n\n"
        "Progress: [🩵🩵🩵🩵🩵🩵🩵🤍🤍🤍] 75%\n\n"
    )

    await asyncio.sleep(1)
    if msg.from_user.id in authorized_users:
        await start_message.edit_text(
            "Great! You are a 𝗣𝗥𝗘𝗠𝗜𝗨𝗠 member! 🌟 Press `/help` in order to use me properly\n\n",
            reply_markup=help_button_keyboard
        )
    else:
        await asyncio.sleep(2)
        await start_message.edit_text(
            "You are currently using the 𝗙𝗥𝗘𝗘 version. 🆓\n\n"
            "I'm here to make your life easier by downloading videos from your **.txt** file 📄 and uploading them directly to Telegram!\n\n"
            "Want to get started? your id \n\n💬 Contact @Course_diploma_bot to get the 𝗦𝗨𝗕𝗦𝗖𝗥𝗜𝗣𝗧𝗜𝗢𝗡 🎫 and unlock the full potential of your new bot! 🔓"
        )

# Add this at the end to run the bot







@bot.on_message(filters.command("stop"))
async def restart_handler(_, m):
    await m.reply_text("**Stopped**🚦", True)
    os.execl(sys.executable, sys.executable, *sys.argv)



@bot.on_message(filters.command(["drm"]))
async def upload(bot: Client, m: Message):
    editable = await m.reply_text('➠ 𝐒𝐞𝐧𝐝 𝐌𝐞 𝐘𝐨𝐮𝐫 𝐓𝐗𝐓 𝐅𝐢𝐥𝐞 𝐢𝐧 𝐀 𝐏𝐫𝐨𝐩𝐞𝐫 𝐖𝐚𝐲 **\n\n**├── Bot Made By : **『 🅹🅰️🅸 🆂🅷🆁🅸 🆁🅰️🅼 ⚡️ 🧑‍💻』**')
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)

    path = f"./downloads/{m.chat.id}"

    try:
       with open(x, "r") as f:
           content = f.read()
       content = content.split("\n")
       links = []
       for i in content:
           links.append(i.split("://", 1))
       os.remove(x)
            # print(len(links)
    except:
           await m.reply_text("**Invalid file input.**")
           os.remove(x)
           return
    
   
    await editable.edit(f"**Total Number of 🔗 Links found are** **{len(links)}**\n**├─ 📽️ Video Links :**\n**├─ 📑 PDF Links :**\n**├─ 🖼️ Image Links :**\n**├─ 🔗 Other Links:**\n\n**Send From where You want to 📩 Download\n**Initial is  :** **1**\n\n **├── Bot Made By : **『 🅹🅰️🅸 🆂🅷🆁🅸 🆁🅰️🅼 ⚡️ 🧑‍💻』**")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text = input0.text
    await input0.delete(True)

    await editable.edit("**Now Please Send Me Your Batch Name**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text0 = input1.text
    await input1.delete(True)
    

    await editable.edit("**Enter Resolution 🎞️ : **\n\n**144**\n**240**\n**360**\n**480**\n**720**\n**1080**\n\n**please choose quality**")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    await input2.delete(True)
    try:
        if raw_text2 == "144":
            res = "256x144"
        elif raw_text2 == "240":
            res = "426x240"
        elif raw_text2 == "360":
            res = "640x360"
        elif raw_text2 == "480":
            res = "854x480"
        elif raw_text2 == "720":
            res = "1280x720"
        elif raw_text2 == "1080":
            res = "1920x1080" 
        else: 
            res = "UN"
    except Exception:
            res = "UN"
    
    

    await editable.edit("Enter 🌟 Extracted name  or send \n\n 📄 You can also specify a custom name \n\n   『 🅹🅰️🅸 🆂🅷🆁🅸 🆁🅰️🅼 ⚡️ 🧑‍💻』 ")
    input3: Message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text
    await input3.delete(True)
    highlighter  = f"️ ⁪⁬⁮⁮⁮"
    if raw_text3 == 'Robin':
        MR = highlighter 
    else:
        MR = raw_text3
    await editable.edit("**𝗘𝗻𝘁𝗲𝗿 𝗣𝘄 𝗧𝗼𝗸𝗲𝗻 𝗙𝗼𝗿 𝗣𝘄 𝗨𝗽𝗹𝗼𝗮𝗱𝗶𝗻𝗴 𝗼𝗿 𝗦𝗲𝗻𝗱 `'noo'` 𝗙𝗼𝗿 𝗢𝘁𝗵𝗲𝗿𝘀**")
    input4: Message = await bot.listen(editable.chat.id)
    raw_text4 = input4.text
    await input4.delete(True)
    if raw_text4 == 'noo':
        MR = token
    else:
        MR = raw_text4
   
    await editable.edit("Now Upload a Thumbnail URL 🔗 =  \n Or if don't want thumbnail send = no")
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text
    await input6.delete(True)
    await editable.delete()

    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"

    if len(links) == 1:
        count = 1
    else:
        count = int(raw_text)

    try:
        for i in range(count - 1, len(links)):

            V = links[i][1].replace("file/d/","uc?export=download&id=").replace("www.youtube-nocookie.com/embed", "youtu.be").replace("?modestbranding=1", "").replace("/view?usp=sharing","") # .replace("mpd","m3u8")
            url = "https://" + V

            if "tencdn.classplusapp" in url:
                headers = {'Host': 'api.classplusapp.com', 'x-access-token': 'eyJjb3Vyc2VJZCI6IjQ1NjY4NyIsInR1dG9ySWQiOm51bGwsIm9yZ0lkIjo0ODA2MTksImNhdGVnb3J5SWQiOm51bGx9', 'user-agent': 'Mobile-Android', 'app-version': '1.4.37.1', 'api-version': '18', 'device-id': '5d0d17ac8b3c9f51', 'device-details': '2848b866799971ca_2848b8667a33216c_SDK-30', 'accept-encoding': 'gzip'}
                params = (('url', f'{url}'),)
                response = requests.get('https://api.classplusapp.com/cams/uploader/video/jw-signed-url', headers=headers, params=params)
                url = response.json()['url']  

          
            
            elif 'media-cdn.classplusapp.com' in url or 'media-cdn-alisg.classplusapp.com' in url or '4b06bf8d61c41f8310af9b2624459378203740932b456b07fcf817b737fbae27' in url:
                headers = { 'x-access-token': 'eyJjb3Vyc2VJZCI6IjQ1NjY4NyIsInR1dG9ySWQiOm51bGwsIm9yZ0lkIjo0ODA2MTksImNhdGVnb3J5SWQiOm51bGx9',"X-CDN-Tag": "empty"}
                response = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers=headers)
                url   = response.json()['url']
            elif 'media-cdn' in url or 'webvideos' in url or 'drmcdni' in url:
             url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers={'x-access-token': 'eyJjb3Vyc2VJZCI6IjQ1NjY4NyIsInR1dG9ySWQiOm51bGwsIm9yZ0lkIjo0ODA2MTksImNhdGVnb3J5SWQiOm51bGx9'}).json()['url']
            elif 'cpvod' in url or 'media-cdn.classplusapp.com' in url or 'media-cdn-alisg.classplusapp.com' in url:
             url =f'https://extractbot.onrender.com/classplus?link={url}'    
            elif "apps-s3-jw-prod.utkarshapp.com" in url:

                
        
                if 'enc_plain_mp4' in url:
                    url = url.replace(url.split("/")[-1], res+'.mp4')
                    
                elif 'Key-Pair-Id' in url:
                    url = None
                    
                elif '.m3u8' in url:
                    q = ((m3u8.loads(requests.get(url).text)).data['playlists'][1]['uri']).split("/")[0]
                    x = url.split("/")[5]
                    x = url.replace(x, "")
                    url = ((m3u8.loads(requests.get(url).text)).data['playlists'][1]['uri']).replace(q+"/", x)
            
                
                
                
            if "embed" in url:
                ytf = f"bestvideo[height<={raw_text2}]+bestaudio/best[height<={raw_text2}]"
            
            elif '/utkarshapp.mpd' in url:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
             id =  url.split("/")[-2]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
             url =  "https://apps-s3-prod.utkarshapp.com/admin_v1/file_library/videos/enc_plain_mp4/" + id + "/plain/{res}.mp4"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
            elif "/khansirvod4" and "akamaized" in url:
              url = url.replace(url.split("/")[-1], raw_text2+".m3u8")
                         
            elif "edge.api.brightcove.com" in url:
                bcov = 'bcov_auth=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE3MjQyMzg3OTEsImNvbiI6eyJpc0FkbWluIjpmYWxzZSwiYXVzZXIiOiJVMFZ6TkdGU2NuQlZjR3h5TkZwV09FYzBURGxOZHowOSIsImlkIjoiZEUxbmNuZFBNblJqVEROVmFWTlFWbXhRTkhoS2R6MDkiLCJmaXJzdF9uYW1lIjoiYVcxV05ITjVSemR6Vm10ak1WUlBSRkF5ZVNzM1VUMDkiLCJlbWFpbCI6Ik5Ga3hNVWhxUXpRNFJ6VlhiR0ppWTJoUk0wMVdNR0pVTlU5clJXSkRWbXRMTTBSU2FHRnhURTFTUlQwPSIsInBob25lIjoiVUhVMFZrOWFTbmQ1ZVcwd1pqUTViRzVSYVc5aGR6MDkiLCJhdmF0YXIiOiJLM1ZzY1M4elMwcDBRbmxrYms4M1JEbHZla05pVVQwOSIsInJlZmVycmFsX2NvZGUiOiJOalZFYzBkM1IyNTBSM3B3VUZWbVRtbHFRVXAwVVQwOSIsImRldmljZV90eXBlIjoiYW5kcm9pZCIsImRldmljZV92ZXJzaW9uIjoiUShBbmRyb2lkIDEwLjApIiwiZGV2aWNlX21vZGVsIjoiU2Ftc3VuZyBTTS1TOTE4QiIsInJlbW90ZV9hZGRyIjoiNTQuMjI2LjI1NS4xNjMsIDU0LjIyNi4yNTUuMTYzIn19.snDdd-PbaoC42OUhn5SJaEGxq0VzfdzO49WTmYgTx8ra_Lz66GySZykpd2SxIZCnrKR6-R10F5sUSrKATv1CDk9ruj_ltCjEkcRq8mAqAytDcEBp72-W0Z7DtGi8LdnY7Vd9Kpaf499P-y3-godolS_7ixClcYOnWxe2nSVD5C9c5HkyisrHTvf6NFAuQC_FD3TzByldbPVKK0ag1UnHRavX8MtttjshnRhv5gJs5DQWj4Ir_dkMcJ4JaVZO3z8j0OxVLjnmuaRBujT-1pavsr1CCzjTbAcBvdjUfvzEhObWfA1-Vl5Y4bUgRHhl1U-0hne4-5fF0aouyu71Y6W0eg'
                url = url.split("bcov_auth")[0]+bcov

            elif '/master.mpd' in url:
             id =  url.split("/")[-2]
             url =  f"https://madxapi-d0cbf6ac738c.herokuapp.com/{id}/master.m3u8?token={raw_text4}"

            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").replace("https", "").replace("http", "").strip()
            name = f'{str(count).zfill(3)}) {name1[:60]}'
            if "youtu" in url:
                ytf = f"b[height<={raw_text2}][ext=mp4]/bv[height<={raw_text2}][ext=mp4]+ba[ext=m4a]/b[ext=mp4]"
            else:
                ytf = f"b[height<={raw_text2}]/bv[height<={raw_text2}]+ba/b/bv+ba"

            if "jw-prod" in url:
                cmd = f'yt-dlp -o "{name}.mp4" "{url}"'
            elif 'd1wy033kfw4qbc.cloudfront.net' in url:
                cmd = f'yt-dlp -f "{ytf}" "{url}" --referer "https://iasscore.edugyaan.com/" -o "{name}.mp4"'
            elif 'penpencilvod.pc.cdn.bitgravity.com' in url :
                cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4" --add-header authorization:"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjAwODUzNDQuNTksImRhdGEiOnsiX2lkIjoiNjY2NmUxY2VmNmEzYjNlNGU3ODIyMTVkIiwidXNlcm5hbWUiOiI5MDI0NTU0NTc2IiwiZmlyc3ROYW1lIjoiUmFodWwiLCJsYXN0TmFtZSI6IiIsIm9yZ2FuaXphdGlvbiI6eyJfaWQiOiI1ZWIzOTNlZTk1ZmFiNzQ2OGE3OWQxODkiLCJ3ZWJzaXRlIjoicGh5c2ljc3dhbGxhaC5jb20iLCJuYW1lIjoiUGh5c2ljc3dhbGxhaCJ9LCJlbWFpbCI6InJhaHVsY2hvdWhhbkBnbWFpbC5jb20iLCJyb2xlcyI6WyI1YjI3YmQ5NjU4NDJmOTUwYTc3OGM2ZWYiXSwiY291bnRyeUdyb3VwIjoiSU4iLCJ0eXBlIjoiVVNFUiJ9LCJpYXQiOjE3MTk0ODA1NDR9.NKpXT-e5Mzrrj1t05qLIGOGqyRbEXEGuUJ1q9xnIFNs"'
            else:
                cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'
            try:  
                
                cc = f'**——— ✦ ** {str(count).zfill(3)}.**——— ✦ ** \n\n** 🎞️ Title :**{𝗻𝗮𝗺𝗲𝟭}\n**├── Extention : @Course_diploma_bot.mkv**\n**├── Resolution : {res}**\n\n**📚 Course** » **{raw_text0}**\n\n**🌟 Extracted By** **{raw_text3}**'
                cc1 = f'**——— ✦ ** {str(count).zfill(3)}.**——— ✦ **\n\n**📁 Title  :** {𝗻𝗮𝗺𝗲𝟭}\n**├── Extention : @Course_diploma_bot.pdf**\n\n**📚 Course** » **{raw_text0}**\n\n**🌟 Extracted By** **{raw_text3}**'
                if "drive" in url:
                    try:
                        ka = await helper.download(url, name)
                        copy = await bot.send_document(chat_id=m.chat.id,document=ka, caption=cc1)
                        count+=1
                        os.remove(ka)
                        time.sleep(1)
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                
                elif ".pdf" in url:
                    try:
                        cmd = f'yt-dlp -o "{name}.pdf" "{url}"'
                        download_cmd = f"{cmd} -R 25 --fragment-retries 25"
                        os.system(download_cmd)
                        copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', caption=cc1)
                        count += 1
                        os.remove(f'{name}.pdf')
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                else:
                    progress_percent = (count / len(links)) * 100
                    Show = f"**🚀 𝐏𝐑𝐎𝐆𝐑𝐄𝐒𝐒 = {progress_percent:.2f}%  🚀... »**\n\n**├──🎞️ 📊 Total Links = {len(links)}**\n\n**├──🎞️ ⚡️ Currently On = {str(count).zfill(3)}**\n\n**├──🎞️ 🔥 Remaining Links = {len(links) - count}**\n\n**├──🎞️ 📈 Progress = {progress_percent:.2f}% **\n\n**├──🎞️ Title** {name}\n\n**├── Resolution {raw_text2}**\n\n**├── Url : ** `Time Gya Url Dekhne ka 😅`\n\n**├── Bot Made By : **『 🅹🅰️🅸 🆂🅷🆁🅸 🆁🅰️🅼 ⚡️ 🧑‍💻』"
                    prog = await m.reply_text(Show)
                    res_file = await helper.download_video(url, cmd, name)
                    filename = res_file
                    await prog.delete(True)
                    await helper.send_vid(bot, m, cc, filename, thumb, name, prog)
                    count += 1
                    time.sleep(1)

            except Exception as e:
                await m.reply_text(
                    f"**downloading Interupted **\n{str(e)}\n**Name** » {name}\n**Link** » `{url}`"
                )
                continue

    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("**𝔻ᴏɴᴇ 𝔹ᴏ𝕤𝕤😎**")


bot.run()

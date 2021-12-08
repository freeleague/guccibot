#слито в @sakh7_bot

import pyrogram 
import time
from pyrogram import Client, filters
import asyncio
#слито в @sakh7_bot

api_id = 3225191
api_hash = 'a683fb95b3272e963a65c26138fc3cc9'
#слито в @sakh7_bot
app = Client("my_account", api_id, api_hash)

#слито в @tg_Inc_soft
@app.on_message(filters.command("all", prefixes="/"))
def an(_, msg):
   answ = msg.text.split("/all ", maxsplit=1)[1]
   toy = msg.chat.id
   da = []
   for ddd in app.iter_chat_members(toy):
        da.append(ddd)
   idx = []
   for op in range(0, 5000):
        try:
          ser = da[op].user.id
          idx.append(ser)
        except IndexError as e:
          break
     #слито в @sakh7_bot       
   ping = []
   pong = []
   n = 0
   m = 0
   smi = ["😎", "😃", "😜", "😉", "😍", "😂", "🤣", "😊", "❤", "😒", "👌", "😘", "💕", "😁", "👍"]
   for d in range(0, 5000):
      try:
        ping.append(idx[d])
        n += 1
        if n == 5:
          pong.append(ping)
          ping = []
          n = 0
          m += 1
      except IndexError as e:
          break
   app.send_message(toy, (f'Все сюда по причине: {answ}'))
   sleep(3)
   for pe in range(0, m):
      try:
          random.shuffle(smi)
          app.send_message(toy, (
          f'<a href=\"tg://user?id={pong[pe][0]}\">{smi[0]}</a> <a href=\"tg://user?id={pong[pe][1]}\">{smi[1]}</a> <a href=\"tg://user?id={pong[pe][2]}\">{smi[2]}</a> <a href=\"tg://user?id={pong[pe][3]}\">{smi[3]}</a> <a href=\"tg://user?id={pong[pe][4]}\">{smi[4]}</a>\n'
          'Реклама/текст'))
      except IndexError as e:
          break
      except FloodWait as e:
          sleep(e.x) 
app.run()
#слито в @sakh7_bot
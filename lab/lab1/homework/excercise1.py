from datetime import datetime
from gmail import GMail, Message
from random import choice

now = datetime.now()
n= now.day
while n == now.day:
    if now.hour >= 7:
        html_template = '''
        <p>Dear sep,<br /><br />Dem qua e bi {{sicknes}} qua. Sep cho em xin phep nghi sang nay.<br /><br />E cam on sep</p>
        '''

        sickness_list=["Thuong han", "kiet li", "Ebola"]
        sickness=choice(sickness_list)
        html_content=html_template.replace("{{sicknes}}", sickness)

        gmail = GMail('minhthanh.ben@gmail.com','minhngoc')
        msg = Message('Xin nghi om' ,to='<c4e.201708@gmail.com>', html=(html_content))
        gmail.send(msg)

        n+=1

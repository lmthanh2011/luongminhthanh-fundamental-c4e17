from gmail import GMail, Message
from random import choice

# gmail = GMail('minhthanh.ben@gmail.com','minhngoc')
# msg = Message('Xin' ,to='<c4e.201708@gmail.com>',text='Hello a Huy', html="<b>ốm lắm</b>"))
# gmail.send(msg)

html_template = '''
<p>Em ch&agrave;o sếp,.<br /><br /><br />H&ocirc;m n&agrave;o {{sicknes}} trời đẹp {{sickness}}fsdfsfsdfsdfsdfs<br /><br />adasdasd</p>
'''

sickness_list=["Thuong han", "kiet li", "Ebola"]
sickness=choice(sickness_list)
html_content=html.template.replace("{sickness}"), "thuong han")


gmail = GMail('minhthanh.ben@gmail.com','minhngoc')
msg = Message('Xin' ,to='<c4e.201708@gmail.com>', html=html_content))
gmail.send(msg)

sickness_list=["Thuong han", "kiet li", "Ebola"]
sickness=choice(sickness_list)

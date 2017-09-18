from datetime import date
from hashlib import sha512

baner="""
 _______    ______    ______  
|       \  /      \  /      \ 
| $$$$$$$\|  $$$$$$\|  $$$$$$\
| $$  | $$| $$ __\$$| $$__| $$
| $$  | $$| $$|    \| $$    $$
| $$  | $$| $$ \$$$$| $$$$$$$$
| $$__/ $$| $$__| $$| $$  | $$
| $$    $$ \$$    $$| $$  | $$
 \$$$$$$$   \$$$$$$  \$$   \$$
                              
                              
                              
"""



def DGA(n,d=None):
	if None==d:
		d='{0.year}--{0.month}--{0.day}'.format(date.today())
		tlds=['.cc','.ws','.to','.in','.hk','.cn','.tk','.so']
		hash=sha512('{0}{1}'.format(d,n)).hexdigest()[3:36]
		rep=chr(0xFF &((n%26)+97))
		return '{0}{1}{2}:443'.format(rep,hash,tlds[n%len(tlds)])


print baner

todomains=[DGA(i) for i in range(300000)]
for i in todomains:
	print i
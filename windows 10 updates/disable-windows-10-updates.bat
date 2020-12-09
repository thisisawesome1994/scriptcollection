sc config wuauserv start= disable
sc config bits start= disable
sc config DcomLaunch start= disable
net stop wuauserv
net stop bits
net stop DcomLaunch
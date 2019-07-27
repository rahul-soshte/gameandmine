import psutil
import sys, string, os
import time
from ctypes import Structure, windll, c_uint, sizeof, byref

games = ['firefox.exe'] #Enter the games here
mining_software = ['NiceHashMiner.exe','xmr-stak.exe','sgminer.exe'] #Enter your mining software here.

# os.popen(r"C:\\Users\\Rahul\\AppData\\Local\\WinXmr\\WinXmr.exe")


class LASTINPUTINFO(Structure):
    _fields_ = [
        ('cbSize', c_uint),
        ('dwTime', c_uint),
    ]

def get_idle_duration():
    lastInputInfo = LASTINPUTINFO()
    lastInputInfo.cbSize = sizeof(lastInputInfo)
    windll.user32.GetLastInputInfo(byref(lastInputInfo))
    millis = windll.kernel32.GetTickCount() - lastInputInfo.dwTime
    return millis / 1000.0


def iter():
	while True:
		damn = checkpresenceofminingprocess()
		rand = checkpresenceofgameprocess()

		if rand is False:
			if damn is None:
				os.popen(r"C:\\Users\\Rahul\\Desktop\\nhm_windows\\NiceHashMiner.exe")
				# os.popen(r"C:\\Users\\Rahul\\AppData\\Local\\WinXmr\\WinXmr.exe")
				time.sleep(10)
				# try:# os.popen(r"C:\\Users\\Rahul\\AppData\\Local\\WinXmr\\WinXmr.exe")
				# 	os.popen(r"C:\\Users\\Rahul\\Desktop\\xmr-stak-win64-2.10.5\\xmr-stak.exe")
				# 	time.sleep(10)
				# except:	
		elif rand is True:
			if damn is not None:
				damn.kill()
				time.sleep(2)
	
def checkpresenceofminingprocess():
	for proc in psutil.process_iter():
		try:
			pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
			if pinfo['name'] in mining_software:
				return proc
		except:
			pass
	

def checkpresenceofgameprocess():
	for proc in psutil.process_iter():
		try:
			pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
			if pinfo['name'] in games:
				if get_idle_duration() > 300:
					return False
				else:
					return True
		except:
			pass

	return False

# def iter2():		
# 	while True:
# 		print(get_idle_duration())

iter()
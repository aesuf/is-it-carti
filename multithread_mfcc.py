import os
import re
import multiprocessing as mp
from pathlib import Path

root = "Carti_Songs_WAV"
thread1,thread2,thread3,thread4 = [],[],[],[]

for subdir, dirs, files in os.walk(root):
	for x in range(1,len(files),4):
		try:
			thread1.append(subdir+"/"+files[x])
			thread2.append(subdir+"/"+files[x+1])
			thread3.append(subdir+"/"+files[x+2])
			thread4.append(subdir+"/"+files[x+3])
		except:
			print("FINISHED LOADING QUEUES")

def compute_mfcc(thread):
	for song in thread:
		output = re.sub('.wav$','.csv',song)
		print(":[I]: STARTING FILE: "+song)
		try:
			os.system('./mfcc --input '+song+' --output '+output+' --samplingrate 44100')
			print(":[I]: FINISHED FILE: "+song)
		except:
			continue

try:
	t1 = mp.Process(target=compute_mfcc,args=(thread1,))
	t2 = mp.Process(target=compute_mfcc,args=(thread2,))
	t3 = mp.Process(target=compute_mfcc,args=(thread3,))
	t4 = mp.Process(target=compute_mfcc,args=(thread4,))
	t1.start()
	t2.start()
	t3.start()
	t4.start()
	t1.join()
	t2.join()
	t3.join()
	t4.join()
except:
	print(":[E]: CANT MULTITHREAD")

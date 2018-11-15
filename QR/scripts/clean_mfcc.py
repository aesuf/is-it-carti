import pandas as pd
import numpy as np
import sys
import getopt
from pathlib import Path

in_file  = None
out_file = None
argv     = sys.argv[1:]
out_df   = []
carti    = None

try:
	opts,args = getopt.getopt(argv,"i:o:c:",["input=","output=","carti="])
except getopt.GetoptError as err:
	print(err)
	opts = []

for opt,arg in opts:
	if opt in ['-i','--input']:
		in_file = arg
	elif opt in ['-o','--output']:
		out_file = Path(arg)
	elif opt in ['-c','--carti']:
		carti = arg

try:
	in_df = pd.read_csv(in_file,header=None)
except:
	print('Invalid input')

for col in in_df:
	out_df.append(in_df[col].std())
	out_df.append(in_df[col].mean())

out_df = pd.DataFrame.from_dict(out_df).T
columns = ['mffc_a_std','mffc_a_mean','mffc_b_std','mffc_b_mean',
					 'mffc_c_std','mffc_c_mean','mffc_d_std','mffc_d_mean',
					 'mffc_e_std','mffc_e_mean','mffc_f_std','mffc_f_mean',
					 'mffc_g_std','mffc_g_mean','mffc_h_std','mffc_h_mean',
					 'mffc_i_std','mffc_i_mean','mffc_j_std','mffc_j_mean',
					 'mffc_k_std','mffc_k_mean','mffc_l_std','mffc_l_mean',
					 'mffc_m_std','mffc_m_mean']

out_df.columns = columns
out_df['carti'] = carti

if out_file.is_file():
	print('File already exists, appending data...')
	with open(out_file,'a') as FH:
		out_df.to_csv(FH,header=False,index=False)
else:
	print('File does not exists, writing new CSV file...')
	with open(out_file,'w') as FH:
		out_df.to_csv(FH,header=True,index=False)

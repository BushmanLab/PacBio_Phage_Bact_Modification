import re


opt = file('../0_Data/Processed_Data/10_All_Sequences_rename.table','w')
opin = file('../0_Data/Processed_Data/10_All_Sequences.table','r')
for line in opin:
	line = line.rstrip().replace(":","\t")
	arr = line.split('\t')
	if arr[1] == 'T4_wt':
		ID = 'T4GlcHMC'
		Type = 'T4'
	elif arr[1] == 'T4_147':
		ID = 'T4HMC'
		Type = 'T4'
	elif arr[1] == 'T4_GT7':
		ID = 'T4C'
		Type = 'T4'
	elif arr[1] == 'T4_WGA':
		ID = 'T4WGA'
		Type = 'T4'
	###
	if arr[0] == '5_Phage1.table':
		ID = arr[1]
		Type = 'Phage1'
	elif arr[0] == '6_Phage2.table':
		ID = arr[1]
		Type = 'Phage2'
	elif arr[0] == '7_Bacteria1.table':
		ID = arr[1]
		Type = 'Bact1'
	elif arr[0] == '8_Bacteria2.table':
		ID = arr[1]
		Type = 'Bact2'
	
	opt.write(('%s\t%s\t%s\n')%(Type,ID,arr[2]))
opt.close()
opin.close()


# T4_wt
# T4_147
# T4_GT7
# T4_WGA


# 5_Phage1.table 
# 6_Phage2.table 
# 7_Bacteria1.table
# 8_Bacteria2.table
# 1_T4_phage_all.fasta.table    
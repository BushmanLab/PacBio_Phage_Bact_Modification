import re


#### load sequences data
##  


id2seq = {}
id2seqlen = {}
id2seqefflen = {}
id2gc = {}
opin = file('../../0_Data/Processed_Data/10_All_Sequences_rename.table','r')
for line in opin:
	line = line.rstrip()
	arr  = line.split('\t')
	seqid = arr[1]
	seq   = arr[2]
	if seqid in id2seq:
		print 'duplicated',seqid
	id2seq[seqid] = seq
	id2seqlen[seqid] = len(seq)
	id2seqefflen[seqid] = seq.count('G')+seq.count('T')+seq.count('C')+seq.count('A')
	id2gc[seqid] = float(seq.count('g')+seq.count('G')+seq.count('c')+seq.count('C'))/float(id2seqlen[seqid])
opin.close()

#### load ipd data
# Type	ID	Pos	Strand	Base	Cov	IPDRatio	Score
# T4	T4C	1	Fwd	A	64	0.675	0
# T4	T4C	1	Rev	T	82	2.526	49
# T4	T4C	2	Fwd	A	71	0.964	2
# T4	T4C	2	Rev	T	91	4.184	85
# T4	T4C	3	Fwd	T	78	0.956	2
# T4	T4C	3	Rev	A	90	1.751	32
# T4	T4C	4	Fwd	T	84	0.718	0
# T4	T4C	4	Rev	A	98	2.876	92

  
opin = file('../../0_Data/Merged_IPD/ipd_merged.txt','r')
opt = file('../../0_Data/Merged_IPD/ipd_merged_filter.txt','w')
for line in opin:
	if re.search('^Type',line):
		opt.write(line)
		continue
	line = line.rstrip()
	arr  = line.split('\t')
	dtype = arr[0]
	dID   = arr[1]
	pos   = int(arr[2])
	## 1. Filter high GC one
	## 2. Filter short one
	## 3. Filter repeat
	## 4. Filter start/end 100 bp
	if pos <= 100: continue
	if pos >= (id2seqlen[dID]-100): continue
	if id2seqlen[dID]<1000:continue
	if id2gc[dID]>0.9:continue
	if id2gc[dID]<0.1:continue
	if id2seqefflen[dID]<500:continue
	opt.write(('%s\n') % (line))
opt.close()
opin.close()
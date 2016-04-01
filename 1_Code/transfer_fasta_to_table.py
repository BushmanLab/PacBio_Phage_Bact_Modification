#!/usr/bin/env python
"""Transform fasta format file into a table with two columns: header\tseqeunce

Usage:
    python transform_fasta_to_table.py infile outfile
"""

# Importing modules
import sys,re

# Parsing user input
try:
    infile = sys.argv[1]
    outfile = sys.argv[2]
except:
    print __doc__
    sys.exit(1)



# Main
if __name__ == "__main__":
    opin = file(infile,'r')
    opt  = file(outfile,'w')
    seq = ''
    for line in opin:
        line = line.rstrip()
        if re.search('^>',line):
            #print line
            if len(seq) > 0:
                opt.write( '%s\t%s\n' % (id,seq))
            id  = line.replace('>','')
            seq = '' 
            continue
        else:
            seq = seq + line
    ### last fasta entry
    opt.write( '%s\t%s\n' % (id,seq))
    ###
    opt.close()
    opin.close()
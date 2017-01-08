from Bio import SeqIO
import glob


path ='./data/*.fa' 
print(glob.glob(path))
i=0
k=0
for f in glob.glob(path):
    recs = SeqIO.parse(f, 'fasta')
    f = open('trim'+str(i)+'.fa', 'w')
    k=0
    for rec in recs:
        if(k>1000):
            break
        seq = str(rec.seq).split('#')[0][1:31]
        if(len(seq)<30):
            continue
        f.write('>'+rec.id+'\n')
        
        if(len(seq)<30):
            continue
        f.write(seq+'\n')
        k+=1
        
    i=i+1
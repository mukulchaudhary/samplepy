# https://www.biostars.org/p/162853

cache = {}

f2 = open('f2')
header2 = f2.next()

for line in f2:
    fields = line.strip().split()
    snp = fields[0]
    cache[snp] = '\t'.join(fields[1:])

f1 = open('f1')
header1 = f1.next()
print header1.strip() + '\t' + '\t'.join(header2.split()[1:])

for line in f1:
    line = line.strip()
    fields = line.split()
    snp = fields[0]
    if snp in cache:
        print '{}\t{}'.format(line, cache[snp])
    else:
        print '{}\t0\t0\t0\t0\t0'.format(line)
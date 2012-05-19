# Generate python33stub.def out of python3.def
# The regular import library cannot be used,
# since it doesn't provide the right symbols for
# data forwarding
out = open("python33stub.def", "w")
out.write('LIBRARY "python33"\n')
out.write('EXPORTS\n')

inp = open("python3.def")
inp.readline()
line = inp.readline()
assert line.strip()=='EXPORTS'

for line in inp:
    # SYM1=python33.SYM2[ DATA]
    head, tail = line.split('.')
    if 'DATA' in tail:
        symbol, tail = tail.split(' ')
    else:
        symbol = tail.strip()
    out.write(symbol+'\n')

inp.close()
out.close()

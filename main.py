f = open("date.txt")

n = int(f.readline().split()[1])

d = {}

for i in range(n):
    l = f.readline().split()
    nod = l[0]
    t = (l[2], l[1], l[3])    # t = (litera, starea urmatoare, output)
    if nod in d:
        d[nod].append(t)
    else:
        d[nod] = [t]

print(d)

stinit = f.readline().split()[0]

starifinale = f.readline().split()[1:]

nrcuv = int(f.readline().split()[0])

for nr in range(nrcuv):
    cuv = f.readline().strip()
    output = []
    drum = [stinit]
    stare = stinit
    for i in range(len(cuv)):
        litera = cuv[i]
        x = d.get(stare)
        for j in range(len(x)):
            if x[j][0] == litera:
                stare = x[j][1]
                drum.append(stare)
                output.append(x[j][2])
    if stare in starifinale:
        print("DA")
        print(*output)
        print("Traseu: ")
        print(*drum)
    else:
        print("NU")

f.close()
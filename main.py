f = open("date.txt")
g = open("afis.txt", "w")

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
        g.write("DA\n")
        for e in output:
            g.write(e + " ")
        g.write("\nTraseu: ")
        for e in drum:
            g.write(e + " ")
        g.write("\n")
    else:
        g.write("NU\n")

f.close()
g.close()
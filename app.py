#python script dat zinnen omdraaid

zin = input("Voer een zin in: ")
zin_lijst = zin.split()
e = len(zin_lijst)-1
new_sent = []
while e >= 0:
     new_sent.append(zin_lijst[e])
     e -=1

zin_reverse = " ".join(new_sent)
print(zin_reverse)


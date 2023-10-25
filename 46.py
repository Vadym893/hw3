lines= int(input("write how muvh is a side of this cube: "))
number=0
line = ""
for j in range(1,lines+1):
    number=j
    for i in range(1,lines+1):
        line += f"{number*i}"+" "
    print(line)
    line+="\n"
    line=""
    
    
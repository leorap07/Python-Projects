birthdate = input("What is your birthday, separated by commas (mm/dd/yyyy)?")
bd = birthdate.split(", ")

mm = int(bd[0])
dd = int(bd[1])
yy = int(bd[2])
#print(bd)
print(mm,dd,yy)

if yyy % 12 
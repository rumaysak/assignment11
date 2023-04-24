def displayarrays(lname):
    for i in range (0,5):
      print(lname[i])

      print("Another display using for loops")
      for x in range (2, 5):
       print(lname[i])
       
      for j in lname:
        print(j)

def rdisplay(lname):
      for x in range (4, -1, -1):
       print(lname[i])

print(lname)
bavg = lname[::-1]
print(bavg)
lname.reverse()
print(lname)
lname = ["Kennedy", "Gomez", "Lewis" "Zaffar", "Jones"]

bavg = [0.267, 0.300, 0.350, 0.475, 0.566]

displayarrays(lname)
print("reverse order")
rdisplay(lname)
lname3 = []
bavg = []
f = open("myfile.txt", "r")
for i in range (0,5,1):
  lname3[1] = f.readline();
 print(lname3[i])
    bavg[1] = f.readline()
  f.close()
#loadarrays(lname3, bavg)
darrays(lname3, bavg)


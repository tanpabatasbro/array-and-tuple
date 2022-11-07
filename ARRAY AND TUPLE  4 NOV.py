
#pendefinisian list
print("pendefinisian list")
word = ["belajar","python","di","teknik","informatika"]
value = [50,100,150,200]
com = ["python", 200,6.99,True]

print(word)
print(value)
print(com)
print()
#pengaksesan list
print("pengaksesan list")
com = ["python",100,5.99,True,"teknik","informatika",80j]
print(com[0])
print(com[1])
print(com[3])
print()

#penggantian nilai/data pada satuu elemen list
print("penggantian nilai/data pada satuu elemen list")
com = ["python",100,5.99,True,"teknik","informatika",80j]

print(com)
com[1] = 200
com[3] = False
print(com)
print()

#menampilkan sebagian list
print("menampilkan sebagian list")
com = ["python",100,5.99,True,"teknik","informatika",80j]
print(com[2:5])
print(com[:3])
print(com[3:])
print(com[:])
print()

#penambahan data pada list
print("penambahan data pada list")
com = ["python",100,5.99,True,"teknik","informatika",80j]
com.append(2)
print(com)
print()

#pendefinisian tuple
print("pendefinisian tuple")
word = ["belajar","python","di","teknik","informatika"]
value = [50,100,150,200]
com = ["python", 200,6.99,True]

print(word)
print(value)
print(com)
print()

#pengakses elemen tuple
print("pengakses elemen tuple")
com = ["python",100,5.99,True,"teknik","informatika",89j]
print(com[0])
print(com[1])
print(com[3])
print(com[2:5])
print(com[:4])
print(com[4:])
print(com[:])
print()

#tuple tidak dapat melakukan perubahan/penambahan data
print("tuple tidak dapat melakukan perubahan/penambahan data")
com = ["python",100,5.99,True,"teknik","informatika",89j]

com[0]="belajar"
print(com)


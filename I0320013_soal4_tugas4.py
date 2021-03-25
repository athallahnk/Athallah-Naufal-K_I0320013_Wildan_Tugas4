inputUser= float(input("Berapa usia anda?\n:"))

#Umur minimal 21 tahun
isLebihDariSamaDengan =(inputUser >= 21)
print("Usia anda =" ,isLebihDariSamaDengan)

inputUser= str(input("Apakah telah lulus ujian spesifikasi? Y/T\n:"))
Y=True
T=False
print('not Y is',not Y)

a=True
b=True
c= a and b
c= "Anda dapat mendaftar di kursus"
print(a,'AND',b,'=',c)

a=True
b=False
d= a and b
d= "Anda tidak dapat mendaftar di kursus"
print(a,'AND',b,'=',d)

a=False
b=False
e= a and b
e= "Anda tidak dapat mendaftar di kursus"
print(a,'AND',b,'=',e)

a=False
b=True
f= a and b
f= "Anda tidak dapat mendaftar di kursus"
print(a,'AND',b,'=',f)
a=input("mulher ou homem ?")
print(a)
b=float(input("Qual sua altura?"))
b=((72.7*b) - 58)
c=((62.1*b) - 44.7)
if a=='mulher':
  print(c)
elif a=='homem':
    print(b, "seu peso ideal")

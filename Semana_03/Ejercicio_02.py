a = input()
b = input()

a = int(a)
b = int(b)


respuesta = not((a == b) or (a <= b)) and ((a%b)!=2)
respuesta = respuesta * 1
print(respuesta)
print (" -- EJEMPLO DE FUNCIONES -- ")

# DECLARANDO INSTRUCCIONES
def hola():
    print("Alguien uso la función hola.")

def chat(msg):
    print(f"Chat: {msg}")

def ellacontesta(msg):
    print(f"Chat Ella: {msg}")
    
def escribenombre(ap,n):
    print(f"Tu nombre completo es: {n} {ap}")

def suma(a, b):
    s=a+b
    return s

def resta(a, b):
    r=a-b
    return r

def multi(a, b):
    m=a*b
    return m

def divv(a, b):
    d=a/b
    return d


## LLAMADAS A FUNCIONES

hola()
chat("Que bonita...")
ellacontesta("Graciassss<3")
escribenombre ("Ramirez", "Janna")

print (" -- OPERACIONES SUMA -- ")
c1=int(input("Ingresa un número "))
c2=int(input("Ingresa un número "))
damesuma=suma(c1,c2)
print (f"La suma de {c1} + {c2} = {damesuma}")

print (" -- OPERACIONES RESTA -- ")
c3=int(input("Ingresa un número "))
c4=int(input("Ingresa un número "))
dameresta=resta(c3,c4)
print (f"La resta de {c3} - {c4} = {dameresta}")

print (" -- OPERACIONES MULTIPLICACIÓN -- ")
c5=int(input("Ingresa un número "))
c6=int(input("Ingresa un número "))
damemulti=multi(c5,c6)
print (f"La multiplicación de {c5} x {c6} = {damemulti}")

print (" -- OPERACIONES DIVISIÓN -- ")
c7=int(input("Ingresa un número "))
c8=int(input("Ingresa un número "))
damedivv=divv(c7,c8)
print (f"La división de {c7} entre {c8} = {damedivv}")
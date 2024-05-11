"""
EJERCICIO PRACTICO: POO
fecha: 16 de abril 2024
seccion: 3055C1 

Actividad
1. Crear una clase PERSONA
2. Atributos de la clase: nombre,edad,identificacion
3. Metodos: constructor, sets,gets, mostrar datos
4. validar datos en la consola
5.Devolver mediante un valor logico si es mayor de edad

caso 1: datos ingresados por el teclado
caso 2: matriz generada
caso 3: determinar cuantos mayores de edad hay
"""
#validacion sencilla
def validacionLetra(name):
    while True:
        user_input = input(name)
        # Check if all characters in the input are alphabetic
        if all(65 <= ord(char) <= 90 or 97 <= ord(char) <= 122 for char in user_input):
            return user_input
        else:
            print("Por favor, ingrese solo caracteres alfabéticos.")
def validationNumber(age):
    while True:
        user_input = int(input(age))
        if user_input>0:
            return user_input
        else: print("Por favor, ingrese solo numeros.")
#class 
class People:  
    def __init__(self,name=str(),age=int(),idf=int()) : #construtor
        self.name =name
        self.age =age
        self.idf =idf
    #method get
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getIdf(self):
        return self.idf
    def boolean(self):#method boolean: indica quien es mayor de edad con un booleano
        return True if self.age>=18 else False

ageMayor =0 #contador de mayores de edad
#caso 1: datos ingresados por el teclado
name = validacionLetra("Nombre: ")
age = validationNumber("Edad: ")
idf= int(validationNumber("Identificacion: "))
ageMayor += 1 if People(name,age,idf).boolean() else 0 

#caso 2: datos a travez de una matriz   
i=0
group = [["Lai","Juan","Carlos","Jesus","Rodrigo"], #name
         [19,18,14,12,19], #age
         [30335074,33222111,4333213,31200562,22353421]] #id

while i<len(group[0]):
    p =    People(group[0][i],group[1][i], group[2][i])
    ageMayor += 1 if p.boolean() else 0
    i+=1

#caso 3: imprimir la cantidad de personas que son mayores de edad
print(f"\nMayores de edad: {ageMayor}")
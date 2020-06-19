#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 14:24:23 2019

@author: juan
"""

class Calculadora:

    def __init__(self, numero1, numero2, numeroDeCalculadora):
        self.numero1 = numero1
        self.numero2 = numero2
        self.numeroDeCalculadora = numeroDeCalculadora

    def Operacion(self):
        print(+self.operacion)

    def Calcular(self):
        print("Vamos a calcular la " +self.operacion)


    def sumar(self):
        print("La calculadora "+str(self.numeroDeCalculadora)+ " esta sumando")
        print("Resultado "+str(self.numeroDeCalculadora)+ " es: "+str(self.numero1+self.numero2))


    def restar(self):
        print("La calculadora "+str(self.numeroDeCalculadora)+ " esta restando")
        print("Resultado "+str(self.numeroDeCalculadora)+ " es: "+str(self.numero1-self.numero2))

    def multipl(self):
        print("La calculadora "+str(self.numeroDeCalculadora)+ " esta multiplicando")
        print("Resultado "+str(self.numeroDeCalculadora)+ " es: "+str(self.numero1*self.numero2))

    def dividir(self):
        print("La calculadora "+str(self.numeroDeCalculadora)+ " esta dividiendo.")
        print("Resultado "+str(self.numeroDeCalculadora)+ " es: "+str(self.numero1/self.numero2))

    while True:
        print("Este es un menu para realizar dos operaciones.")
        print("1-Sumar")
        print('2-Restar')
        print("3-Multilplicar")
        print("4-Dividir")
        print("5-Salir")

        seleccion = []

        seleccion.append(float(input("Primer operacion:")))
        seleccion.append(float(input("segunda operacion:")))

        #&& y and, || o or,
        if seleccion[0] == 5 or seleccion [1] == 5:
            break

        #las listas tambien pueden almacenar objetos, cada elemento de la lista puede ser un objeto

        calculadora = []

        for i in range(len(seleccion)):
            print("Operacion " +str(i+1))
            n1 = float(input("Numero 1: "))
            n2 = float(input("Numero 2: "))
            calculadora.append(Calculadora(n1,n2,i+1))

        for i in range(len(seleccion)):
            if seleccion[i] == 1:
                calculadora[i].sumar()
            elif seleccion[i]==2:
                calculadora[i].restar()
            elif seleccion[i]==3:
                calculadora[i].multipl()
            elif seleccion[i]==4:
                calculadora[i].dividir()

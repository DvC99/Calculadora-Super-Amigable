""" Programa calculadora artimética super amigable#
    Realiza las 4 operaciones (+,-,* /)
    dada como entrada una cadena de caracteres 
    incorpora al modulo calculadora_aritmetica.py
    Daniel Valencia Cordero
    Mayo 3-2021 """

#---------------- Zona librerias------------
import calculadora_aritmetica as calc

#----------Definición de Funciones (Dividir)------------
def parser_cadena(cadena_entrada):
  #TODO: codigo que obtiene los numeros y el operando
  vec = cadena_entrada.split()
  numero_uno = vec[0]
  numero_dos = vec[2]
  operando = vec[1]
  return numero_uno, numero_dos, operando

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================
cadena_entrada = input("Digite la operacion aritmetica que quiere realizar, solo se acepta un operador: \n")

#TODO: Leer cadena de entrada
num1,num2,op= parser_cadena(cadena_entrada)
#TODO: terminar programa 
if(op == "+"):
  print("El resultado de al suma de "+num1+" + "+num2+" es = "+str(calc.sumar_numeros(int(num1),int(num2))) )
elif(op == "-"):
  print( "El resultado de al resta de "+num1+" - "+num2+" es = "+str(calc.restar_numeros(int(num1),int(num2))) )
elif(op == "*"):
  print( "El resultado de al multiplicacion de "+num1+" x "+num2+" es = "+str(calc.multiplicar_numeros(int(num1),int(num2))) )
elif(op == "/"):
  if(num1 == "0" and num2 != "0"):
    print( "El resultado de al division de "+num1+" / "+num2+" es = 0")
  elif(num2 == "0" and num1 != "0"):
    print( "El resultado de al division de "+num1+" / "+num2+" es = ERROR DIV FOR 0")
  else:
    print( "El resultado de al division de "+num1+" / "+num2+" es = "+str(calc.dividir_numeros(int(num1),int(num2))) )
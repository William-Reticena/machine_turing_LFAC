from operations.addition import dtm_add
from operations.subtraction import dtm_sub
from operations.multiplication import dtm_mult
from operations.division import dtm_div

print("MÁQUINA DE TURING")
print("Qual operação aritmética você deseja realizar?")
print("[1] - Operação de adição")
print("[2] - Operação de subtração")
print("[3] - Operação de multiplicação")
print("[4] - Operação de divisão")
option = int(input("Opção: "))

def add():
  print("Insira uma string para servir como fita da MT")
  print("Ela deve ser no formato \"#EEEEE+EE#\" como exemplo")
  print("Onde quantidade de E's representa um número (O número 5 representado como EEEEE)")
  tape = input("Fita: ")
  dtm_add.read_input(tape).print()

def sub():
  print("Insira uma string para servir como fita da MT")
  print("Ela deve ser no formato \"#EEEEE-EE#\" como exemplo")
  print("Onde quantidade de E's representa um número (O número 5 representado como EEEEE)")
  tape = input("Fita: ")
  dtm_sub.read_input(tape).print()

def mult():
  print("Insira uma string para servir como fita da MT")
  print("Ela deve ser no formato \"#11*111####\" como exemplo")
  print("Onde quantidade de 1's representa um número (O número 5 representado como 11111)")
  tape = input("Fita: ")
  dtm_mult.read_input(tape).print()

def div():
  print("Insira uma string para servir como fita da MT")
  print("Ela deve ser no formato \"#111111/11####\" como exemplo")
  print("Onde quantidade de 1's representa um número (O número 5 representado como 11111)")
  tape = input("Fita: ")
  dtm_div.read_input(tape).print()

if option == 1:
  add()
elif option == 2:
  sub()
elif option == 3:
  mult()
elif option == 4:
  div()
else:
  print("Opção inválida")


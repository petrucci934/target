# int INDICE = 13, SOMA = 0, K = 0; 

#  	enquanto K < INDICE faça 

# 	{ 

# 		K = K + 1; 

# 		SOMA = SOMA + K; 

# 	} 

#  	imprimir(SOMA); 


# Ao final do processamento, qual será o valor da variável SOMA? 

# Resposta: 91

INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

print(SOMA)

# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência. 

def is_fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n

def fibonacci_sequence(n):
    fib = [0, 1]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
    if fib[-1] == n:
        print(f"{n} pertence à sequência de Fibonacci: {fib}")
    else:
        print(f"{n} não pertence à sequência de Fibonacci: {fib}")

n = int(input("Digite um número: "))
fibonacci_sequence(n)



# 3) Descubra a lógica e complete o próximo elemento:  

   

a) 1, 3, 5, 7, _9__  

b) 2, 4, 8, 16, 32, 64, __128__  

c) 0, 1, 4, 9, 16, 25, 36, __49__  

d) 4, 16, 36, 64, _100___  

e) 1, 1, 2, 3, 5, 8, _13___  

f) 2,10, 12, 16, 17, 18, 19, __20__  



# 4 - Dois veículos (um carro e um caminhão) saem respectivamente de cidades opostas pela mesma rodovia. O carro de Ribeirão Preto em direção a Franca, a uma velocidade constante de 110 km/h e o caminhão de Franca em direção a Ribeirão Preto a uma velocidade constante de 80 km/h. Quando eles se cruzarem na rodovia, qual estará mais próximo a cidade de Ribeirão Preto?  

   

# IMPORTANTE:  

# a)            Considerar a distância de 100km entre a cidade de Ribeirão Preto <-> Franca.  

# b)           Considerar 2 pedágios como obstáculo e que o caminhão leva 5 minutos a mais para passar em cada um deles e o carro possui tag de pedágio (Sem Parar)  

# c)            Explique como chegou no resultado. 



    O carro leva tempo = distância / velocidade = 100 km / 110 km/h = 0,9091 horas
    O caminhão leva tempo = distância / velocidade = 100 km / 80 km/h = 1,25 horas


 No ponto de encontro o carro estará a uma distância de apenas 50 km da cidade de Ribeirão Preto


# 5) Escreva um programa que inverta os caracteres de um string. 

  

# IMPORTANTE: 

# 	a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código; 

# 	b) Evite usar funções prontas, como, por exemplo, reverse; 

  


string = input("Digite uma string para inverter: ")
string_invertida = ""

for i in range(len(string)-1, -1, -1):
    string_invertida += string[i]

print("String original:", string)
print("String invertida:", string_invertida)

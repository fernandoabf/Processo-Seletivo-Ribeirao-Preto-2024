#RESOLUÇÃO 2º QUESTÃO

def fibonacci_Sequence(num):

   #Defino os valores iniciais e fixos. Como dá para perceber, a sequência sempre tem esses valores iniciais fixos e serão necessários para a conta.
    fixo_A, fixo_B = 0, 1

    #Agora irei fazer uma verificação para os valores iniciais.
    if fixo_A == num:
        return True
    
    elif fixo_B == num:
         return True
    
    #Agora irei fazer um cálculo da sequência para alcançar ou ultrapassar o valor de 'num'.
    while True:
        
        #Aqui estou definindo que o número atual, ou seja, o que estamos agora, é a soma do fixo A mais o fixo B.
        num_Atual = fixo_A + fixo_B

        #Aqui estou verificando se o número atual é igual ao número desejado. Caso sim, ele retorna True, ou seja, encontramos o número desejado.
        if num_Atual == num:
            return True
        
        #Aqui ele verifica se o número atual é maior que o número desejado. Assim, percebendo que é maior e não caiu na verificação acima, o número não faz parte da sequência e retorna False.
        elif num_Atual > num:
            return False
        
        #Aqui nós iremos fazer com que continue somando após a soma inicial, ou seja, 0,1 vai ser 1,1 e depois 1,2 e depois 2,3 e assim por diante, até achar ou ultrapassar o número desejado.
        fixo_A, fixo_B =  fixo_B, num_Atual

#Agora nós iremos fazer uma função para verificar se pertence ou não.
def fibonacci_Verify(num):
    
    #Chamando a função que usamos para ver a sequência de Fibonacci, e caso pertença, ou seja, retorne True, ele vai printar que pertence.
    if fibonacci_Sequence(num):
        print(f"{num} pertence à sequência de Fibonacci.")
    
    #Caso não pertença à sequência, ele receberá o valor de False e então printar que não pertence.
    else:
        print(f"{num} não pertence à sequência de Fibonacci.")

#Fazendo um input e guardando-o em uma variável para verificar se pertence ou não.
numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))

#Chamando a função fibonacci_Verify() e passando como parâmetro o número anteriormente escolhido.
fibonacci_Verify(numero)
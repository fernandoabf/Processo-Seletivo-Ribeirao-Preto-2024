#RESOLUÇÃO 5º QUESTÃO

def string_Reverse(string):
    
    #Primeiro iremos criar uma lista vzaia para guardar os futuros valores reversos da string.
    list = []

    #após nos iremos fazer um loop para que possamos reverter a string utilizando o range.
    for i in range(len(string),0,-1):
        
        #Como está contando do 5 ao 1 e nos precisamos do 4 ao 0 diminuimos 1 do index.
        i = i-1
        #guardamos cada parte separadamente em uma lista vazia.
        list.append(string[i])
    
    #Juntamos cada parte da lista para assim formar a frase.
    strings = ''.join(list)
    return strings

def string_Verify(string):

    #Printar a string inversamente.
    print(f"Sua string invertida fica assim: {string_Reverse(string)}")
    
    
string = str(input('Digite uma frase: '))
string_Verify(string)
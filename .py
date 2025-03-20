#loja de tintas
#1 litro vale 6 metros quadrados
#tinta em lata vale 18 litros que custa 80 reias



print("Seja bem vindo a nossa loja de tintas, abaixo escolha uma das 3 opções do menu")

#tinta= int(input("quanta tinta quer comprar:"))

print(""" 
----------------Menu--------------------------------
[1]- 1 litro é igual a 6 metros quadrados
[2]- uma lata de tinta vale 18 litros e custa 80 reias
[3]- galoes de 4 L custa 25 reias cada um
""")

opcao=input("Escolha uma das 3 do menu:")

if opcao == '1':
    area= int(input("Quantos metros quadrados voce vai pintar:"))
    tinta_total= area*6
    print(tinta_total)
    
if opcao =='2':
    latas_tinta= int(input("quantas latas de tinta quer comprar:"))
    total=latas_tinta*80
    print(total)
    
if opcao =='3':
    galoes=int(input("quantos galoes quer comprar:"))
    preco= galoes*25
    print('o total da quantidade de galoes vezes o preco fica {}'.format(preco))
else:
    print("não tem essa opcao no nosso menu")

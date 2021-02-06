#Qual time vai para a final
#4) Faça um algoritmo que recebe a quantidade de pênaltis convertidos em gols pelos times
#numa partida de futebol na fase semi-final da copa do Mundo após terem empatado na
#prorrogação.
#Primeiramente pergunte o nome de cada time e quantos gols cada um marcou (salva cada
#informação numa variável):
#● Qual o nome do primeiro time?
#● Time1 marcou quantos gols?
#● Qual o nome do segundo time?
#● Time2 marcou quantos gols?
#● Se o Time1 tiver feito mais gols que o Time2 mostre a mensagem &quot;O Time1 vai para
#a final&quot;, se o resultado for o contrário mostre uma mensagem equivalente para o
#Time2.
import time

time1 = str(input("Qual o nome do seu time? \n"))
gols1 = int(input("%s quantos gols vocês marcaram? \n"% time1))
time2 = str(input("Qual o nome do seu time? \n"))
gols2 = int(input("%s quantos gols vocês marcaram? \n"% time2))

print("Time %s venceu"% time1 if gols1>gols2 else "Time %s venceu"% time2)

time.sleep(0)
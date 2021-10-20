import random

def main():
    acertou = False
    inf, sup = 0, 100
    tentativa = int((sup - inf) / 2)
    while not acertou:
        resposta = input("Pensou no número " + str(tentativa) + "? (Sim/Não)")
        
        if resposta == "Sim":
            acertou = True
            
        else:
            resposta = input ("O número que pensou é maior ou menor que " + str(tentativa) + "? (Maior/Menor)")
            
            if resposta == "Maior":
                inf = tentativa + 1
                
            else:
                sup = tentativa - 1
                
            tentativa = int((sup - inf) / 2) + inf
                
    print("Consegui!")

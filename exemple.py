


a = ['a','b']

b = [(0, 0, 1, 1), (0, 1, 0, 1)]

def multiple(numero):    # Primero declaramos una función condicional
    if numero % 5 == 0:  # Comprobamos si un numero es múltiple de cinco
        return True      # Sólo devolvemos True si lo es

numeros = [2, 5, 10, 23, 50, 33]

print(list(filter(multiple, numeros)))


bo=[1,0,1,1]


    
def Eval_result(t):
    for i in t:
        if i==1 and t.count(1)==len(t):
            return "Tautologie"
            break
        elif i==0 and t.count(0)==len(t): 
            print("Contradicción")
            break
        else: 
            print("Contingencia")
            break
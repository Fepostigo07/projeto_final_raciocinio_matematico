def fazer_pergunta(pergunta, alternativa, correta):
    print("-----------------------------------------")
    print(pergunta)
    print("-----------------------------------------")

    for letra, texto in alternativa.items():
        print(f'{letra}) {texto}')

    while True:
        resposta = input('\nDigite a alternativa correta: ').lower()
        if resposta in alternativa:
            break
        else:
            print('Opção inválida! Por favor, digite uma das letras das alternativas.')

    if resposta == correta:
        return True
    else:
        return False

perguntas = [
    "Questão 1: Complete o código a seguir para que ele funcione corretamente:\n\n"
    "if _____________:\n"
    "   resultado = (math.log((x+5)/(y-2)))**0.5\n"
    "   print('O resultado é:', resultado)\n"
    "else:\n"
    "   print('Não é possível ____________.')",

    "Questão 2: Complete o código a seguir para que ele funcione corretamente:\n\n"
    "if _____________:\n"
    "   resultado = (e**((9 - (x**2))**0.5)) / math.log(y + 3)\n"
    "   print('O resultado é:', resultado)\n"
    "else:\n"
    "   print('Não é possível ____________.')",

    "Questão 3: Complete o código a seguir para que ele funcione corretamente:\n\n"
    "if _____________:\n"
    "   resultado = ((16 - ((x - 1)**2)) / ((y**2) + 1))**0.5\n"
    "   print('O resultado é:', resultado)\n"
    "else:\n"
    "   print('Não é possível ____________.')"
]

alternativas = [
    {
        'a': ("(x + 5) / (y - 2) < 0 and (y - 2) != 0 and (math.log((x+5)/(y-2))) % 2\n"
              "   Fazer log de base positiva ou de base 0, dividir por 0, fazer raiz de número par"),
        'b': ("(x + 5) / (y - 2) > 0 and (y - 2) != 0\n"
              "   Fazer log de base negativa ou de base 0, dividir por 0, fazer raiz de número negativo"),
        'c': ("(x + 5) / (y - 2) != 0 and (y - 2) > 0 and (math.log((x+5)/(y-2))) >= 0\n"
              "   Fazer log de base 0, dividir por número negativo, fazer raiz de número negativo"),
        'd': ("(x + 5) > 0 and y != 0\n"
              "   Fazer log de base negativa ou de base 0, y ser 0")
    },
    {
        'a': " 9 - (x**2) < 0 and y + 3 > 0 and math.log(y + 3) = 0\n"
        "   Fazer log de base negativa , dividir por 0, fazer raiz de número positivo.",
        'b': " 9 - (x**2) = 0 and y + 3 < 0 and math.log(y + 3) > 0\n"
        "   Fazer log de base 0, dividir por número negativo, fazer raiz de número negativo.",
        'c': " 9 - (x**2) > 0 and y + 3 = 0 and math.log(y + 3) < 0\n"
        "   Fazer log de base positiva ou de base 0, dividir por 0, fazer raiz de número negativo.",
        'd': " 9 - (x**2) >= 0 and y + 3 > 0 and math.log(y + 3) > 0\n"
        "   Fazer log de base negativa ou de base 0, dividir por 0, fazer raiz de número negativo."
    },
    {
        'a': "(16 - ((x - 1)**2)) / ((y**2) + 1) >= 0 and ((y**2) + 1) != 0"
             "   Fazer raiz de número negativo, dividir por 0",
        'b': "(16 - ((x - 1)**2)) / ((y**2) + 1) != 0 and ((y**2) + 1) < 0"
             "   Fazer raiz de 0, dividir por número positivo",
        'c': "(16 - ((x - 1)**2)) / ((y**2) + 1) = 0 and ((y**2) + 1) > 0"
             "   Fazer raiz de número negativo, dividir por número negativo",
        'd': "(16 - ((x - 1)**2)) / ((y**2) + 1) < 0 and ((y**2) + 1) != 4"
             "   Fazer raiz de número positivo, dividir por 4"
    }
]

corretas = ['b', 'd', 'a']


total_questoes = len(perguntas)

for i in range(total_questoes):
    if fazer_pergunta(perguntas[i], alternativas[i], corretas[i]):
        print('Resposta correta, Parabéns!')
    else:
        print(f'Alternativa incorreta! A resposta certa era a letra "{corretas[i]}".')

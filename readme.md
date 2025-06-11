# 💻 Quiz: Raciocínio Matemático para Computação

## 📝 Descrição do Projeto

Este projeto consiste em um quiz interativo desenvolvido em Python, elaborado como trabalho para a disciplina de **Raciocínio Matemático para Computação**. A disciplina faz parte do primeiro período do curso de Bacharelado em Engenharia de Software.

O quiz tem como objetivo principal avaliar a compreensão sobre as **condições de existência** de expressões matemáticas, um conceito fundamental na programação para evitar erros em tempo de execução. As questões abordam domínios de funções que envolvem:

* Divisão por zero.
* Logaritmos de números negativos ou zero.
* Raízes quadradas (ou de índice par) de números negativos.

## ⚙️ Estrutura do Código

O script `projetofinal.py` é construído de forma procedural e modular, contendo os seguintes elementos:

1.  **Função `fazer_pergunta(pergunta, alternativa, correta)`**: Esta é a função central do quiz. Ela é responsável por:
    * Exibir a pergunta e suas alternativas de forma clara.
    * Receber a entrada do usuário.
    * Validar se a entrada corresponde a uma das alternativas.
    * Comparar a resposta do usuário com o gabarito e retornar `True` para acerto e `False` para erro.

2.  **Estruturas de Dados**:
    * `perguntas`: Uma lista de strings que armazena o enunciado de cada uma das três questões.
    * `alternativas`: Uma lista de dicionários. Cada dicionário mapeia as letras ('a', 'b', 'c', 'd') ao texto de suas respectivas alternativas.
    * `corretas`: Uma lista que serve como gabarito, contendo a letra da alternativa correta para cada questão.

3.  **Loop Principal**: Um laço `for` que itera sobre todas as questões, invocando a função `fazer_pergunta` para cada uma e fornecendo feedback imediato ao usuário (se acertou ou errou).

## 🚀 Como Executar o Projeto

Para interagir com o quiz, é necessário ter o **Python 3** instalado no sistema.

1.  Salve o código em um arquivo chamado `projetofinal.py`.
2.  Abra um terminal (ou Prompt de Comando, PowerShell, etc.).
3.  Navegue até o diretório onde você salvou o arquivo.
4.  Execute o script com o seguinte comando:
    ```bash
    python projetofinal.py
    ```
5.  O programa será iniciado, e a primeira pergunta aparecerá no terminal. Leia o enunciado e as alternativas, e então digite a letra correspondente à resposta que julgar correta e pressione Enter.

## 🧠 Análise Matemática das Questões

Cada questão apresenta um desafio de identificar a condição `if` correta para que uma expressão matemática seja calculada sem erros.

### Questão 1
* **Expressão**: `(math.log((x+5)/(y-2)))**0.5`
* **Análise**:
    1.  **Divisão**: O denominador `(y - 2)` não pode ser zero. Portanto, $y \ne 2$.
    2.  **Logaritmo**: O argumento do logaritmo, `(x+5)/(y-2)`, deve ser estritamente positivo. Assim, $(x+5)/(y-2) > 0$.
    3.  **Raiz Quadrada**: O resultado de `math.log((x+5)/(y-2))` (base da potência `**0.5`) deve ser um número não negativo.
* **Conclusão**: A alternativa correta (`b`) simplifica as condições, focando nas restrições mais críticas que impedem o cálculo inicial.

### Questão 2
* **Expressão**: `(e**((9 - (x**2))**0.5)) / math.log(y + 3)`
* **Análise**:
    1.  **Raiz Quadrada**: O radicando `(9 - (x**2))` não pode ser negativo. Portanto, $9 - x^2 \ge 0$, o que implica $-3 \le x \le 3$.
    2.  **Logaritmo**: O argumento `(y + 3)` deve ser estritamente positivo. Portanto, $y + 3 > 0$, ou $y > -3$.
    3.  **Divisão**: O denominador `math.log(y + 3)` não pode ser zero. Isso acontece quando o argumento do logaritmo é 1. Portanto, $y + 3 \ne 1$, o que significa $y \ne -2$.
* **Conclusão**: A alternativa correta (`d`) combina todas essas condições de forma precisa.

### Questão 3
* **Expressão**: `((16 - ((x - 1)**2)) / ((y**2) + 1))**0.5`
* **Análise**:
    1.  **Divisão**: O denominador `(y**2) + 1` é sempre positivo para qualquer valor real de `y`, pois $y^2 \ge 0$, o que garante $(y^2) + 1 \ge 1$. Portanto, não há risco de divisão por zero.
    2.  **Raiz Quadrada**: A fração inteira deve ser não negativa. Como o denominador é sempre positivo, basta que o numerador seja não negativo. Portanto, $16 - (x - 1)^2 \ge 0$.
* **Conclusão**: A alternativa correta (`a`) reflete essa análise, garantindo que a base da raiz quadrada não seja negativa.
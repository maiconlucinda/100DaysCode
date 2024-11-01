
# Qual é o problema a ser resolvido?
    # Criar o jogo Hangman - Um jogo no qual o usuário tem que acertar a palavra definida pelo jogo, o usuário envia a letras que podem estar na palavra, quando ele erra, ele perde uma de suas vidas.

# O que o programa precisa fazer de maneira geral?
    # Definir uma palavra de maneira aleatória, obter inputs do usuário e testar se aquelas letras existem na palavra escolhida, validar a questão da quantidade de vidas que o usuário tem.

# Quais são as etapas que compoem esse objetivo?
    # 01 - Criar uma lista de palavras
    # 02 - Escolher uma dessas palavras aleatoriamente
    # 03 - Criar uma lista na qual cada letra da palavra escolhida, será uma posição nessa lista
    # 04 - Validar se a letra escolhida corresponde a alguma letra da palavra escolhida
    # 05 - Caso seja, atualiza a lista com a letra na posição correta.
    # 06 - Valide a quantidade de vidas que o usuário tem.


import random 

list_of_words = ["carro", "moto", "bicicleta", "trem", "onibus", "aviao", "helicoptero", "caminhao", "carreta", "submarino"]
chosen_word = random.choice(list_of_words)
word_length = len(chosen_word)


display = ["_"] * word_length

guess = input("Insira a letra desejada: ").lower()

while "_" in display:

    guess = input("Insira a letra desejada: ").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(display)

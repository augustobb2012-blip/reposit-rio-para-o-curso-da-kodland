print("olá muito prazer")

nome = input("Qual seu nome? ")

meme_dict = {
    "STALKEAR": "Investigar a vida de alguém online",
    "CRINGE": "Algo vergonhoso ou constrangedor",
    "VDD": "Abreviação da palavra verdade",
    "BISCOITAR": "Postar algo apenas para chamar a atenção",
    "HATER": "Pessoa que está constantemente criticando os outros",
    "VLW": "Abreviação da palavra valeu",
    "NOOB": "Novato, iniciante ou inexperiente em jogos online",
    "TANKAR": "Suportar/aguentar algo",
}

word = input(nome + ", bem-vindo! Digite uma palavra moderna que você não entende (em MAIÚSCULO): ")

if word in meme_dict:
    print(meme_dict[word])
else:
    print("Ainda não temos essa palavra no nosso dicionário")

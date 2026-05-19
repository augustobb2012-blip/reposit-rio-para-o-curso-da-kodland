from flask import Flask
import random

app = Flask(__name__)

facts_list = ["Elon Musk afirma que as redes sociais são projetadas para nos manter dentro da plataforma, para que passemos o máximo de tempo possível visualizando conteúdo.",            
              "De acordo com um estudo realizado em 2018, mais de 50% das pessoas entre 18 e 34 anos se consideram dependentes de seus smartphones.", 
              "As redes sociais têm seus pontos positivos e negativos, e devemos estar conscientes de ambos ao utilizá-las.", 
              "O estudo da dependência tecnológica é uma das áreas mais relevantes da pesquisa científica moderna."]

@app.route("/") 
def home(): 
    return '''
    <h1>Dependência Tecnológica</h1>
    <p>A tecnologia faz parte do nosso dia a dia, mas o uso excessivo pode causar dependência.</p>

    <a href="/random_fact">Veja um fato aleatório!</a><br><br>

    <a href="/coin">Jogo cara ou coroa </a>
    '''

@app.route("/random_fact")
def fatos():
    return f'<p>{random.choice(facts_list)}</p>'

@app.route("/coin")
def coin():
    return f'<h2>{random.choice(["Cara", "Coroa"])}</h2>'

if __name__ == "__main__":
    app.run(debug=True)
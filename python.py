# A very simple Flask Hello World app for you to get started with...
import sqlite3
#import MySQLdb
from flask import jsonify
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return'''<!DOCTYPE html>
<html>
<head>
<META HTTP-EQUIV="refresh" CONTENT="15">
<title>Industria 4.0</title>

  <style type="text/css">
  body {
    padding-left: 11em;
    font-family: Georgia, "Times New Roman",
          Times, serif;
    color: black;
    background-color: #ade1ff; }
  ul.navbar {
    list-style-type: none;
    padding: 0;
    margin: 0;
    position: absolute;
    top: 2em;
    left: 1em;
    width: 9em }
  h1 {
    font-family: Helvetica, Geneva, Arial,
          SunSans-Regular, sans-serif }
  ul.navbar li {
    background: white;
    margin: 0.5em 0;
    padding: 0.3em;
    border-right: 1em solid black }
  ul.navbar a {
    text-decoration: black }
  a:link {
    color: blue }
  a:visited {
    color: blue }
  address {
    margin-top: 36em;
    padding-top: 1em;
    border-top: thin dotted }
  </style>
</head>
	<body>

<!-- Menu de navegacao do site -->
<ul class="navbar">
    <li><a href="http://comunicacaoindustrial.pythonanywhere.com/mostra">Mostrar Dados</a>
    <li><a href="http://comunicacaoindustrial.pythonanywhere.com/post">POST</a>
    <li><a href="http://comunicacaoindustrial.pythonanywhere.com/reload">Reload Data Base</a>
</ul>

<!-- Conteudo -->
<h1>Comunica��o Industrial</h1>

<p>Bem vindos � comunica��o industrial web!

<p>Nesta pagina voc� ver� a comunica��o feita entre dois rob�s, e
como poder� ser o gerenciamento de uma industria em um futuro pr�ximo.
Ela cont�m links que o ajudar�o.

<p>Basta seguir o palestrante :).

<!-- Date e assine sua p�gina, isto � educado! -->
<address>Construida em 10 de outubro de 2017<br>
</address>

</body>'''



@app.route('/reload', methods=['POST','GET'])
def criarbd():

    conn = sqlite3.connect('BANCO.db')
    cursor = conn.cursor()

    cursor.execute ("""
        CREATE TABLE PECAS (

        quantidade VARCHAR(9) NOT NULL,
        circulos VARCHAR(9) NOT NULL
        );""")

    cursor.execute("""
        INSERT INTO PECAS (quantidade,circulos)
        VALUES (?,?)
        """, ('1','2'))


    cursor.execute ("""
        CREATE TABLE PECAS1 (

        quadrados VARCHAR(9) NOT NULL,
        triangulos VARCHAR(9) NOT NULL
        );""")

    cursor.execute("""
        INSERT INTO PECAS1 (quadrados,triangulos)
        VALUES (?,?)
        """, ('3','4'))

    conn.commit()
    conn.close()


@app.route('/post', methods=['POST','GET'])
def upar():
        if request.method =='POST':

            if not request.json:
                return jsonify( {
                    "status": "sem json"
                })

            conn = sqlite3.connect('BANCO.db')
            cursor = conn.cursor()

            data = request.get_json()

            quantidade = data['quantidade']
            circulos = data['circulos']
            quadrados = data['quadrados']
            triangulos = data['triangulos']

            cursor.execute("""
            UPDATE PECAS
            SET quantidade = ?, circulos = ?;
                    """, (quantidade, circulos))

            conn.commit()

            cursor.execute("""
            UPDATE PECAS1
            SET quadrados = ?, triangulos = ?;
            """, (quadrados, triangulos))


            conn.commit()
            conn.close()

            return jsonify( {
                "status": "O mundo � bonito"
            })

        else:
            return jsonify( {
                "status": "erro"
            })

@app.route('/mostra', methods=['GET'])
def mostra_dados():

    conn = sqlite3.connect('BANCO.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM PECAS;")


    dados = {}
    for linhas in cursor.fetchall():
        dados["quantidade"] = linhas[0]
        dados["circulos"] = linhas[1]


    cursor.execute("SELECT * FROM PECAS1;")

    for linhas in cursor.fetchall():
        dados["quadrados"] = linhas[0]
        dados["triangulos"] = linhas[0]

    conn.close()

    pagina = """<!DOCTYPE html>
            <html>
                <head>
                    <title>Dados</title>
                </head>
                <body>
                    <h3>Quantidade   {0}</h3>
                    <h3>Circulos     {1}</h3>
                    <h3>Quadrados    {2}</h3>
                    <h3>Triangulos   {3}</h3>

                </body>
            </html>
         """.format(dados["quantidade"],dados["circulos"], dados["quadrados"], dados["triangulos"])

    return  pagina




'''@app.route('/allan')
def sucesso():

    conn = sqlite3.connect("ComunicacaoIndustrial.mysql.pythonanywhere-services.com", "ComunicacaoIndus", "allanlixo", "ComunicacaoIndus$Data_base")

    c = conn.cursor()

    c.execute("SELECT * FROM dados")

    rows = c.fetchall()
    for eachRow in rows:
        print (eachRow)'''


'''@app.route('/teste2')
def teste2():
    conn = sqlite3.connect('allan1.db')
    cursor = conn.cursor()
    #lendo os dados
    cursor.execute("""
    SELECT *
      FROM estoque2;
    """)

    retorno = []
    for linha in cursor.fetchall():
        retorno.append(linha)
    conn.close()

    return str(retorno)'''
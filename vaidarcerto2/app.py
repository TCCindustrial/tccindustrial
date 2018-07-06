from flask import Flask, render_template, redirect, request, jsonify
app = Flask(__name__)

@app.route('/')
def index():
	return  render_template('index.html')

@app.route('/login')
def login():
	return  render_template('Login_page.html')

@app.route('/compras')
def Compras():
	return  render_template('Compras.html')

@app.route('/home')
def return_index():
   return redirect('/')

@app.route('/variaveis')
def variaveis():
	return  render_template('variaveis.html')







if __name__ == '__main__':
	app.run()


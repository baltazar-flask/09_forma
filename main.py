from flask import Flask, render_template, redirect, request
from flask_bootstrap import Bootstrap
import json

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    text = 'ovo je početna stranica!'
    return render_template('index.html',text=text)

@app.route('/forma', methods=['get', 'post'])
def forma():

    gosti=['C#','Java','JavaScript','Python']

    data=[]
    
    with open('data.json',mode='r',encoding='utf-8') as json_datoteka:
        data=json.load(json_datoteka)
        json_datoteka.close()

    if request.method == 'POST':
       
        ucenik=request.form['ucenik']
        programski_jezik=request.form['programski_jezik']
        redni_broj=len(data)+1     

        with open('data.json',mode='w',encoding='utf-8') as json_datoteka:
            data.append({"redni_broj": redni_broj, "ucenik": ucenik, "programski_jezik": programski_jezik})        
            json.dump(data,json_datoteka)
            json_datoteka.close()

            return redirect("/podaci")
    
    if len(data)==0:
        redni_broj=1
    else:
        redni_broj=len(data)+1    
  
    return render_template('form.html',redni_broj=redni_broj,gosti=gosti)

@app.route('/podaci', methods=['get', 'post'])
def podaci():

    with open('data.json',mode='r',encoding='utf-8') as json_datoteka:
        data = json.load(json_datoteka)
        json_datoteka.close()
        print(data)
    
    for i in range(len(data)):
        print(data[i]['ucenik'])
   
    return render_template('data.html',data=data)

# Error pages
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

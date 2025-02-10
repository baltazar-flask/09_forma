from flask import Flask, render_template, redirect, request
from flask_bootstrap import Bootstrap
import json
import os

app = Flask(__name__)
bootstrap = Bootstrap(app)

def open_json():
    # Provjera da li datoteka postoji
    if not os.path.exists('data.json'):
    # Kreiranje prazne liste ako datoteka ne postoji
        data = []   
        with open('data.json', 'w', encoding='utf-8') as json_datoteka:
            json.dump(data, json_datoteka)
    else:
        with open('data.json',mode='r',encoding='utf-8') as json_datoteka:
            data=json.load(json_datoteka)            
    return data

@app.route('/')
def index():
    text = 'ovo je početna stranica!'
    return render_template('index.html',text=text)

@app.route('/forma', methods=['get', 'post'])
def form():

    programski_jezici=['C#','Java','JavaScript','Python'] 

    # Otvaram postojeći JSON da bih dodao na kraj novi zapis
    # I da bih dobio novi redni broj novog zapisa
    data=open_json()

    if request.method == 'POST':
       
        ucenik=request.form['ucenik']
        programski_jezik=request.form['programski_jezik']
        redni_broj=len(data)+1          

        with open('data.json',mode='w',encoding='utf-8') as json_datoteka:
            data.append({"redni_broj": redni_broj, "ucenik": ucenik, "programski_jezik": programski_jezik})        
            json.dump(data,json_datoteka)          

            return redirect("/podaci")
    
    if len(data)==0:
        redni_broj=1
    else:
        redni_broj=len(data)+1    
  
    return render_template('form.html',redni_broj=redni_broj,programski_jezici=programski_jezici)

@app.route('/podaci', methods=['get', 'post'])
def podaci():

    data=open_json()
    #print(data)'''
    
    '''for i in range(len(data)):
        print(data[i]['ucenik'])'''
   
    return render_template('data.html',data=data)

# Error pages
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

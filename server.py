from flask import Flask, request, render_template, redirect
import json
import requests

app = Flask(__name__)

@app.route('/firstrequest', methods=['GET'])
def firstRequest():
    return(render_template('index.html'))

@app.route('/secondrequest', methods=['GET'])
def secondRequest():
    userAgent = str(request.headers['User-Agent'])
    return(render_template('start.html', userAgent = userAgent))

@app.route('/fourthrequest', methods=['GET'])
def fourthRequest():
    API_KEY = '243903e61d82bc31cb61d6d1bd8b70a3'
    city = request.args.get('q')
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    response = requests.get(url)
    #data = response.content
    #temperature = response.content('main')
    temperature = response.json()
    weather = temperature['weather'][0]['description']
    return weather

@app.route('/thirdrequest', methods=['GET', 'POST'])
def thirdRequest():
    reqData = request.form
    return('You just posted.... ' + str(reqData))

@app.route('/fifthrequest', methods=['GET'])
def fifthRequest():
    return redirect("https://kids.nationalgeographic.com/animals/", code=302)

@app.route('/form-example', methods=['GET', 'POST'])
def form_example():
    return '''<form method="POST">
                Language: <input type="text" name="language"><br>
                Framework: <input type="text" name="framework"><br>
                <input type= "submit" value="Submit"><br>
            </form>'''

if __name__ == '__main__':
    app.run(debug=True )

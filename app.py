from flask import Flask,render_template

app = Flask(__name__)

app.debug = True
mymodel ='Amir'
@app.route('/')
def index():
  return render_template('index.html',model=mymodel)

@app.route('/result')
def result():
    return render_template('result.html')

if __name__=='__name__':
    app.run()

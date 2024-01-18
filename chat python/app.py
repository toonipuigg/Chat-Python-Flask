from flask import Flask

app = Flask(__name__)

@app.route('/')
def Index():
    return "<h2>Pedro Maricona</h2>"

if __name__ == '__main__':
    
    #Ejecución en el puerto 3000
    #Con el debug se refrescan los cambios que se hagan
    app.run(port=3000, debug=True)

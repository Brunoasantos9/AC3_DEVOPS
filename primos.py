from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def print_primos():
    qtdtotal = 100
    primos = '1,2'
    candprimo = 3
    qtdencontrados = 2
    ehprimo = 1
    
    while qtdencontrados < qtdtotal:
        for i in range (2, candprimo):
            if candprimo % i == 0:
                ehprimo = 0
                break
        if ehprimo == 1:
            primos = primos + ',' + str(candprimo)
            qtdencontrados += 1
            if qtdencontrados % 20 == 0:
                primos += "<br>" 
        
        ehprimo = 1   
        candprimo += 1
    
    return primos


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

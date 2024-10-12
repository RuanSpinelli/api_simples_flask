#importando coisas relacionadas ao Flask, ao jsonify(para criar jsons) e ao request para que os endpoints recebam informação
from flask import Flask, jsonify, request
#importando json para facilitar a leitura de arquivos json
import json 
"""
"""

#jsonify: serve para transformar dicionarios em jsons

app = Flask(__name__)

@app.route("/<int:id>")
def pessoa(id):
    return jsonify({'id': id, 'nome': 'Rafael', 'profissao': 'desenvolvedor'})



"""
@app.route("/soma/<int:valor1>/<int:valor2>",methods=["GET"])
def soma(valor1, valor2):
    return jsonify({"soma": valor1+valor2}) 

"""


@app.route("/soma",methods=["POST","GET"])
def soma():
    #O IF e ELSE abaixo serve para checar o método que está sendo usado para acessar o endpoint
    
    if request.method == "POST":
        dados = json.loads(request.data)
        print(dados)

        total = sum(dados['valores'])
    elif request.method == "GET": 
        total = 10 + 10

    return jsonify({"soma": total})

if __name__ == "__main__":
    app.run(debug=True)


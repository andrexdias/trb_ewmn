from flask import Flask, request, jsonify, send_from_directory
from conversor import converter
from op_ar import soma, subtracao
from tabela_gray import gray_code
import os

app = Flask(__name__, static_folder="../frontend", static_url_path="")

@app.route('/')
def serve_frontend():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def serve_static_files(path):
    return send_from_directory(app.static_folder, path)

@app.route('/api/convert', methods=['POST'])
def convert():
    data = request.json
    numero = int(data['numero'])
    base_origem = int(data['base_origem'])
    base_destino = int(data['base_destino'])
    resultado = converter(numero, base_origem, base_destino)
    return jsonify({'resultado': resultado})

@app.route('/api/arithmetic', methods=['POST'])
def arithmetic():
    data = request.json
    num1 = data['num1']
    num2 = data['num2']
    operacao = data['operacao']
    base_final = int(data['base_final'])
    if operacao == 'soma':
        resultado = soma(num1, num2, base_final)
    elif operacao == 'subtracao':
        resultado = subtracao(num1, num2, base_final)
    else:
        return jsonify({'erro': 'Operação não suportada'}), 400
    return jsonify({'resultado': resultado})

@app.route('/api/gray', methods=['POST'])
def gray():
    data = request.json
    n_bits = int(data['n_bits'])
    resultado = gray_code(n_bits)
    return jsonify({'resultado': resultado})

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/api/saque', methods=['POST'])
def saque():
    
    
    data = request.get_json()
    print(data)

    if not data or 'valor' not in data:
        return jsonify({'error': 'Nenhum valor fornecido'}), 400
    
    #elif not valor.is_integer(): 
    #   return jsonify({'error': 'Valor digitado não é um número inteiro'}), 400

    valor = data['valor']
    #print(f"Valor recebido: {valor}")
    nota100, nota50, nota20, nota10, nota5, nota2 = 0, 0, 0, 0, 0, 0 

    i = valor

    while i >= 2:
            if i >= 100:
                nota100 = i//100
                i = i - (nota100 * 100)  
            elif i >= 50: 
                nota50 = i // 50
                i = i - (nota50 * 50)  
            elif i >= 20:
                nota20 = i // 20
                i = i - (nota20 * 20) 
            elif i >= 10:
                nota10 = i // 10
                i = i - (nota10 * 10) 
            elif i >= 5:
                nota5 = i // 5
                i = i - (nota5 * 5) 
            elif i >= 2:
                nota2 = i // 2
                i = i - (nota2 * 2)
            else:
                break 
 
    response = {
    "100": nota100,
    "50": nota50,
    "20": nota20,
    "10": nota10,
    "5": nota5,
    "2": nota2
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)

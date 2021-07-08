from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/req', methods=['POST'])
def req():
    nueva_accion = {
        "comando": request.json['comando'],
        "producto_kg": request.json['producto_kg'],
        "lote": request.json['lote']
    }
    print(nueva_accion)
    return jsonify(nueva_accion)


if __name__ == '__main__':
    app.run(debug=True)

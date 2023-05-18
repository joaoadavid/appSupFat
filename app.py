from flask import Flask, jsonify

app = Flask(__name__)

def calcular_fatorial(numero, resultado=1):
    if numero == 0 or numero == 1:
        return resultado
    else:
        return calcular_fatorial(numero - 1, resultado * numero)

def calcular_super_fatorial(numero):
    if numero < 0:
        return jsonify({'error': 'O número deve ser não negativo'})

    fatoriais = {}
    super_fatorial = 1
    for i in range(1, numero + 1):
        if i not in fatoriais:
            fatoriais[i] = calcular_fatorial(i)
        super_fatorial *= fatoriais[i]
    return super_fatorial

@app.route('/super_fatorial/<int:numero>')
def calcular_super_fatorial_rota(numero):
    resultado = calcular_super_fatorial(numero)
    return jsonify({' O numero e ': numero, ' e sua versao super fatorial': resultado})

if __name__ == '__main__':
    app.run(debug=True)


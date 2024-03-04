from flask import Flask, jsonify, request

app = Flask(__name__)

# lista com valores iniciais 
musicas = [
    {
        'song': 'Uma canção para a Lua',
        'type': 'romantic'
    },
    {
        'song': 'Nuvens',
        'type': 'rock'
    },
    {
        'song': 'Cidade velha',
        'type': 'rap'
    }
]

print(musicas[2])
# rota padrão - GET http
@app.route('/')
def get_songs():
    return jsonify(musicas)

# Busca um item com base no indice, que é passado na url
@app.route('/song/<int:indice>', methods=['GET'])
def get_song_with_indice(indice):
    return jsonify(musicas[indice])

# adiciona um novo item a lista
@app.route('/song', methods=['POST'])
def new_song():
    musica = request.get_json()
    musicas.append(musica)

    return jsonify(musica, 200)

@app.route('/song/<int:indice>', methods=['PUT'])
def change_song_information(indice):
    musica = request.get_json()
    musicas[indice].update(musica)

    return jsonify(musicas[indice], 200)

# deletar uma musica da lista
@app.route('/song/<int:indice>', methods=['DELETE'])
def delete_song(indice):
    try:
        if musicas[indice] is not None:
            del musicas[indice]
            return jsonify(f'Musica excluida', 200)
    except:
        return jsonify('Não foi possível encontrar a musica para excluir', 404)


# responsavel pela configuração do servidor
# necessário para iniciar a API
app.run(port=5000, host='localhost', debug=True)


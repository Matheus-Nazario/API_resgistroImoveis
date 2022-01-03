from flask import Flask, request
from flask_restful import Resource, Api
from caracteristica import Caracteristica
import json

app = Flask(__name__)
api = Api(app)


alug_imoveis = [
    {
        'id':'0',
        'imovel':'casa',
        'características':['estacionamento', 'pscina']
    },
    {
        'id':1,
        'imovel':'apartamento',
        'características':['estacionamento', 'academia']
    }
]


# devolve um desenvolvedor pelo ID, também altera e deleta um desenvolvedor
class Imoveis(Resource):
    def get(self, id):
        try:
            response = alug_imoveis[id]
        except IndexError:
            mensagem = 'O ID {} não existe'.format(id)
            response = {'status':'erro', 'mensagem':mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status':'erro', 'mensagem':mensagem}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        alug_imoveis[id] = dados
        return dados

    def delete(self, id):
        alug_imoveis.pop(id)
        return {'status':'sucesso', 'mensagem':'Registro excluído'}

# Lista todos os desenvolvedor e permite registrar um novo desenvolvedor
class ListaImoveis(Resource):
    def get(self):
        return alug_imoveis

    def post(self):
        dados = json.loads(request.data)
        posicao = len(alug_imoveis)
        dados['id'] = posicao
        alug_imoveis.append(dados)
        return alug_imoveis[posicao]

api.add_resource(Imoveis, '/dev/<int:id>/')
api.add_resource(ListaImoveis, '/dev/')
api.add_resource(Caracteristica, '/caracteristica/')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, jsonify
import re
import requests

app = Flask(__name__)

def gerar_sugestoes(nome):
    nome_base = re.sub(r'[^a-zA-Z0-9]', '', nome.lower())
    return [
        f"{nome_base}.com.br",
        f"{nome_base}contabil.com.br",
        f"{nome_base}online.com.br",
        f"{nome_base}consultoria.com.br",
        f"{nome_base}servicos.com.br"
    ]

def verificar_disponibilidade(dominio):
    url = f"https://rdap.registro.br/domain/{dominio}"
    response = requests.get(url)
    return response.status_code == 404

@app.route("/sugerir-dominios", methods=["POST"])
def verificar_dominios():
    dados = request.get_json()
    nome = dados.get("nome_empresa")

    if not nome:
        return jsonify({"erro": "Campo 'nome_empresa' é obrigatório"}), 400

    sugestoes = gerar_sugestoes(nome)
    disponiveis = [dom for dom in sugestoes if verificar_disponibilidade(dom)]
    return jsonify({"dominios_disponiveis": disponiveis[:3]})

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

# API - Sugerir Domínios .com.br

Esta API recebe o nome de uma empresa e retorna até 3 sugestões de domínio .com.br disponíveis.

### ▶️ Como rodar localmente

```bash
pip install -r requirements.txt
python app.py
```

Acesse em: http://localhost:10000/sugerir-dominios

### 🌐 Como publicar no Render

1. Crie um repositório no GitHub com esses arquivos
2. Vá em https://render.com → "New Web Service"
3. Configure:
   - Build command: `pip install -r requirements.txt`
   - Start command: `python app.py`

A API estará acessível via HTTPS com a rota `/sugerir-dominios`.

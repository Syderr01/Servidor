import http.server
import socketserver

# Porta onde o servidor será executado 
PORT = 8000

# Diretório onde está o arquivo HTML
DIRECTORY = "."

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

# Configura o servidor
with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print(f"Servidor rodando no endereço: http://localhost:{PORT}")
    print(f"Servindo arquivos do diretório: {DIRECTORY}")
    httpd.serve_forever()


# Servidor Local em Python para Arquivos HTML

Este documento explica como funciona o script que cria um servidor HTTP local para servir arquivos HTML (ou outros) através de um navegador usando Python.

---

## **1. Objetivo do Script**
O objetivo do script é criar um servidor HTTP básico que:
- Roda localmente na máquina.
- Serve arquivos armazenados em um diretório específico.
- Permite visualizar arquivos HTML e recursos relacionados (CSS, JS, imagens) no navegador.

---

## **2. Descrição do Código**

### **Importações**
```python
import http.server
import socketserver
```
- **`http.server`**: Módulo embutido no Python que fornece classes para implementar servidores HTTP simples.
- **`socketserver`**: Módulo usado para configurar e gerenciar conexões TCP.

### **Configuração da Porta**
```python
PORT = 8000
```
Define a porta onde o servidor será executado. O navegador pode acessar o servidor em `http://localhost:8000`. Você pode alterar para outra porta (por exemplo, 8080).

### **Configuração do Diretório**
```python
DIRECTORY = "."
```
Define o diretório onde os arquivos serão servidos. O valor `"."` indica o diretório atual onde o script está sendo executado.

### **Classe CustomHandler**
```python
class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
```
- A classe `CustomHandler` herda da `SimpleHTTPRequestHandler`.
- Adiciona a capacidade de definir um diretório personalizado (`DIRECTORY`) para servir arquivos.

### **Configuração e Execução do Servidor**
```python
with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print(f"Servidor rodando no endereço: http://localhost:{PORT}")
    print(f"Servindo arquivos do diretório: {DIRECTORY}")
    httpd.serve_forever()
```
- Cria uma instância do servidor TCP que escuta na porta especificada.
- Associa o manipulador de solicitações (`CustomHandler`) ao servidor.
- Exibe mensagens no terminal com informações sobre o servidor.
- Chama o método `serve_forever()` para manter o servidor ativo até ser interrompido.

---

## **3. Como Usar o Script**

1. **Preparar o Ambiente**
   - Salve o script como `servidor.py`.
   - Coloque o arquivo HTML (e recursos relacionados) no diretório onde o script será executado ou configure a variável `DIRECTORY` com o caminho desejado.

2. **Executar o Servidor**
   - Execute o script no terminal:
     ```bash
     python servidor.py
     ```

3. **Acessar o Servidor**
   - Abra o navegador e acesse:
     ```
     http://localhost:8000
     ```
   - Os arquivos do diretório configurado serão exibidos. O arquivo `index.html` será carregado automaticamente (se existir).

4. **Encerrar o Servidor**
   - Pressione `Ctrl+C` no terminal para encerrar o servidor.

---

## **4. Limitações**
- O servidor não é seguro e não deve ser usado em ambientes de produção.
- Ele é ideal apenas para desenvolvimento e testes locais.

---

## **6. Conclusão**
Este script é uma solução simples e eficiente para criar um servidor local para visualizar arquivos HTML. Ele aproveita bibliotecas padrão do Python e é fácil de configurar e usar, tornando-o ideal para desenvolvedores que precisam de um servidor rápido para testes.

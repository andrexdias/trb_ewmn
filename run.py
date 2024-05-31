import subprocess
import sys
import webbrowser

# Verifique se o script está sendo executado no ambiente virtual correto
if sys.prefix == sys.base_prefix:
    raise EnvironmentError("Por favor, ative o ambiente virtual antes de executar este script.")

# Iniciar o servidor Flask
subprocess.Popen(["python", "backend/app.py"])

# Abrir o navegador web
webbrowser.open("http://localhost:5000")

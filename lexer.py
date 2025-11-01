# ------------------------------------------------------------ 
# lexer.py
# Analizador Léxico usando PLY
# ------------------------------------------------------------
# Integrantes:
#   👤 Derian Baque Choez (fernan0502)
#   
# ------------------------------------------------------------
import ply.lex as lex
import datetime
import os
import subprocess

# ------------------------------------------------------------
# 1 Definición de los tokens 
# ------------------------------------------------------------
tokens = [
    # ---------------- Aporte Derian ----------------
    'IDENTIFICADOR',
    'NUMERO',
    'CADENA',
    'ASIGNACION',
    'SUMA',
    'RESTA',
    'MULT',]
    # ---------------- Fin Derian -------------------
reservadas = {
    # -------- Aporte Derian --------
    'if': 'IF',
    'else': 'ELSE',
    'for': 'FOR',
    'while': 'WHILE',
    'fn': 'FUNCTION',}

tokens = tokens + list(reservadas.values())

# ------------------------------------------------------------
# 2 Expresiones regulares para tokens simples
# ------------------------------------------------------------
# -------- Aporte Derian --------
t_ASIGNACION = r'='
t_SUMA       = r'\+'
t_RESTA      = r'-'
t_MULT       = r'\*'
# -------- Fin Derian --------

# ------------------------------------------------------------
# 3 Reglas con acciones
# ------------------------------------------------------------
# -------- Aporte Derian --------
def t_IDENTIFICADOR(t):
    r'[a-zA-ZáéíóúÁÉÍÓÚñÑ_][a-zA-Z0-9áéíóúÁÉÍÓÚñÑ_]*'
    t.type = reservadas.get(t.value, 'IDENTIFICADOR')
    return t

def t_NUMERO(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

def t_CADENA(t):
    r'\"([^\\\n]|(\\.))*?\"'
    return t
# -------- Fin Derian --------

# ------------------------------------------------------------
# 4 Función para obtener el usuario de Git automáticamente
# ------------------------------------------------------------
def get_git_user():
    try:
        name = subprocess.check_output(["git", "config", "user.name"], encoding="utf-8").strip()
        if name:
            return name
    except:
        pass
    # fallback si no hay user.name configurado
    return os.getenv("USER") or os.getenv("USERNAME") or "usuarioGit"

# ------------------------------------------------------------
# 5 Función para guardar logs
# ------------------------------------------------------------
def log_token(mensaje):
    usuario = get_git_user()  # obtiene automáticamente el usuario de Git
    fecha_hora = datetime.datetime.now().strftime("%d-%m-%Y-%Hh%M")
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, f"lexico-{usuario}-{fecha_hora}.txt")
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(mensaje + "\n")

# ------------------------------------------------------------
# 6 Construcción del lexer
# ------------------------------------------------------------
lexer = lex.lex()

# ------------------------------------------------------------
# 7 Ejecución manual del analizador
# ------------------------------------------------------------
if __name__ == "__main__":
    print("Analizador léxico iniciado.\n")
    archivo = input("Ingrese la ruta del archivo a analizar: ").strip()

    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            data = f.read()
            lexer.input(data)

            while True:
                tok = lexer.token()
                if not tok:
                    break
                mensaje = f"Línea {tok.lineno}: {tok.type} -> {tok.value}"
                print(mensaje)
                log_token(mensaje)

        print("\n✅ Análisis léxico completado. Revise la carpeta 'logs' para ver el resultado.")

    except FileNotFoundError:
        print("❌ Archivo no encontrado. Verifique la ruta e intente nuevamente.")
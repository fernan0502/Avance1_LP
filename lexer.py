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
# Definición de los tokens 
# ------------------------------------------------------------
tokens = [
    # ---------------- Aporte Derian ----------------
    'IDENTIFICADOR', 'NUMERO', 'CADENA',
    'ASIGNACION', 'SUMA', 'RESTA', 'MULT', 'DIV',
    'PAREN_IZQ', 'PAREN_DER', 'LLAVE_IZQ', 'LLAVE_DER',
    'PUNTOCOMA', 'PUNTO', 'MODULO', 'POTENCIA',
    'MENOR', 'COMA', 'DOSPUNTOS']
    # ---------------- Fin Derian -------------------
reservadas = {
    # -------- Aporte Derian --------
    'if': 'IF', 'else': 'ELSE', 'for': 'FOR', 'while': 'WHILE',
    'fn': 'FUNCTION', 'return': 'RETURN', 'let': 'VAR',
    'const': 'CONST', 'true': 'TRUE', 'false': 'FALSE',
    'break': 'BREAK', 'print': 'PRINT'}

tokens = tokens + list(reservadas.values())

# ------------------------------------------------------------
# Expresiones regulares para tokens simples
# ------------------------------------------------------------
# -------- Aporte Derian --------
t_ASIGNACION = r'='
t_SUMA       = r'\+'
t_RESTA      = r'-'
t_MULT       = r'\*'
t_DIV        = r'/'
t_PAREN_IZQ  = r'\('
t_PAREN_DER  = r'\)'
t_LLAVE_IZQ  = r'\{'
t_LLAVE_DER  = r'\}'
t_PUNTOCOMA  = r';'
t_PUNTO      = r'\.'
t_MODULO     = r'%'
t_POTENCIA   = r'\^'
t_MENOR      = r'<'
t_COMA       = r','
t_DOSPUNTOS  = r':'
# -------- Fin Derian --------

# ------------------------------------------------------------
# Reglas con acciones
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

def t_COMENTARIO_LINEA(t):
    r'//.*'
    pass

def t_COMENTARIO_BLOQUE(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')
    pass

t_ignore = ' \t'

def t_nueva_linea(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    mensaje = f"❌ Error léxico: carácter no reconocido '{t.value[0]}' en línea {t.lineno}"
    print(mensaje)
    log_token(mensaje)
    t.lexer.skip(1)

# -------- Fin Derian --------

# ------------------------------------------------------------
#  Función para obtener el usuario de Git automáticamente
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
#  Función para guardar logs
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
#  Construcción del lexer
# ------------------------------------------------------------
lexer = lex.lex()

# ------------------------------------------------------------
#  Ejecución manual del analizador
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
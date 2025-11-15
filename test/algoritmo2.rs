// Pruebas de operadores relacionales, lógicos, arrays y caracteres
fn main() {
    // Comparaciones
    if 5 > 3 { }
    if 5 < 3 { }
    if 5 >= 5 { }
    if 3 <= 5 { }
    if 5 == 5 { }
    if 5 != 3 { }

    // Lógicos
    if true && false { }
    if true || false { }
    if !false { }

    // Arrays y matrices
    let numeros = [1, 2, 3, 4, 5];
    let matriz = [[1, 2], [3, 4]];
    // Acceso a elementos
    let _primero = numeros[0];
    let _segundo = matriz[1][0];

    // Caracteres
    let _letra = 'a';
    let _digito = '5';
    let _especial = '\n';
    let _tab = '\t';
    let _comilla = '\'';

    // Rango y rango incluido, con paréntesis, llaves y punto y coma
    for k in (0..5) { }
    for m in (0..=5) { }

    // Closure con flecha y anotaciones (->)
    let _suma = |a: i32, b: i32| -> i32 { a + b };

    // Uso de ?: para tokenizar INTERROGACION y DOSPUNTOS
    let cond = true;
    let _valor = cond ? 10 : 20;

    // Comentarios
    // Comentario de una línea
    /* Comentario de bloque
       en varias líneas */
}
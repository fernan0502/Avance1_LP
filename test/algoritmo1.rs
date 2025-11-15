// Prueba de tokens básicos: literales, asignación y aritmética
fn main() {
    // Comentario de línea
    /* Comentario de bloque */

    let mut x: i32 = 10; // IDENTIFICADOR, ENTERO, ASIGNACION, DOSPUNTOS, PUNTOCOMA
    let y: f64 = 20.5;   // FLOTANTE
    let z: i32 = 3;
    let palabra: &str = "Hola"; // CADENA
    let letra: char = 'a';        // CARACTER
    let verdadero = true;         // BOOLEANO/TRUE
    let falso = false;            // BOOLEANO/FALSE

    // Operadores aritméticos
    let _suma = x + z;    // SUMA
    let _resta = x - z;   // RESTA
    let _mult = x * z;    // MULT
    let _div = x / z;     // DIV
    let _mod = x % z;     // MODULO
    let _pot_o_xor = x ^ z; // POTENCIA o BIT_XO (según precedencia del lexer)

    // Paréntesis, coma, punto y punto y coma
    let _tupla = (x, y, z); // PAREN_IZQ, COMA, PAREN_DER
    let longitud = palabra.len(); // PUNTO

    // Corchetes
    let numeros = [1, 2, 3]; // CORCHETE_IZQ, CORCHETE_DER
    let primero = numeros[0];

    // Rango y rango incluido
    for i in 0..3 { }      // RANGO
    for j in 0..=3 { }     // RANGO_INCLUIDO

    // Dos puntos en anotaciones y uso de ? y : (solo para tokenizar)
    let _otro: i32 = 0;
    let cond = true;
    let ternario = cond ? 1 : 0; // INTERROGACION y DOSPUNTOS

    // Flecha en closures
    let suma_closure = |a: i32, b: i32| -> i32 { a + b }; // FLECHA

    println!("{}", longitud);
}
fn main() {
    if 5 > 3 {
        println!("5 es mayor que 3");
    }
    if 5 < 3 {
        println!("5 es menor que 3");
    }
    if 5 >= 5 {
        println!("5 es mayor o igual que 5");
    }
    if 3 <= 5 {
        println!("3 es menor o igual que 5");
    }
    if 5 == 5 {
        println!("5 es igual a 5");
    }
    if 5 != 3 {
        println!("5 es diferente de 3");
    }
    if 5 && 3 {
        println!("Operador AND");
    }
    if 5 || 3 {
        println!("Operador OR");
    }
    if !false {
        println!("Operador NOT");
    }
    // Prueba de CORCHETE_IZQ y CORCHETE_DER - Arrays
    let numeros = [1, 2, 3, 4, 5];
    let matriz = [[1, 2], [3, 4]];
    let vacio = [];
    
    // Acceso a elementos del array
    let primero = numeros[0];
    let segundo = matriz[1][0];
    
    // Prueba de CARACTER - Caracteres individuales
    let letra = 'a';
    let digito = '5';
    let especial = '\n';
    let tab = '\t';
    let comilla = '\'';
    
    // Prueba de BOOLEANO - Valores booleanos
    let verdadero = true;
    let falso = false;
    
    if true {
        println!("Esto es verdadero");
    }
    
    if false {
        println!("Esto nunca se ejecuta");
    }
    
    // Prueba de FLECHA - Funciones y closures
    let suma = |a, b| -> i32 {
        return a + b;
    };
    
    let multiplica = |x| -> i32 {
        x * 2
    };
    
    fn resta(a: i32, b: i32) -> i32 {
        return a - b;
    }
    
    // Prueba de INTERROGACION - Operador ternario o manejo de errores
    let resultado = if verdadero ? 10 : 20;
    let valor = resultado ? 5 : 0;
    
    // Combinación de todos los tokens
    let array_chars = ['x', 'y', 'z'];
    let es_valido = true;
    


    
}
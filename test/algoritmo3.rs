// Prueba de operadores bit a bit, asignaciones compuestas y palabras reservadas
mod mymod {
	pub struct S;
	pub enum E { A }
}

use crate::mymod::S as Alias;
use self::mymod::E;
use super::mymod as mm;

trait T { fn m(&self); }
impl T for Alias { fn m(&self) {} }

static X: i32 = 0;
const C: i32 = 5;

// async/await y dyn
async fn af() {}

fn main() {
	let mut a: i32 = 1;

	// Operadores bit a bit
	let _b = a & 1;  // BIT_Y
	let _c = a | 2;  // BIT_O
	let _d = a ^ 3;  // POTENCIA/BIT_XO
	let _e = ~a;     // BIT_NO
	let _f = a << 2; // DESPLAZAR_IZQ
	let _g = a >> 1; // DESPLAZAR_DER

	// Asignación compuesta
	a += 2; // MAS_IGUAL
	a -= 3; // MENOS_IGUAL
	a *= 4; // POR_IGUAL
	a /= 5; // DIV_IGUAL
	a %= 2; // MOD_IGUAL
	a &= 1; // Y_IGUAL
	a |= 2; // O_IGUAL
	a ^= 3; // XO_IGUAL
	a <<= 1; // DESP_IZQ_IGUAL
	a >>= 2; // DESP_DER_IGUAL

	// match, loop, while, for, in, break, continue
	match 1 { 1 => {}, _ => {} }
	loop { break; }
	let mut i = 0;
	while i < 2 { i += 1; continue; }
	for j in 0..=2 { let _x = j; }

	// where en funciones genéricas
	fn foo<T>() where T: Sized { }
	foo::<i32>();

	// move/ref/type/unsafe/await/dyn
	let _cl = move |x: i32| x;
	let ref _r = a;
	type MyInt = i32;
	unsafe { let _p = &X as *const i32; }
	let _aw = af();
	// uso de await para tokenizar
	// (no es ejecutable aquí, solo tokenización)
	// _aw.await;
	let _tobj: &dyn T = &Alias;

	// Palabras reservadas adicionales de la otra lista
	let _k = if true { 1 } else { 0 }; // if/else
	let _rtn = (|| -> i32 { return 1; })(); // return y ->
	print("hola"); // PRINT (token reservado)
	input();       // INPUT (token reservado)
}

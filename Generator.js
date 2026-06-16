function* miGenerador() {
    yield "Primer valor";
    yield "Segundo valor";
    return "Fin de la función";
}

const iterador = miGenerador();

console.log(iterador.next()); // { value: "Primer valor", done: false }
console.log(iterador.next()); // { value: "Segundo valor", done: false }
console.log(iterador.next()); // { value: "Fin de la función", done: true }

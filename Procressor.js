const usuario = {
  nombre: "Carlos",
  saludar: function() {
    setTimeout(() => {
      console.log(`Hola, soy ${this.nombre}`);
    }, 1000);
  },
  despedir: function() {
    setTimeout(function() {
      console.log(`Adiós de parte de ${this.nombre}`);
    }, 1000);
  }
};

usuario.saludar();
usuario.despedir();

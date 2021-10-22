boton_buscar_usuario = document.getElementById("buscar_usuario");

boton_buscar_usuario.addEventListener("click", () => {
  input_buscardor = document.getElementById("input_usuario");
  usuario = input_buscardor.value;
  if (input_buscardor.value !== "") {
    window.location.href = "/perfil/" + usuario;
  } else {
    alert("Campo de usuario vacio");
  }
});

boton_cerrar_sesion = document.getElementById("cerrar_sesion");

boton_cerrar_sesion.addEventListener("click", () => {
  //CERRAR SESION
});

boton_agregar_foto = document.querySelector(".boton-agregar-foto");
if (boton_agregar_foto != null) {
  input_imagen = document.getElementById("ingreso_imagen");

  boton_agregar_foto.addEventListener("click", () => {
    input_imagen.click();
  });

  input_imagen.addEventListener("change", async (evt) => {
    let files = evt.target.files;
    let img = files[0];

    var reader = new FileReader();

    reader.onload = async function () {
      const parametros = {
        headers: {
          "content-type": "application/json",
        },
        body: reader.result,
        method: "POST",
      };

      let usuario = window.location.pathname.split("/")[2];

      await fetch(`/insertarImg/${usuario}`, parametros)
        .then((data) => {
          return data.json();
        })
        .then((res) => console.log(res))
        .catch((error) => console.log(error));

      location.reload();
    };

    reader.readAsText(img);
    
  });
}

boton_cerrar_sesion = document.getElementById("cerrar_sesion");

boton_cerrar_sesion.addEventListener("click", () => {
  location.href = "/cerrar_sesion";
});

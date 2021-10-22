btn_regresar = document.querySelector(".regresar span");

btn_regresar.addEventListener("click", () => {
  window.location.href = "/";
});

function icono_mostrar_ocultar_contrasena(btn_vision, id_input_contrasena) {
  btn_vision.addEventListener("click", () => {
    let input_contrasena = document.getElementById(id_input_contrasena);
    let tipo_input = input_contrasena.getAttribute("type");

    if (tipo_input == "password") {
      input_contrasena.setAttribute("type", "text");
      input_contrasena.style.width = "70%";
      btn_vision.setAttribute("src", "static/img/hidden.png");
    } else {
      input_contrasena.setAttribute("type", "password");
      btn_vision.setAttribute("src", "static/img/view.png");
    }
  });
}

btn_vision = document.getElementById("vision_contrasena");
icono_mostrar_ocultar_contrasena(btn_vision, "contrasena");

btn_vision = document.getElementById("vision_confirmar_contrasena");
icono_mostrar_ocultar_contrasena(btn_vision, "confirmar_contrasena");

function validar_formulario_registro() {
  input_usuario = document.getElementById('usuario')
  input_correo = document.getElementById('correo')
  input_contrasena = document.getElementById('contrasena')
  input_confirmar_contrasena = document.getElementById('confirmar_contrasena')

  if (!validar_usuario(input_usuario.value)) {
    alert('El campo usuario no debe contener espacios')
    return false
  }

  if (!validar_correo(input_correo.value)) {
    alert('El correo no es valido')
    return false
  }
  
  if (!validar_contrasena(input_contrasena.value)) {
    alert('La contrasena debe tener minimo 8 caracteres, una letra mayuscula, una letra minuscula y un caracter especial')
    return false
  }

  if (!(input_contrasena.value == input_confirmar_contrasena.value)) {
    alert('Las contrasenas no coinciden')
    return false
  }

  return true
}

function validar_usuario(usuario) {
  if (/^\S*$/i.test(usuario)) {
    return true
  } else {
    return false
  }
}

function validar_correo(correo) {
  if (/^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/i.test(correo)) {
    return true
  } else {
    return false
  }
}

function validar_contrasena(contrasena) {
  if (/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/i.test(contrasena)) {
    return true
  } else {
    return false
  }
}
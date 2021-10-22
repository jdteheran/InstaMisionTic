btn_registrate = document.querySelector('.registro span')

btn_registrate.addEventListener('click', () => {
    window.location.href = "/registro";
})

btn_vision = document.getElementById('vision')

btn_vision.addEventListener('click', () => {
    let input_contrasena = document.getElementById('contrasena')
    let tipo_input = input_contrasena.getAttribute('type')
    if (tipo_input == 'password') {
        input_contrasena.setAttribute('type', 'text')
        input_contrasena.style.width = '70%'
        btn_vision.setAttribute('src', 'static/img/hidden.png')
    } else {
        input_contrasena.setAttribute('type', 'password')
        btn_vision.setAttribute('src', 'static/img/view.png')
    }
})
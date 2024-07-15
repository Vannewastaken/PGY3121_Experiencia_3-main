

// PARA MOSTRAR LA CONTRASEÑA
function togglePasswordVisibility() {
    let passwordInput = document.getElementById("password");
    let checkbox = document.getElementById("showPasswordCheckbox");

    if (checkbox.checked) {
        passwordInput.type = "text";
    } else {
        passwordInput.type = "password";
    }
}

//VALIDAR INICIO DE SESIÓN
const expresion = /^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$/;
function iniciarSesion() {
    let c = document.getElementById('email').value;
    c = c.toLowerCase();
    const validar = expresion.test(c);
    let p = document.getElementById('password').value;

    if (validar == false) {
        alert('El correo electronico no es valido');
        document.getElementById('email').value = "";
        document.getElementById('email').focus();

    }
    else if (p.length < 8) {
        alert('Error..debe ingresar una contraseña válida');
        document.getElementById('password').value = "";
        document.getElementById('password').focus();
    }
    else {
        alert('Has iniciado sesión correctamente...')
    }

}


// LUKAS REGISTRO

function registrarUsuario() {
    let nom = document.getElementById('name').value;
    let usu = document.getElementById('uname').value;
    let em = document.getElementById('email').value;
    let tel = document.getElementById('telefono').value;
    let con = document.getElementById('contraseña').value;
    let concon = document.getElementById('confirmarContraseña').value;

    em = em.toLowerCase();
    const validar = expresion.test(em);


    if (nom.length < 20) {
        alert('Error..debe ingresar el nombre completo');
        document.getElementById('name').value = "";
        document.getElementById('name').focus();
    }
    else if (usu.length < 4) {
        alert('Error..debe ingresar un nombre de usuario mayor a 3 caracteres');
        document.getElementById('uname').value = "";
        document.getElementById('uname').focus();

    }
    else if (validar == false) {
        alert('El correo electronico no es valido');
        document.getElementById('email').value = "";
        document.getElementById('email').focus();

    }
    else if (tel.length < 8) {
        alert('Error..debe ingresar un telefono correcto');
        document.getElementById('telefono').value = "";
        document.getElementById('telefono').focus();
    }
    else if (con.length < 8) {
        alert('Error..debe ingresar una contraseña de 8 caracteres o más');
        document.getElementById('contraseña').value = "";
        document.getElementById('contraseña').focus();
    }
    else if (concon !== con) {
        alert('Error..las contraseñas no coinciden');
        document.getElementById('contraseña').value = "";
        document.getElementById('confirmarContraseña').value = "";
        document.getElementById('contraseña').focus();
    }
    else {
        alert('Te has registrado correctamente!')
    }

}
function MostrarServicios(){
    let url='http://localhost:3300/camiones';
    //implementar Fetch que permita la información de las mascotas
    fetch(url)
    .then(response => response.json())
    .then(data => MostrarProductos(data))
    .catch(error => console.log(error))

    const MostrarProductos=(data)=>{
        console.log(data)
        let texto=""
        for(var i=0;i<data.length;i++){
            texto+=`<tr>
                <td>${data[i].id}</td>
                <td><img style="width:200px;" src="${data[i].img}"></td>
                <td>${data[i].marca}</td>
                <td>${data[i].valorxruta}</td>
                <td>${data[i].capacidad}</td>
                <td>${data[i].ciudad}</td>
                </tr>`
        }
        document.getElementById('apicamion').innerHTML=texto;
    }


}
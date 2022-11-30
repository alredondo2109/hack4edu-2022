
//guardamos los input en cada una de las variables
var formulario = document.getElementById('formulario'),
    correo = formulario.correo,
    clave = formulario.clave,
    terminos = formulario.terminos,
    error = document.getElementById('error');


//quiero que cuando presione el boton valide todos los campos

function validarCorreo(e){
    //alert();
    // con .value accedemos al valor del input
    
    if(correo.value == '' | correo.value == null){
        console.log('Por favor complet el correo');
        error.style.display= 'block';
        error.innerHTML = error.innerHTML + '<li>Por favor completa el correo</li>';
        e.preventDefault();//tenemos que parar el formulario para que no se envie si hay un error
    }else{//no hay error y queremos ocultar el mensale
        error.style.display = 'none';
    }
}

function validarClave (e){
    if(clave.value == '' | clave.value == null){
        error.style.display= 'block';
        error.innerHTML = error.innerHTML + '<li>Por favor completa con tu clave</li>';
        e.preventDefault();
    }else{
        error.style.display = 'none';
    }
}

function validarTerminos (e){
    if(terminos.checked == false){
        console.log('Por favor afecta los terminos');
        error.style.display= 'block';
        error.innerHTML = error.innerHTML + '<li>Por favor acepta los terminos</li>';
        e.preventDefault();
    }else{
        error.style.display = 'none';
    }
  
}

function validarFormulario(e){
    //el mensaje que tenemos de error queremos resetearlo para que cada vez que demos a registrar no se duplique
    error.innerHTML = '';
    
    validarCorreo(e);
    validarClave(e);
    validarTerminos(e);
}


formulario.addEventListener('submit', validarFormulario);



    //alert('Hola mundo, soy Raquel ');
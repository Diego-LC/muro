function str(error){
    a = `<ul class="mt-2 d-flex justify-content-center">
            <li class="list-group-item list-group-item-danger p-2 bd-highlight mb-3">
                ${error}
            </li>
        </ul>`;
    return a
}

function old(fecha) {
    var hoy = new Date();
    var cumpleanos = new Date(fecha);
    var edad = hoy.getFullYear() - cumpleanos.getFullYear();
    var mes = hoy.getMonth() - cumpleanos.getMonth();

    if (mes < 0 || (mes === 0 && hoy.getDate() < cumpleanos.getDate())) {
        edad--;
    }
    return edad;
}

emailRegex = /^[-\w.%+]{1,64}@(?:[A-Z0-9-]{1,63}\.){1,125}[A-Z]{2,63}$/i;
document.getElementById('form1').addEventListener('input', function() {
    campo = event.target;
    //Se muestra un texto a modo de ejemplo, luego va a ser un icono
    if (($('#fname').val()).length < 2){
        $('#fname').removeClass('green').addClass('red')
    }else{
        $('#fname').removeClass('red').addClass('green')
    }
    if (($('#lname').val()).length < 2){
        $('#lname').removeClass('green').addClass('red')
    }else{
        $('#lname').removeClass('red').addClass('green')
    }
    if (emailRegex.test($('#email').val())) {
        $('#email').removeClass('red').addClass('green')
    } else {
        $('#email').removeClass('green').addClass('red')
    }
    if (old($('#date').val()) < 13){
        $('#date').removeClass('green').addClass('red')
        $('#fecha').html('')
        error = 'Para registrarse se debe tener al menos 13 años de edad'
        a = str(error)
        $(a).hide().appendTo($('#fecha')).fadeIn(700);
    }else{
        $('#date').removeClass('red').addClass('green')
        $('#fecha').html('')
        }
    if (($('#pw').val()).length < 8){
        $('#pw').removeClass('green').addClass('red')
    }else{
        $('#pw').removeClass('red').addClass('green')
    }
    if (($('#pw2').val()).length < 8){
        $('#pw2').removeClass('green').addClass('red')
    }else{
        $('#pw2').removeClass('red').addClass('green')
        }
    });

$(document).ready(function(){
    
    $('#form1').submit(function(){
        var count = 0;
        if (($('#fname').val()).length < 2){
            $('#nombre').html('')
            error = 'El campo nombre debería tener al menos dos carácteres'
            a = str(error)
            $(a).hide().appendTo($('#nombre')).fadeIn(600);
            count += 1;
        } ;
        if (($('#lname').val()).length < 2){
            $('#apell').html('')
            error = 'El campo apellido debería tener al menos dos carácteres'
            a = str(error)
            $(a).hide().appendTo($('#apell')).fadeIn(600);
            count += 1;
        }
        if (emailRegex.test($('#email').val()) == false){
            $('#em').html('')
            error = 'El campo email debería tener un formato válido'
            a = str(error)
            $(a).hide().appendTo($('#em')).fadeIn(700);
            count += 1;
        }

        $('#validate_email').val($('#email').val())
        var valid = $.post('/valid', $('#form2').serialize()).done(function(data){
            if (data.length > 1){
                $('#em').html('')
                error = 'El email ya está registrado'
                a = str(error)
                $(a).hide().appendTo($('#em')).fadeIn(700);
                count += 1;
            }
        })
        if (old($('#date').val()) < 13){
            $('#fecha').html('')
            error = 'Para registrarse se debe tener al menos 13 años de edad'
            a = str(error)
            $(a).hide().appendTo($('#fecha')).fadeIn(700);
            count += 1;
        }
        if ($('#pw').val() != $('#pw2').val()){
            $('#contra2').html('')
            error = 'Las contraseñas no coinciden'
            a = str(error)
            $(a).hide().appendTo($('#contra2')).fadeIn(700);
            count += 1;
        }
        console.log(count)
        if (count == 0){
            return true;
        }    
        return false;
    });

});
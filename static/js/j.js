const $txtnombre = document.getElementById('txtnombre');
const $formulario = document.getElementById('formulario');
const $btneliminacion = document.querySelectorAll('.btneliminacion');


(function () {
    
    $formulario.addEventListener('submit', function (e) {
        let nombre= String($txtnombre.value).trim()
        if (nombre.length===0){
            Swal.fire(
                'Error  al Guradar Curso',
                'El compo Nombre no pude contener espacios en Blanco',
            );
            e.preventDefault();
        }
        
    });

    $btneliminacion.forEach(btn => {
        btn.addEventListener('click', function (e) {
            e.preventDefault()
            Swal.fire({
                title: "¿esta seguro de eliminar el curso?",
                showCancelButton:true,
                confirmButtonText: "Eliminar",
                confirmButtonColor: "#d33",
                backdrop:true,
                showLoaerOnConfirm:true,
                preConfirm:()=>{
                    location.href=e.target.href;

                },
                allowOutsideClick:()=>false,
                allowEscapekey:()=>false

              });
            
        })
        
    });
})();

// toast

const alertBoxerror = document.querySelector('.alert-boxs-error');
const closeBtn = document.querySelector('.close-btn');
const msg = document.querySelector('.errorlist')


let timer;


if (msg.innerText){


     showAlertBox();
}



closeBtn.addEventListener('click', function(){
    hideAlertBox();
    clearTimeout(timer);
})


function showAlertBox(){

    if(alertBoxerror.classList.contains('hidden')){
        alertBoxerror.classList.remove('hidden')
    }

    alertBoxerror.classList.remove('hide');
    alertBoxerror.classList.add('show');
    timer = setTimeout(function(){
        hideAlertBox();
    }, 5000)


}



function hideAlertBox(){
    alertBoxerror.classList.remove('show');
    alertBoxerror.classList.add('hide');
}

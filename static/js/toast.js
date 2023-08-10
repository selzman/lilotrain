
// toast

const alertBox = document.querySelector('.alert-boxs');
const closeBtn = document.querySelector('.close-btn');
const msg = document.getElementById('msg')


let timer;


if (msg.innerText != null){
     showAlertBox();
}



closeBtn.addEventListener('click', function(){
    hideAlertBox();
    clearTimeout(timer);
})


function showAlertBox(){

    if(alertBox.classList.contains('hidden')){
        alertBox.classList.remove('hidden')
    }

    alertBox.classList.remove('hide');
    alertBox.classList.add('show');
    timer = setTimeout(function(){
        hideAlertBox();
    }, 5000)


}



function hideAlertBox(){
    alertBox.classList.remove('show');
    alertBox.classList.add('hide');
}

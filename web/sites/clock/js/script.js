window.onload = countdown;

function countdown(){
    var tday = new Date();

    var hr = tday.getHours();
    var min = tday.getMinutes();
    var sec = tday.getSeconds();

    if(sec < 10) sec = '0' + sec;
    if(min < 10) min = '0' + min;

    var data = hr + ' : ' + min + ' : ' + sec;

    document.getElementById('clock').innerHTML = data;

    setTimeout('countdown()', 1000);
}

function check(){
    var val = document.getElementById('input1').value;
    var res;

    if(val < 0) res = 'Ujemna';
    if(val > 0) res = 'Dodatnia';
    if(val == 0) res = 'Zero';

    document.getElementById('result').innerHTML = res;
}

const hamburger = document.querySelector('.hamburger');
const handleClick = () => {
    hamburger.classList.add('hamburger-active');
}
if(hamburger){
    hamburger.addEventListener('onclick', handleClick);
}
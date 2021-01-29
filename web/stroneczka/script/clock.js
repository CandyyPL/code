setInterval(watch, 1000);

const hh = document.querySelector('[hour-hand]');
const mh = document.querySelector('[minute-hand]');
const sh = document.querySelector('[second-hand]');

function watch(){
    const time = new Date();

    var s = time.getSeconds() / 60;
    var m = (s + time.getMinutes()) / 60;
    var h = (m + time.getHours()) / 12;

    setRotation(hh, h);
    setRotation(mh, m);
    setRotation(sh, s);
}

function setRotation(element, rotation){
    element.style.setProperty('--rotation', rotation * 360);
}

watch()
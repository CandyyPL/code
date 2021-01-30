const hamburger = document.querySelector('.hamburger');
const navigation = document.querySelector('.nav');

function handleClick(){
    hamburger.classList.toggle('hamburger-active');
    navigation.classList.toggle('nav-active');
}

hamburger.addEventListener('click', handleClick);
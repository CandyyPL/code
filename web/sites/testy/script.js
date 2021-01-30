var div = document.querySelector('.rectangle');

const handleClick = () => {
    div.classList.toggle('move');
}

div.addEventListener('click', handleClick);
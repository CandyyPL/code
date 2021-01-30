const item = document.querySelectorAll('.main__content__item');
const searchBar = document.querySelector('#search_bar');

setInterval(check, 2000);

function check(){
    var searched = (searchBar.value).toLowerCase();
    item.forEach((element) => {
        var name = (element.attributes.name.nodeValue).toLowerCase();
        if(searched == ''){
            element.style.display = 'flex';
        }
        else if(searched != '' && name.includes(searched) == false){
            element.style.display = 'none';
        }
    });
}
const addPost = () => {
    var post = document.createElement('div');
    post.classList.add('post-zadanie')

    var postSubject = promt('Przedmiot: ');
    var postContent = promt('Treść zadania: ');
    var postTeacher = promt('Imię i nazwisko nauczyciela: ');

    var tDay = new Date();

    var d = tDay.getDate();
    var m = tDay.getMonth();
    var y = tDay.getFullYear();

    var hrs = tDay.getHours();
    var min = tDay.getMinutes();

    if(min < 10) min = '0' + min;

    var months = new Array(12);

    months[0] = ' stycznia ';
    months[1] = ' lutego ';
    months[2] = ' marca ';
    months[3] = ' kwietnia ';
    months[4] = ' maja ';
    months[5] = ' czerwca ';
    months[6] = ' lipca ';
    months[7] = ' sierpnia ';
    months[8] = ' września ';
    months[9] = ' października ';
    months[10] = ' listopada ';
    months[11] = ' grudnia ';

    if(postSubject != null && postContent != null && postTeacher != null){
        var postInfo = 'Admin ' + d + months[m] + y + ' ' + hrs + ':' + min;
        var innerPost = '<div class="post-header">' + postSubject.toUpperCase() + '</div> <p>' + postContent + '</p><div class="sign">' + postTeacher + '</div> <div class="post-info">' + postInfo + '</div>';
        post.innerHTML = innerPost;
        var main = document.querySelector('main');
        main.appendChild(post);
    }
}
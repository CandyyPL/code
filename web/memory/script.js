/*var imgNames = new Array(6);

imgNames[0] = 'ciri.png';
imgNames[1] = 'geralt.png';
imgNames[2] = 'jaskier.png';
imgNames[3] = 'iorweth.png';
imgNames[4] = 'triss.png';
imgNames[5] = 'yen.png';

// Card positions Draw
// {

// }

var cards = new Array(12);

cards[ciri1] = imgNames[0];
cards[ciri2] = imgNames[0];
cards[geralt1] = imgNames[1];
cards[geralt2] = imgNames[1];
cards[jaskier1] = imgNames[2];
cards[jaskier2] = imgNames[2];
cards[iorweth1] = imgNames[3];
cards[iorweth2] = imgNames[3];
cards[triss1] = imgNames[4];
cards[triss2] = imgNames[4];
cards[yen1] = imgNames[5];
cards[yen2] = imgNames[5];
*/

var cards = ['ciri.png', 'geralt.png', 'yen.png', 'jaskier.png', 'iorweth.png', 'triss.png',  'geralt.png', 'jaskier.png', 'yen.png', 'triss.png', 'iorweth.png', 'ciri.png'];

$(document.getElementById('c0')).on('click', function () { showCard(0) });
$(document.getElementById('c1')).on('click', function () { showCard(1) });
$(document.getElementById('c2')).on('click', function () { showCard(2) });
$(document.getElementById('c3')).on('click', function () { showCard(3) });
$(document.getElementById('c4')).on('click', function () { showCard(4) });
$(document.getElementById('c5')).on('click', function () { showCard(5) });
$(document.getElementById('c6')).on('click', function () { showCard(6) });
$(document.getElementById('c7')).on('click', function () { showCard(7) });
$(document.getElementById('c8')).on('click', function () { showCard(8) });
$(document.getElementById('c9')).on('click', function () { showCard(9) });
$(document.getElementById('c10')).on('click', function () { showCard(10) });
$(document.getElementById('c11')).on('click', function () { showCard(11) });

var oneVis = false;
var turns = 0;
var card;
var lock = false;
var pairsLeft = 6;

function showCard(num){
    if($('#c'+num).css('opacity') == 1 && lock == false){
        var image = 'url(img/' + cards[num] + ')';

        $('#c'+num).css('background-image', image);
        $('#c'+num).addClass('card-active');

        if(oneVis == false){
            oneVis = true;
            card = num;
        }
        else{
            if(card != num){
                lock = true;
                if(cards[card] == cards[num]){
                    pairsLeft--;
                    setTimeout(function() { hideCards(card, num) }, 500);
                }
                else{
                    setTimeout(function() { hideBadCards(card, num) }, 750);
                }

                turns++;
                $('.score').html('Turn counter: '+turns);

                oneVis = false;
            }
        }
    }
}

function hideCards(card1, card2){
    $('#c' + card1).css('opacity', '0');
    $('#c' + card2).css('opacity', '0');
    lock = false;

    if(pairsLeft == 0){
        $('.field').html('<span class="end">Wygrana</span><br><br><span class="end_bt" onclick="location.reload()">Jeszcze Raz</span>');
    }
}

function hideBadCards(card1, card2){
    $('#c' + card1).css('background-image', 'url(img/karta.png)');
    $('#c' + card1).removeClass('card-active');
    $('#c' + card2).css('background-image', 'url(img/karta.png)');
    $('#c' + card2).removeClass('card-active');
    lock = false;
}
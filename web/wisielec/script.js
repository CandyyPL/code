window.onload = write;

letters = new Array(35);

letters[0] = 'A';
letters[1] = 'Ą';
letters[2] = 'B';
letters[3] = 'C';
letters[4] = 'Ć';
letters[5] = 'D';
letters[6] = 'E';
letters[7] = 'Ę';
letters[8] = 'F';
letters[9] = 'G';
letters[10] = 'H';
letters[11] = 'I';
letters[12] = 'J';
letters[13] = 'K';
letters[14] = 'L';
letters[15] = 'Ł';
letters[16] = 'M';
letters[17] = 'N';
letters[18] = 'Ń';
letters[19] = 'O';
letters[20] = 'Ó';
letters[21] = 'P';
letters[22] = 'Q';
letters[23] = 'R';
letters[24] = 'S';
letters[25] = 'Ś';
letters[26] = 'T';
letters[27] = 'U';
letters[28] = 'V';
letters[29] = 'W';
letters[30] = 'X';
letters[31] = 'Y';
letters[32] = 'Z';
letters[33] = 'Ź';
letters[34] = 'Ż';

passes = new Array(47);

passes[0] = 'YOU KNOW NOTHING JOHNY SNOW';
passes[1] = 'JAVA SCRIPT';
passes[2] = 'VISUAL STUDIO CODE';
passes[3] = 'WEB STORM';
passes[4] = 'PROGRAMMING';
passes[5] = 'JSX';
passes[6] = 'WEB DEVELOPMENT';
passes[7] = 'WEB DEVELOPER';
passes[8] = 'C PLUS PLUS';
passes[8] = 'ZAŻÓŁĆ GĘŚLĄ JAŻŃ';
passes[9] = 'OPERATING SYSTEM';
passes[10] = 'BOOTLOADER';
passes[11] = 'GRAPHICAL PROCESSING UNIT';
passes[12] = 'CENTRAL PROCESSING UNIT';
passes[13] = 'HYPER TEXT MARKUP LANGUAGE';
passes[14] = 'CASCADING STYLE SHEETS';
passes[15] = 'ANGULAR';
passes[16] = 'JAVA';
passes[17] = 'NODE JS';
passes[18] = 'PHP';
passes[19] = 'SQL';
passes[20] = 'REACT';
passes[21] = 'MACBOOK';
passes[21] = 'HYPERTEXT PREPROCESSOR';
passes[22] = 'INTEL';
passes[23] = 'AMD';
passes[24] = 'PERIPHERAL COMPONENT INTERCONNECT EXPRESS';
passes[25] = 'LINUS TORVALDS';
passes[26] = 'ALAN WALKER';
passes[27] = 'ROBIN SCHULZ';
passes[28] = 'MARTIN GARRIX';
passes[29] = 'BASIC INPUT OUTPUT SYSTEM';
passes[30] = 'MYSQL';
passes[31] = 'LUMOS';
passes[32] = 'PETRIFICUS TOTALUS';
passes[33] = 'ARRESTO MOMENTUM';
passes[34] = 'AVADA KEDAVRA';
passes[35] = 'LORD VOLDEMORT';
passes[36] = 'TOM MARVOLO RIDDLE';
passes[37] = 'HARRY POTTER';
passes[38] = 'ALBUS PERCIVAL WULFRIC BRIAN DUMBLEDORE';
passes[39] = 'MINERVA MCGONAGALL';
passes[40] = 'PROTEGO MAXIMA';
passes[41] = 'SALVIO HEXIA';
passes[42] = 'FIANTO DURI';
passes[43] = 'PROTEGO HORRIBILIS';
passes[44] = 'REPELLO INIMICUM';
passes[45] = 'LUMOS MAXIMA';
passes[46] = 'HARMONIA NECTERE PASSUS';

var pasNum = Math.floor(Math.random()*47);

var passphrase = passes[pasNum];
var psph_dashed = '';
var pass_ln = passphrase.length;
var fails = 0;

for(i = 0; i < pass_ln; i++){
    if(passphrase.charAt(i) == ' ') psph_dashed += ' ';
    else psph_dashed += '-';
}

function write(){
    document.querySelector('.pass').innerHTML = psph_dashed;
}

var wholeAlph = '';

for(i = 0; i <= 34; i++){
    var divNum = 'let' + i;
    wholeAlph += '<div class="letter" id='+divNum+' onclick="check('+i+')">'+letters[i]+'</div>'
}

document.querySelector('.alph').innerHTML = wholeAlph;

String.prototype.setChar = function(pos, char){
    if(pos > this.length-1) return this.toString();
    else{
        return this.substr(0, pos) + char + this.substr(pos+1);
    }
}

function check(num){
    var good = false;

    for(i = 0; i < pass_ln; i++){
        if(passphrase.charAt(i) == letters[num]){
            psph_dashed = psph_dashed.setChar(i, letters[num]);
            good = true;
        }
    }

    if(good == true){
        var divNum = 'let' + num;
        document.getElementById(divNum).style.background = '#45a372';
        document.getElementById(divNum).style.color = '#286646';
        document.getElementById(divNum).style.border = '2.5px solid #286646';
        document.getElementById(divNum).style.cursor = 'default';

        write();
    }
    else{
        var divNum = 'let' + num;
        document.getElementById(divNum).style.background = '#d10d44';
        document.getElementById(divNum).style.color = '#821433';
        document.getElementById(divNum).style.border = '2.5px solid #821433';
        document.getElementById(divNum).style.cursor = 'default';
        document.getElementById(divNum).setAttribute('onclick', ';');

        fails++;
        var img = 'img/s'+fails+'.jpg';

        if(fails < 9){
            document.querySelector('.imgs').innerHTML = '<img src="'+img+'">';
        }
        else{
            document.querySelector('.imgs').innerHTML = '<img src="'+img+'">';
            document.querySelector('.alph').innerHTML = 'Przegrana! <br><br> <span class="reset-lose" onclick="location.reload()">Jeszcze Raz</span>';
        }
    }

    if(psph_dashed == passphrase){
        document.querySelector('.alph').innerHTML = 'Podano prawidłowe hasło! <br><br> <span class="reset" onclick="location.reload()">Jeszcze Raz</span>';
    }
}
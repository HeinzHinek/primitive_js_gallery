
var messages = [
    '',
    'みなさん',
    'Thank you...',
    '...for being here!',
    'Please welcome...',
    '',
    'JAN & SAYA'
]

function getRandomColor() {
    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}

function setRandomColor() {
    $("#psychedelic").css("background-color", getRandomColor());
}

function calculateImgSize(srcWidth, srcHeight, maxWidth, maxHeight) {
    var ratio = Math.min(maxWidth / srcWidth, maxHeight / srcHeight);
    return { width: srcWidth * ratio, height: srcHeight * ratio };
}

function epileptize() {
    setTimeout(function () {
        setRandomColor();
        epileptize();
    }, 200)
};

function show_message(idx) {
    var $msg = $("#msg");

    if (idx == 5) {
        var $img = $('#img');
        $img.show();
        $img.animate({
            opacity: 1
        }, 2000)
    } else if (idx == 6) {
        epileptize();
    } else if (idx == messages.length) {
        $msg.hide();
        return;
    }

    $msg.text(messages[idx]);

    idx++;

    $msg.show();
    $msg.animate({
        "font-size": "6em",
        opacity: 1
    }, 3200, function() {
        $msg.animate({
            "font-size": "6.5em"
        }, 4000, function () {
            $msg.animate({
                "font-size": "10em",
                "opacity": "0"
            }, 3000, function() {
                $msg.hide();
                $msg.removeAttr('style');
                $msg.removeClass('.msg');
                show_message(idx);
            })
        })
    });
}

$(document).ready(function() {
    var winWidth = window.innerWidth;
    var winHeight = window.innerHeight;

    var $img = $('#img');
    var $svg = $(document).find('svg');

    newImgSize = calculateImgSize($img.width(), $img.height(), winWidth, winHeight);

    $img.attr('width', newImgSize.width);
    $img.attr('height', newImgSize.height);
    $img.css('marginLeft', (winWidth - newImgSize.width) / 2);
    $img.css('marginTop', (winHeight - newImgSize.height) / 2);

    $img.on('click', function() {
        window.location.href = "/show";
    });

    show_message(0);
});

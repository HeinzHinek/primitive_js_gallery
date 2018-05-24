
function nextImg() {
    setTimeout(function() {
        // Send next image
    }, 5000);
}

function showImg() {
    setTimeout(function() {
        $('#img').css('z-index', 999);
        $('#img').fadeIn(2000);
        $('#svg-wrapper').fadeOut(2000, nextImg);
    }, 1000);
};

function calculateImgSize(srcWidth, srcHeight, maxWidth, maxHeight) {
    var ratio = Math.min(maxWidth / srcWidth, maxHeight / srcHeight);
    return { width: srcWidth * ratio, height: srcHeight * ratio };
 }

$(document).ready(function() {
    var winWidth = window.innerWidth;
    var winHeight = window.innerHeight;

    var $img = $('#img');
    var $svg = $(document).find('svg');

    $svg.attr('width', winWidth);
    $svg.attr('height', winHeight);

    newImgSize = calculateImgSize($img.width(), $img.height(), winWidth, winHeight);

    $img.attr('width', newImgSize.width);
    $img.attr('height', newImgSize.height);
    $img.css('marginLeft', (winWidth - newImgSize.width) / 2);
    $img.css('marginTop', (winHeight - newImgSize.height) / 2);
    $img.hide();

    var $paths = $svg.find('path');
    $paths.each(function() {
        $(this).hide();
    });

    $('#svg-wrapper').show();

    (function addPaths(i) {
        setTimeout(function() {
            var idx = $paths.length - i;
            var $path = $($paths[idx]);
            $path.show();
            if (--i) {
                addPaths(i);
            } else {
                showImg();
            }
        }, i/20)
    })($paths.length);
});

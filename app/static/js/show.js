var $svg = $("#svg");

$svg.attr("width", window.innerWidth);
$svg.attr("height", window.innerHeight);

var rect = '<rect x="' + svg_data.rect.x + 
        '" y="' + svg_data.rect.y + 
        '" width="' + svg_data.rect.width + 
        '" height="' + svg_data.rect.height + 
        '" fill="' + svg_data.rect.fill + '"/>';
$("#svg:last-child").html($("#svg:last-child").html() + rect);

function addPath(path_data) {
    var path = '<path d="' + path_data.d + 
            '" fill="' + path_data.fill + 
            '", fill-opacity="' + path_data.fillOpacity + '"/>'
    $("#svg:last-child").html($("#svg:last-child").html() + path);
}

(function addPaths(i) {
    setTimeout(function() {
        var idx = svg_data.paths.length - i;
        var path_data = svg_data.paths[idx];
        addPath(path_data);
        if (--i) addPaths(i);
    }, 1)
})(svg_data.paths.length);

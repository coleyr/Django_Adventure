var captionLength = 0;
var caption = '';


$(document).ready(function() {
    setInterval('cursorAnimation()', 600);
    captionEl = $('#caption');
    let pressed = false;

    $('#begin').click(function() {
        if (!pressed) {
            document.getElementById('begin').classList.add('hidden')
            testTypingEffect();
            // play()
            pressed = true
        }
    });

});

function play() {
    const audio = document.getElementById('Audio');
    audio.play();
}

function testTypingEffect() {
    caption = $('#user-caption').text();
    type();
}

function type() {
    captionEl.html(caption.substr(0, captionLength++));
    if (captionLength == caption.length) {
        setTimeout('type()', 75);
        showNext();
    } else if (captionLength < caption.length + 1) {
        setTimeout('type()', 75);
    } else {
        captionLength = 0;
        caption = '';
    }
}

function showNext() {
    document.getElementById('nextbutton').classList.remove('hidden')
}

function testErasingEffect() {
    caption = captionEl.html();
    captionLength = caption.length;
    if (captionLength > 0) {
        erase();
    } else {
        $('#caption').html("You didn't write anything to erase, but that's ok!");
        setTimeout('testErasingEffect()', 1000);
    }
}

function erase() {
    captionEl.html(caption.substr(0, captionLength--));
    if (captionLength >= 0) {
        setTimeout('erase()', 50);
    } else {
        captionLength = 0;
        caption = '';
    }
}

function cursorAnimation() {
    $('.cursor').animate({
        opacity: 0
    }, 'fast', 'swing').animate({
        opacity: 1
    }, 'fast', 'swing');
}
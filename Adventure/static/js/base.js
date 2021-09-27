/*!
* Start Bootstrap - Creative v7.0.4 (https://startbootstrap.com/theme/creative)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-creative/blob/master/LICENSE)
*/
//
// Scripts
// 

window.addEventListener('DOMContentLoaded', event => {

    // Navbar shrink function
    var navbarShrink = function () {
        const navbarCollapsible = document.body.querySelector('#mainNav');
        if (!navbarCollapsible) {
            return;
        }
        if (window.scrollY === 0) {
            navbarCollapsible.classList.remove('navbar-shrink')
        } else {
            navbarCollapsible.classList.add('navbar-shrink')
        }

    };

    // Shrink the navbar 
    navbarShrink();

    // Shrink the navbar when page is scrolled
    document.addEventListener('scroll', navbarShrink);

    // Activate Bootstrap scrollspy on the main nav element
    const mainNav = document.body.querySelector('#mainNav');
    if (mainNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#mainNav',
            offset: 74,
        });
    };

    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navbarResponsive .nav-link')
    );
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
            }
        });
    });

    // Activate SimpleLightbox plugin for portfolio items
    // new SimpleLightbox({
    //     elements: '#portfolio a.portfolio-box'
    // });
    function getreqfullscreen(){
        var root = document.documentElement
        return root.requestFullscreen || root.webkitRequestFullscreen || root.mozRequestFullScreen || root.msRequestFullscreen
    }
    function getexitfullscreen(){
        return document.exitFullscreen || document.webkitExitFullscreen || document.mozCancelFullScreen || document.msExitFullscreen
    }
    function getfullscreenelement(){
        return document.fullscreenElement || document.webkitFullscreenElement || document.mozFullScreenElement || document.msFullscreenElement
    }
    document.querySelectorAll(".clueimagemedia").forEach((item) => {
        item.addEventListener("click", (event) => {
            getreqfullscreen().call(event.target) ;
        });
      });
    document.querySelectorAll(".clueimagemedia").forEach((item) => {
        item.addEventListener("click", (event) => {
            if (getfullscreenelement() && getfullscreenelement().tagName == "IMG"){
                getexitfullscreen().call(document) ;
            }
        });
      });
    function saveUrl() {
        /* Get the text field */
        var copyText = document.getElementById("saveurl");
        
        /* Select the text field */
        copyText.select();
        copyText.setSelectionRange(0, 99999); /* For mobile devices */
        
            /* Copy the text inside the text field */
        navigator.clipboard.writeText(copyText.value);
        
        /* Alert the copied text */
        alert("Copied the text: " + copyText.value);
    }
    document.querySelectorAll(".saveurl").forEach((item) => {
        item.addEventListener("click", (event) => {
            saveUrl() ;
        });
      });

    });

let captionLength = 0;
let caption = '';

function type(htmlElement, caption) {
    htmlElement.html(caption.substr(0, captionLength++));
    if (captionLength == caption.length) {
        setTimeout(type, 75, htmlElement, caption);
        showNext()
    } else if (captionLength < caption.length + 1) {
        setTimeout(type, 75, htmlElement, caption);
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
};
setInterval(cursorAnimation, 600);
let pressed = false;

$('#begin').click(function() {
    if (!pressed) {
        document.getElementById('begin').classList.add('hidden')
        let htmlElement = $('#caption');
        caption = $('#user-caption').text();
        type(htmlElement, caption);
        pressed = true
    }
});

function play() {
    const audio = document.getElementById('Audio');
    audio.play();
}



function showNext() {
    document.getElementById('nextbutton')?.classList.remove('hidden')
}


const hints = [...document.querySelectorAll(".showhint")]
for (hint of hints){
    const hintNumber = hints.indexOf(hint) + 1
    hint.addEventListener("click", function () {
        const hintdisplay = document.getElementById(`hint-${hintNumber}`);
        const messagetext = document.querySelector(`#hint-${hintNumber} .messagecontents`).textContent
        let messagedisplay = $(`#hint-${hintNumber} .mesagedisplay`)
        if (hintdisplay.style.display === "none") {
            hintdisplay.style.display = "block";
            type(messagedisplay, messagetext)
        } else {
            hintdisplay.style.display = "none";
        }
        } )
}


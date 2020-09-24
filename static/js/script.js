$('.slider').slick({
    arrows: false,
    autoplay: true,
    speed: 800,
    dots: true,
    draggable: true,
    focusOnSelect: true
}).slickAnimation();

$('.client-for').slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    arrows: false,
    infinite: true,
    dots: true,
    autoplay: true,
    autoplaySpeed: 2000,
    speed: 300,
    focusOnSelect: true
});

$('.slider').mouseover(function () {
    $(this).slick('play')
});

$('.client-logo').slick({
    slidesToShow: 6,
    slidesToScroll: 6,
    arrows: false,
    infinite: true,
    dots: false,
    autoplay: true,
    autoplaySpeed: 2000,
    speed: 300,
    focusOnSelect: true,
    responsive: [
        {
            breakpoint: 1024,
            settings: {
                slidesToShow: 5,
                slidesToScroll: 5
            }
                            },
        {
            breakpoint: 768,
            settings: {
                slidesToShow: 4,
                slidesToScroll: 4
            }
                            },
        {
            breakpoint: 576,
            settings: {
                slidesToShow: 2,
                slidesToScroll: 2
            }
                            }


                          ]
});



$(window).scroll(function () {
    var sticky = $('.navbar'),
        scroll = $(window).scrollTop();

    if (scroll >= 200) {
        sticky.addClass('fixed-top');
        btn.show();
    } else {
        sticky.removeClass('fixed-top');
        btn.hide();
    }
});

var btn = $('#bottom-btn');
btn.on('click', function (e) {
    e.preventDefault();
    $('html, body').animate({
        scrollTop: 0
    }, '500');
});

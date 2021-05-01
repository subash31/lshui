
$('document').ready(function(){
    $('.img-carousel').on('slide.bs.carousel', function (e) {
        var $e = $(e.relatedTarget);
        var idx = $e.index();
        var itemsPerSlide = 5;
        var totalItems = $('.img-carousel .carousel-item').length;
        console.log('totalItems--', totalItems);
        console.log('idx--', idx);
        if (idx >= totalItems-(itemsPerSlide-1)) {
            var it = itemsPerSlide - (totalItems - idx);
            console.log('it--', it);
            for (var i=0; i < it; i++) {
                    // append slides to end
                    if (e.direction=="left") {
                        $('img-carousel .carousel-item').eq(i).appendTo('.img-carousel .carousel-inner');
                    }
                    else {
                        $('.img-carousel .carousel-item').eq(0).appendTo('.img-carousel .carousel-inner');
                    }
                }
            }
    });
})

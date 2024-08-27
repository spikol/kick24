$(".animate-logo").on("click touchstart", function (event) {
    if (iOS() || $(window).width() < 767) {
        console.log("Small");
        var ripple = $('<span>');
        ripple.addClass('ripple');

        var max = Math.max($(this).width(), $(this).height());

        ripple.css('width', max * 2 + 'px');
        ripple.css('height', max * 2 + 'px');

        var rect = $(this).offset();

        ripple.css('left', event.pageX - rect.left - max + 'px');
        ripple.css('top', event.pageY - rect.top - max + 'px');

        $(this).append(ripple);
    }

    function iOS() {
        return [
            'iPad Simulator',
            'iPhone Simulator',
            'iPod Simulator',
            'iPad',
            'iPhone',
            'iPod'
        ].includes(navigator.platform)||(navigator.userAgent.includes("Mac") && "ontouchend" in document)
    }
});

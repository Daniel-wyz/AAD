
$(window).on("beforeunload", function (e) {
    const top = $(window).scrollTop();
    console.log("unload:" + top)
    $.cookie("scroll_top", top);
});

$(document).ready(function () {
    const top = $.cookie("scroll_top");
    console.log("ready:" + top)
    window.scroll(0, top);
})

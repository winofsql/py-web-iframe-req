$(function(){
    // ***************************
    // ボタン表示位置微調整
    // ***************************
    $( ".btn" ).css({
        "margin-top": "-4px"
    });

    // ***************************
    // IFRAME に問合せを表示
    // ***************************
    $( "#btn" ).click(function() {
        $("#extend").prop("src","req/control.py?nm=" + encodeURIComponent($("#cond").val()));
    });


});

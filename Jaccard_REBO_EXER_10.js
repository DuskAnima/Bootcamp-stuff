$('#text1').mouseenter(function () { 
    $('#text2').hide();
});
$('#text1').mouseout(function () { 
    $('#text2').show('fast');
});
///////////////////////////////////////////
$('#img').click(function (e) { 
    e.preventDefault();
    $('#img').width('100%');
});
$('#img').mouseout(function () { 
    $('#img').width('20%');
});
//////////////////////////////////////////
$('#caja3').dblclick(function (e) { 
    e.preventDefault();
    $('#caja3').css('font-size', '30px');
});

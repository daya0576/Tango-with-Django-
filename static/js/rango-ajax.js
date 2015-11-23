$('#likes').click(function(){
    alert("123");
    var catid;
    catid = $(this).attr("data-catid");
    $.get('/rango/like_category/', {category_id: catid}, function(data){
               $('#like_count').html(data);
               $('#likes').hide();
               $('#liked').show();
    });
});



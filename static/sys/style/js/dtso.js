$(function (argument) {
    
$("#conding").click(function(){
    jqchk();
});
$("#dtso").click(function() {
    var data='key='+$('#dtkey').val();
    $.ajax({
        url:"/m/Dest/dtso",
        type: "POST",
        dataType:"json",
        data:data,
        success:function (data) {
            // console.log(data);
            $('.smlist').html('');
            if (data.status==1) {
                $('.dquerylist').find('tbody').html('');
                $.each(data.data, function(i, item){
                        var tr=createTr(item);
                        $('.dquerylist').find('tbody').append(tr)
　　          });
                  $('.smlist').append($('.dquerylist').html());
                
            }else if(data.status==0){
                $('.smlist').append('<p class="msg-req">未查到相关结果</p>');
            }
        }
    });
});

function createTr(dest) {
    var tr='<tr><td  class="first"><input name="dts" type="checkbox" value="'+dest.id+'"></td><td class="dtname">'+dest.name+'</td></tr>';
    return tr;
}
    function jqchk(){ //jquery获取复选框值 
        var chk_value =[]; 
        $('input[name="dts"]:checked').each(function(){ 
            chk_value.push($(this).val()); 
            $('input[name="dest"]').val($(this).val());
            var tr=$(this).parent().parent();
            var td=$(tr).find('.dtname');
            console.log($(td).html());
            $('.iViewer').html($(td).html());
        }); 

        // alert(chk_value.length==0 ?'你还没有选择任何内容！':chk_value); 
    } 
});
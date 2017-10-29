$(function (argument) {
    $("#menu").niceScroll({  
        cursorcolor:"#eee",  
        cursoropacitymax:1,  
        touchbehavior:false,  
        cursorwidth:"5px",  
        cursorborder:"0",  
        overflowx:false,
        cursorborderradius:"5px"  
    }); 
    $("#play").niceScroll({  
        cursorcolor:"#eee",  
        cursoropacitymax:1,  
        touchbehavior:false,  
        cursorwidth:"5px",  
        cursorborder:"0",  
        overflowx:false,
        cursorborderradius:"5px"  
    }); 
    

// 导航条
    var miao = window.location.hash;
    var $nav=$(".le-nav");
    var $navs=$(".le-m",$nav);
    $navs.each(function(index, val){
        var $nips=$navs[index];
        var $href=$('a',$nips);
        if ($href.attr("href")==miao) {          
            $('.on',$nav).removeClass("on");
            $($nips).addClass("on");
             var anchor=$href.attr("href").split("#");
            $('#menu').attr('src','../../m/menu/did?anchor='+anchor[1]);
        };
        $href.click(function(){
            $('.on',$nav).removeClass("on");
            $($nips).addClass("on");
             var anchor=$href.attr("href").split("#");
            $('#menu').attr('src','../../m/menu/did?anchor='+anchor[1]);
        });
    });

// var node={
//     title:"测试",
//     items :[
//         {
//             name:"子节点",
//             href:"http://www.baidu.com"
//         },
//     ]
// };
// var node_t=create_node(node); 
// $(".op-nodes").append(node_t);

function create_node (node) {
    var nd_start='<div class="node">';
    var nd_close='</div>';
    var nd_title='<h3 class="nd-title">'+node.title+'</h3>';
    var nd_items_start='<div class="nd-items">';                
    var nd_items_close='</div>'; 
    var nd_items=nd_items_start;
for(var i in node.items){
    nd_items=nd_items+'<a href="'+node.items[i].href+'" target="play">'+node.items[i].name+'</a>';
}
    nd_items=nd_items+nd_items_close;
    var node=nd_start+nd_title+ nd_items+nd_close;
    return node;           
}




});
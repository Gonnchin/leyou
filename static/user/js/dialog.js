var Dialog= {
	opt:{
		show:true,
		title:'标题',
		ids:''
	},
	show:function (show,title,ids) {
		Dialog.build(show,title);
		this.opt.ids=ids;
		// console.log(ids);
		$(".theme-context").html($("#"+this.opt.ids));
		$('.theme-poptit .close').click(function(){
		    Dialog.close();
		});
	},
	close:function () {
		Dialog.build(false);
		$(".dialogBody").append($("#"+this.opt.ids));
		$(".theme-context").html('');	

	},
	build:function (show,title) {
		if (show) {
			maskShow (true);
			$('.theme-popover').fadeIn(100);
			$('.theme-title').html(title);
		}else{
			maskShow (false);
			$('.theme-popover').fadeOut(100);
			$('.theme-title').html('');
		};
	}

}


function maskShow (bool) {
	if (true==bool) {
		$('.theme-popover-mask').fadeIn(100);
	}else{
		$('.theme-popover-mask').fadeOut(100);
	}
}
function dialog(show,title,msg){
	if (show) {
		maskShow (true);
		$('.theme-popover').fadeIn(100);
		$('.theme-context').html(msg);
		$('.theme-title').html(title);
	}else{
		maskShow (false);
		$('.theme-popover').fadeOut(100);
		$('.theme-context').html('');
		$('.theme-title').html('');
	};
}
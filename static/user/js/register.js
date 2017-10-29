
$(function(){

	var error_password = false;
	var error_check_password = false;
	var error_email = false;


	$('#pwd').blur(function() {
		// 隐藏服务器端的错误信息提示
		$('.error_tip_info').hide();
		check_pwd();
	});

	$('#cpwd').blur(function() {
		// 隐藏服务器端的错误信息提示
		$('.error_tip_info').hide();
		check_cpwd();
	});

	$('#email').blur(function() {
		// 隐藏服务器端的错误信息提示
		$('.error_tip_info').hide();
		check_email();
	});

	function check_pwd(){
		var len = $('#pwd').val().length;
		if(len<6||len>20)
		{
			$('#pwd').next().html('密码最少6位，最长20位')
			$('#pwd').next().show();
			error_password = true;
		}
		else
		{
			$('#pwd').next().hide();
			error_password = false;
		}		
	}

	function check_cpwd(){
		var pass = $('#pwd').val();
		var cpass = $('#cpwd').val();

		if(pass!=cpass)
		{
			$('#cpwd').next().html('两次输入的密码不一致')
			$('#cpwd').next().show();
			error_check_password = true;
		}
		else
		{
			$('#cpwd').next().hide();
			error_check_password = false;
		}		
		
	}

	function check_email(){
		var re = /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/;

		if(re.test($('#email').val()))
		{
			$.get('/users/check_exist/', {'user_email':$('#email').val()}, function(data) {

                if(data.ret == 1){
                	$('#email').next().html('该邮箱已注册').show();
					// $('#email').next().hide();
                	error_email = true;
                }else{
					$('#email').next().hide();
					error_email = false;
                }
        	});
		}
		else
		{
			$('#email').next().html('你输入的邮箱格式不正确')
			$('#email').next().show();
			error_check_password = true;
		}

	}

	$('#reg_form').submit(function() {
		check_pwd();
		check_cpwd();
		check_email();

		if(error_password == false && error_check_password == false && error_email == false)
		{
			return true;
		}
		else
		{
			return false;
		}

	});

})
'use strict';
var token = $('input[name=csrfmiddlewaretoken]').val();

$(function(){
	$.ajaxSetup({
		data:{csrfmiddlewaretoken:'{{ csrf_token }}'}
	});

	$('.form_text_ipt input').focus(function(){
		$('.ececk_warning').hide();
	});

	$("#email").blur(function(){
		var email = $('#email').val();
		$.ajax({
			type: "POST",
			url: "/register",
			data:{
				"email":email
			},
			success: function(data){
				if (data["err"] === 0){

				} else if (data["err"] === 1) {
					$('#regist_echeck').show();
					$('#regist_echeck_text').text('该邮箱已经注册!');
					return false;
				}
			}
		});
	});

	$("#username").blur(function(){
		var username = $('#username').val();
		$.ajax({
			type: "POST",
			url: "/register",
			data:{
				"username":username
			},
			success: function(data){
				if (data["err2"] === 0){

				} else if (data["err2"] === 1) {
					$('#regist_echeck').show();
					$('#regist_echeck_text').text('用户名已经注册！');
					return false;
				}
			}
		});
	});

	$("#send_code").click(function() {
		var email = $('#email').val();
		var username = $('#username').val();
		if (! /^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$/.test(email)) {
			$('.ececk_warning').show();
			$('.ececk_warning_text').text('邮箱格式有误！')
			return false;
		}
		// 通过Ajax技术连接服务器后端校验用户名是否已被注册
		console.log("校验邮箱...")
		$.ajax({
			url: "/check_uname",
			data: {
				email: email,
				username: username
			},
			success: function(data){
				if (data["err"] === 0){
					// console.log("校验用户名...")
					if(data["err2"] == 0){
						// 邮箱没有被注册
					var s = 60;
					$("#send_code").prop("disabled", true);
					$("#send_code").html(s + "S");
					
					var timer = window.setInterval(function() {
						--s;
						if (s === 0) {
							window.clearInterval(timer);
							$("#send_code").html("重新发送");
							$("#send_code").prop("disabled", false);
							return;
						}
						$("#send_code").html(s + "S");
					}, 1000);
					// 通过ajax请求后端发送验证码
					console.log("申请发送验证码")
					$.ajax({
						type: "POST",
						url: "/send_code",
						data: {
							csrfmiddlewaretoken: token,
							email: email
						},
						dataType: "json",
						success: function(data) {
							if (data["err"] === 0) {
								// 发送验证码成功！
							}
							else {
								// 失败
								alert("发送验证码失败！" + data["desc"]);
							}
						},
						error: function() {
							alert("发送请求失败，请检查网络连接！");
						}
					});
					}else if (data["err2"] == 1){
						// 用户名已经被注册
						$('.ececk_warning').show();
						$('.ececk_warning_text').text('用户名已经注册！')
					}
					

				} else if (data["err"] === 1) {
					// 邮箱已经被注册
					console.log("1111111111111")
					$('.ececk_warning').show();
					$('.ececk_warning_text').text('该邮箱已经注册！')
					return false;
				}
			}
		});
	});

	$('#submit').click(function (){
		console.log("11111111111")
		var email = $('#email').val();
		var username = $('#username').val();
        var password = $('#password').val();
        var password2 = $('#password2').val();
		var code = $('#code').val();
		if (email.trim() == '' || username.trim() == '' || password.trim() == '' || password2.trim() == '' || code.trim() == '') {
			$('.ececk_warning').show();
			$('.ececk_warning_text').text('请输入完整信息！')
			return false;
		}
		if (! /^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$/.test(email)) {
			$('.ececk_warning').show();
			$('.ececk_warning_text').text('邮箱格式有误！')
			return false;
		} 
		if (username.length < 6 || username.length > 16) {
			$('.ececk_warning').show();
			$('.ececk_warning_text').text('用户名长度为6~16个有效字符')
			return false;
		}
		if (! /^[a-zA-Z0-9_?!/*-+.]+$/.test(username)) {
			$('.ececk_warning').show();
			$('.ececk_warning_text').text('用户名只能含有数字、字母、下划线，其它字符无效！')
			return false;
        }
		if (password.length < 6 || password.length > 16) {
			$('.ececk_warning').show();
			$('.ececk_warning_text').text('密码长度为6~16个有效字符')
			return false;
		}
		if (! /^[a-zA-Z0-9_?!/*-+.]+$/.test(password)) {
			$('.ececk_warning').show();
			$('.ececk_warning_text').text('密码中只能含有数字、字母、下划线，其它字符无效！')
			return false;
        }
        if (password2 !== password) {
			$('.ececk_warning').show();
			$('.ececk_warning_text').text('两次输入密码不一致！')
			return false;
		}
		if (! /^\d{6}$/.test(code)) {
			$('.ececk_warning').show();
			$('.ececk_warning_text').text('验证码为六位数字！')
			return false;
		}
		return true;
	});

	$('#form1').submit(function(){
		var postData = $("#form1").serialize();
		$.ajax({
			type: "POST",
			url: "/register",
			data:postData,
			success: function(data){
				if (data["err"] === 0){
					if(data["err2"] == 0){
						if(data["err3"] == 0){
							window.location.href = "/login";
						}else if (data["err3"] == 1){
							// 验证码错误
							$('.ececk_warning').show();
							$('.ececk_warning_text').text('验证码错误！')
							return false;
						}
					}else if (data["err2"] == 1){
						// 用户名已经被注册
						$('.ececk_warning').show();
						$('.ececk_warning_text').text('用户名已经注册！')
						return false;
					}
					
				} else if (data["err"] === 1) {
					$('.ececk_warning').show();
					$('.ececk_warning_text').text('该邮箱已经注册！')
					return false;
				} else if (data["err"] === 2) {
					$('.ececk_warning').show();
					$('.ececk_warning_text').text('邮箱发生更改！')
					return false;
				}
			}
		});
		return true;
	});
	$('#form2').submit(function(){
		var postData = $("#form2").serialize();
		$.ajax({
			type: "POST",
			url: "/login",
			data:postData,
			success: function(data){
				if (data["err"] === 0){
					window.location.href = "/";
				} else if (data["err"] === 1) {
					$('.ececk_warning').show();
					$('.ececk_warning_text').text('用户名或密码错误!')
					return false;
				}
			}
		});
		return true;
	});
});



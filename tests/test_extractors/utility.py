html_doc_with_captcha = """
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en"><head>
	<base href="https://service2.diplo.de/rktermin/">
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=9; IE=10; IE=11">
	<title>
		RK-Termin - Kategorie
	</title>	
	<link rel="stylesheet" type="text/css" href="style_css/reset.css">	
	<link rel="stylesheet" type="text/css" media="screen" href="style_css/screen.css">	
	<link rel="stylesheet" type="text/css" media="print" href="style_css/print.css">	
	<link rel="stylesheet" type="text/css" media="screen" href="style_css/rktermin.css">

	<!--[if gte IE 7]><link rel="stylesheet" type="text/css" media="screen" href="style_css/ie7.css" /><![endif]-->	
	<!--[if gte IE 6]><link rel="stylesheet" type="text/css" media="screen" href="style_css/ie6.css" /><![endif]-->	
	<!--[if lte IE 5.5000]><link rel="stylesheet" type="text/css" media="screen" href="style_css/ie5.css" /><![endif]-->	


	<link rel="stylesheet" type="text/css" href="css/redmond/jquery-ui-1.11.4.custom.min.css">
	<script type="text/javascript" src="js/jquery-1.6.2.min.js"></script> 
	<script type="text/javascript" src="js/jquery-ui-1.11.4.custom.min.js"></script> 

</head>
<body data-gr-c-s-loaded="true">
<div id="global">

	<div id="header">

		<div id="logo">
			<img src="style_images/auswaertiges-amt-logo-220x120.gif" alt="Auswärtiges Amt">
		</div>
		<div id="logo-app" style="background-image:  url('images/auswaertigesamt.gif'); min-height: 54px; width: 78%;">
			&nbsp;
		</div>
		<div id="nav-main" style="min-height: 28px;">


<ul>
	<li></li>
</ul>
		</div>		

	</div> <!-- end: #header -->			


	<div id="main" class="l-s">

		<div id="content">

			<div class="wrapper">	


<div style="font-size: 14pt; font-weight: bold; margin-bottom: 1em;">
Национальная виза
</div>







<form id="appointment_captcha_month" name="appointment_captcha_month" onsubmit="startCommitRequest();" action="/rktermin/extern/appointment_showMonth.do" method="post" class="top">

<div>


<captcha>
<div id="_680500659" style="background:white url('data:image/jpg;base64,CapTch4/Zq==') no-repeat scroll left top;width:350px;height:50px;margin:2em;display:block;">&nbsp;</div>
</captcha>




<div class="input submit left">
<input type="submit" value="Загрузить новую картинку" id="appointment_captcha_month_refreshcaptcha" name="action:appointment_refreshCaptchamonth">

</div>
</div>
<div id="wwgrp_appointment_captcha_month_captchaText" class="input text s">
<div id="wwlbl_appointment_captcha_month_captchaText" class="wwlbl">
<label for="appointment_captcha_month_captchaText" class="label">        Введите код с картинки:
</label></div> 
<div id="wwctrl_appointment_captcha_month_captchaText">
<input type="text" name="captchaText" value="" id="appointment_captcha_month_captchaText" class="input text s" onkeypress="checkKey(event)"></div> </div>

<input type="hidden" name="rebooking" value="false" id="appointment_captcha_month_rebooking">
<input type="hidden" name="token" value="" id="appointment_captcha_month_token">
<input type="hidden" name="lastname" value="" id="appointment_captcha_month_lastname">
<input type="hidden" name="firstname" value="" id="appointment_captcha_month_firstname">
<input type="hidden" name="email" value="" id="appointment_captcha_month_email">
<input type="hidden" name="locationCode" value="jeka" id="appointment_captcha_month_locationCode">
<input type="hidden" name="realmId" value="881" id="appointment_captcha_month_realmId">
<input type="hidden" name="categoryId" value="1677" id="appointment_captcha_month_categoryId">
<input type="hidden" name="openingPeriodId" value="" id="appointment_captcha_month_openingPeriodId">
<input type="hidden" name="date" value="12.09.2020" id="appointment_captcha_month_date">
<input type="hidden" name="dateStr" value="12.09.2020" id="appointment_captcha_month_dateStr">





    <script type="text/javascript">
            function checkKey(event){                   
                if(event.keyCode == 13){
                    document.appointment_captcha_month.action="extern/appointment_showMonth.do";
                    document.appointment_captcha_month.submit();
                    event.preventDefault();
                }
            }
      </script>



<div class="input submit left">
	<input type="submit" value="Вперед" id="appointment_captcha_month_appointment_showMonth" name="action:appointment_showMonth">
<input type="submit" value="Отменить" id="appointment_captcha_month_choose_category" name="action:choose_category">
</div>      


</form>








<script language="javascript" type="text/javascript">

$(function() {
	$("#commit-request").dialog({
		resizable : false,
		height : 200,
		width: 350,
		modal : true,
		autoOpen: false, 
		buttons : {
			/* none */
		},
		close: function( event, ui ) {
			$('#commit-request').dialog('open');
		}
	});
 	$( "#commit-request-progressbar" ).progressbar({
	  value: false
	});
});

function startCommitRequest(event) {

	$("#commit-request").css('cursor', 'progress');

	setTimeout("innerStartCommitRequest()", 500);

	return true;

}

function innerStartCommitRequest() {
	$('#commit-request').dialog('open');
}

</script>




			</div>

			<div class="bottom"></div>

		</div>

		<div id="context">

			<div class="wrapper">
				&nbsp;
			</div>

		</div>

	</div> <!-- end: #main -->
	<div id="footer">




<div style="min-height: 15px;">
	<ul>
		<li>RK-Termin&nbsp;1.2.36.1</li>
		<li style="margin-left: 5em;">

				<a href="extern/dsgvo.do?request_locale=ru" target="_blank" title="Информация о защите данных и правила пользования"><img src="images/flags/ru.png" alt="Информация о защите данных и правила пользования" title="Информация о защите данных и правила пользования">&nbsp; Информация
					о защите данных и правила пользования</a>
			 </li>
	</ul>
</div>



	</div>
</div>

<div class="ui-dialog ui-widget ui-widget-content ui-corner-all ui-front ui-draggable" tabindex="-1" role="dialog" aria-describedby="commit-request" style="display: none;" aria-labelledby="ui-id-1"><div class="ui-dialog-titlebar ui-widget-header ui-corner-all ui-helper-clearfix ui-draggable-handle"><span id="ui-id-1" class="ui-dialog-title">В обработке ... </span><button type="button" class="ui-button ui-widget ui-state-default ui-corner-all ui-button-icon-only ui-dialog-titlebar-close" role="button" title="Close"><span class="ui-button-icon-primary ui-icon ui-icon-closethick"></span><span class="ui-button-text">Close</span></button></div><div id="commit-request" class="ui-dialog-content ui-widget-content">
	<p>
		<span class="ui-icon ui-icon-alert" style="float: left; margin: 0 7px 20px 0; margin-bottom: 100px"></span>
		<span id="question">
			<b>подождите ...</b><br>Ваш запрос обрабатывается. Пожалуйста, дождитесь ответа. Перезагрузка страницы замедлит обработку.
		</span>

	</p>
	<div id="commit-request-progressbar" style="background: #7192b6;" class="ui-progressbar ui-widget ui-widget-content ui-corner-all ui-progressbar-indeterminate" role="progressbar" aria-valuemin="0">

		<div style="background: rgba(0,0,0,0) url('images/indet.gif'); opacity:0.25; height:2em;">
			&nbsp;
		</div>

	<div class="ui-progressbar-value ui-widget-header ui-corner-left" style="width: 100%;"><div class="ui-progressbar-overlay"></div></div></div>
</div></div></body></html>
"""

html_doc_with_day = """
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en"><head>
	<base href="https://service2.diplo.de/rktermin/">
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=9; IE=10; IE=11">
	<title>
		RK-Termin - Kategorie
	</title>	
	<link rel="stylesheet" type="text/css" href="style_css/reset.css">	
	<link rel="stylesheet" type="text/css" media="screen" href="style_css/screen.css">	
	<link rel="stylesheet" type="text/css" media="print" href="style_css/print.css">	
	<link rel="stylesheet" type="text/css" media="screen" href="style_css/rktermin.css">

	<!--[if gte IE 7]><link rel="stylesheet" type="text/css" media="screen" href="style_css/ie7.css" /><![endif]-->	
	<!--[if gte IE 6]><link rel="stylesheet" type="text/css" media="screen" href="style_css/ie6.css" /><![endif]-->	
	<!--[if lte IE 5.5000]><link rel="stylesheet" type="text/css" media="screen" href="style_css/ie5.css" /><![endif]-->	


	<link rel="stylesheet" type="text/css" href="css/redmond/jquery-ui-1.11.4.custom.min.css">
	<script type="text/javascript" src="js/jquery-1.6.2.min.js"></script> 
	<script type="text/javascript" src="js/jquery-ui-1.11.4.custom.min.js"></script> 

</head>
<body data-gr-c-s-loaded="true">
<div id="global">

	<div id="header">

		<div id="logo">
			<img src="style_images/auswaertiges-amt-logo-220x120.gif" alt="Auswärtiges Amt">
		</div>
		<div id="logo-app" style="background-image:  url('images/auswaertigesamt.gif'); min-height: 54px; width: 78%;">
			&nbsp;
		</div>
		<div id="nav-main" style="min-height: 28px;">


<ul>
    <li><a href="extern/appointment_showMonth.do?request_locale=de&amp;locationCode=nowo&amp;realmId=1098&amp;categoryId=2266&amp;dateStr=25.08.2020" title="Diese Seite in Deutsch"><img src="images/flags/de.png" alt="Deutsche Fahne" title="Deutsche Fahne"></a></li>





        <li><a href="extern/choose_realmList.do?locationCode=nowo&amp;request_locale=ru" title="Russisch"><img src="images/flags/ru.png" alt="Flagge Russlands" title="Flagge Russlands"></a></li>

</ul>
		</div>		

	</div> <!-- end: #header -->			


	<div id="main" class="l-s">

		<div id="content">

			<div class="wrapper">	


<div style="font-size: 14pt; font-weight: bold; margin-bottom: 1em;">
	окно А
</div>


	<h2>
		Выберите дату (формат:день/месяц/год)
	</h2>






<h2>
	<a onclick="return startCommitRequest();" href="extern/appointment_showMonth.do?locationCode=nowo&amp;realmId=1098&amp;categoryId=2266&amp;dateStr=25.07.2020" style="margin-left: 2em; margin-right: 2em;"><img src="images/go-previous.gif"></a>
	08/2020
	<a onclick="return startCommitRequest();" href="extern/appointment_showMonth.do?locationCode=nowo&amp;realmId=1098&amp;categoryId=2266&amp;dateStr=25.09.2020" style="margin-left: 2em; margin-right: 2em;"><img src="images/go-next.gif"></a>
</h2>




		<div style="width: 100%;">

		</div>

		<div style="width: 100%;">

		</div>

		<div style="width: 100%;">

		</div>

		<div style="width: 100%;">

		</div>

		<div style="width: 100%;">

		</div>

		<div style="width: 100%;">

		</div>

		<div style="width: 100%;">

		</div>

		<div style="width: 100%;">

		</div>

		<div style="width: 100%;">

		</div>

		<div style="width: 100%;">

		</div>

		<div style="width: 100%;">

		</div>

		<div style="width: 100%;">

		</div>

		<div style="width: 100%;">

		</div>

		<div style="width: 100%;">

		</div>

		<div style="width: 100%;">

		</div>

		<div style="width: 100%;">

		</div>

		<div style="width: 100%;">

		</div>

		<div style="width: 100%;">

		</div>

		<div style="width: 100%;">

		</div>

		<div style="width: 100%;">

		</div>

		<div style="width: 100%;">

		</div>

		<div style="width: 100%;">

		</div>

		<div style="width: 100%;">

		</div>

		<div style="width: 100%;">

		</div>

		<div style="width: 100%;">

		</div>

		<div style="width: 100%;">

				<div style="float: left;">
					<h4>

						СРЕДА 26.08.2020
					</h4>
				</div>
				<div style="margin-left: 20%;">
					<a onclick="return startCommitRequest();" href="extern/appointment_showDay.do?locationCode=nowo&amp;realmId=1098&amp;categoryId=2266&amp;dateStr=26.08.2020" class="arrow">
						Запись на прием возможна
					</a>


					<hr style="clear: left;">
				</div>


		</div>

		<div style="width: 100%;">

				<div style="float: left;">
					<h4>

						ЧЕТВЕРГ 27.08.2020
					</h4>
				</div>
				<div style="margin-left: 20%;">
					<a onclick="return startCommitRequest();" href="extern/appointment_showDay.do?locationCode=nowo&amp;realmId=1098&amp;categoryId=2266&amp;dateStr=27.08.2020" class="arrow">
						Запись на прием возможна
					</a>


					<hr style="clear: left;">
				</div>


		</div>

		<div style="width: 100%;">

				<div style="float: left;">
					<h4>

						ПЯТНИЦА 28.08.2020
					</h4>
				</div>
				<div style="margin-left: 20%;">
					<a onclick="return startCommitRequest();" href="extern/appointment_showDay.do?locationCode=nowo&amp;realmId=1098&amp;categoryId=2266&amp;dateStr=28.08.2020" class="arrow">
						Запись на прием возможна
					</a>


					<hr style="clear: left;">
				</div>


		</div>

		<div style="width: 100%;">

		</div>

		<div style="width: 100%;">

		</div>

		<div style="width: 100%;">

		</div>







<script language="javascript" type="text/javascript">

$(function() {
	$("#commit-request").dialog({
		resizable : false,
		height : 200,
		width: 350,
		modal : true,
		autoOpen: false, 
		buttons : {
			/* none */
		},
		close: function( event, ui ) {
			$('#commit-request').dialog('open');
		}
	});
 	$( "#commit-request-progressbar" ).progressbar({
	  value: false
	});
});

function startCommitRequest(event) {

	$("#commit-request").css('cursor', 'progress');

	setTimeout("innerStartCommitRequest()", 500);

	return true;

}

function innerStartCommitRequest() {
	$('#commit-request').dialog('open');
}

</script>




			</div>

			<div class="bottom"></div>

		</div>

		<div id="context">

			<div class="wrapper">
				&nbsp;
			</div>

		</div>

	</div> <!-- end: #main -->
	<div id="footer">




<div style="min-height: 15px;">
	<ul>
		<li>RK-Termin&nbsp;1.2.36.1</li>
		<li style="margin-left: 5em;">

				<a href="extern/dsgvo.do?request_locale=ru" target="_blank" title="Информация о защите данных и правила пользования"><img src="images/flags/ru.png" alt="Информация о защите данных и правила пользования" title="Информация о защите данных и правила пользования">&nbsp; Информация
					о защите данных и правила пользования</a>
			 </li>
	</ul>
</div>



	</div>
</div>

<div class="ui-dialog ui-widget ui-widget-content ui-corner-all ui-front ui-draggable" tabindex="-1" role="dialog" aria-describedby="commit-request" style="display: none;" aria-labelledby="ui-id-1"><div class="ui-dialog-titlebar ui-widget-header ui-corner-all ui-helper-clearfix ui-draggable-handle"><span id="ui-id-1" class="ui-dialog-title">В обработке ... </span><button type="button" class="ui-button ui-widget ui-state-default ui-corner-all ui-button-icon-only ui-dialog-titlebar-close" role="button" title="Close"><span class="ui-button-icon-primary ui-icon ui-icon-closethick"></span><span class="ui-button-text">Close</span></button></div><div id="commit-request" class="ui-dialog-content ui-widget-content">
	<p>
		<span class="ui-icon ui-icon-alert" style="float: left; margin: 0 7px 20px 0; margin-bottom: 100px"></span>
		<span id="question">
			<b>подождите ...</b><br>Ваш запрос обрабатывается. Пожалуйста, дождитесь ответа. Перезагрузка страницы замедлит обработку.
		</span>

	</p>
	<div id="commit-request-progressbar" style="background: #7192b6;" class="ui-progressbar ui-widget ui-widget-content ui-corner-all ui-progressbar-indeterminate" role="progressbar" aria-valuemin="0">

		<div style="background: rgba(0,0,0,0) url('images/indet.gif'); opacity:0.25; height:2em;">
			&nbsp;
		</div>

	<div class="ui-progressbar-value ui-widget-header ui-corner-left" style="width: 100%;"><div class="ui-progressbar-overlay"></div></div></div>
</div></div></body></html>
"""

html_doc_with_time_slot = """
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en"><head>
	<base href="https://service2.diplo.de/rktermin/">
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=9; IE=10; IE=11">
	<title>
		RK-Termin - Kategorie
	</title>	
	<link rel="stylesheet" type="text/css" href="style_css/reset.css">	
	<link rel="stylesheet" type="text/css" media="screen" href="style_css/screen.css">	
	<link rel="stylesheet" type="text/css" media="print" href="style_css/print.css">	
	<link rel="stylesheet" type="text/css" media="screen" href="style_css/rktermin.css">

	<!--[if gte IE 7]><link rel="stylesheet" type="text/css" media="screen" href="style_css/ie7.css" /><![endif]-->	
	<!--[if gte IE 6]><link rel="stylesheet" type="text/css" media="screen" href="style_css/ie6.css" /><![endif]-->	
	<!--[if lte IE 5.5000]><link rel="stylesheet" type="text/css" media="screen" href="style_css/ie5.css" /><![endif]-->	


	<link rel="stylesheet" type="text/css" href="css/redmond/jquery-ui-1.11.4.custom.min.css">
	<script type="text/javascript" src="js/jquery-1.6.2.min.js"></script> 
	<script type="text/javascript" src="js/jquery-ui-1.11.4.custom.min.js"></script> 

</head>
<body data-gr-c-s-loaded="true">
<div id="global">

	<div id="header">

		<div id="logo">
			<img src="style_images/auswaertiges-amt-logo-220x120.gif" alt="Auswärtiges Amt">
		</div>
		<div id="logo-app" style="background-image:  url('images/auswaertigesamt.gif'); min-height: 54px; width: 78%;">
			&nbsp;
		</div>
		<div id="nav-main" style="min-height: 28px;">


<ul>

    <li><a href="extern/appointment_showDay.do?request_locale=de&amp;locationCode=nowo&amp;realmId=1098&amp;categoryId=2266&amp;dateStr=&amp;openingPeriodId=" title="Diese Seite in Deutsch"><img src="images/flags/de.png" alt="Deutsche Fahne" title="Deutsche Fahne"></a></li>
    <li><a href="extern/appointment_showDay.do?request_locale=de&amp;locationCode=nowo&amp;realmId=1098&amp;categoryId=2266&amp;dateStr=&amp;openingPeriodId=" title="Diese Seite in Deutsch"><img src="images/flags/de.png" alt="Deutsche Fahne" title="Deutsche Fahne"></a></li>





        <li><a href="extern/choose_realmList.do?locationCode=nowo&amp;request_locale=ru" title="Russisch"><img src="images/flags/ru.png" alt="Flagge Russlands" title="Flagge Russlands"></a></li>

</ul>

		</div>		

	</div> <!-- end: #header -->			


	<div id="main" class="l-s">

		<div id="content">

			<div class="wrapper">	

<script>
	$(function() {
		$("#date").datepicker({
			dateFormat : 'dd.mm.yy',
			numberOfMonths : 3,
			showButtonPanel : true
		});
	});
</script>
<div style="font-size: 14pt; font-weight: bold; margin-bottom: 1em;">
	окно А
</div>




<h2>
	Выберите дату собеседования
	<a onclick="return startCommitRequest();" href="extern/appointment_showMonth.do?locationCode=nowo&amp;realmId=1098&amp;categoryId=2266&amp;dateStr=25.08.2020" class="arrow" style="margin-left: 3em;">Месяцы</a>
</h2>
<div style="width: 100%;">
	<div style="margin-left: 20%;">
		Вы можете записаться на собеседование с 14.08.2020 до 10.09.2020
	</div>
</div>
<div>
	<div style="float: left; width: 20%; text-align: left; margin-left: 2em;">


			<a onclick="return startCommitRequest();" href="extern/appointment_showDay.do?locationCode=nowo&amp;realmId=1098&amp;categoryId=2266&amp;dateStr=25.08.2020" style="margin-left: 2em; margin-right: 2em;"><img src="images/go-previous.gif"></a>

	</div>
	<div style="float: right; width: 20%; text-align: right; margin-right: 2em;">

		<a onclick="return startCommitRequest();" href="extern/appointment_showDay.do?locationCode=nowo&amp;realmId=1098&amp;categoryId=2266&amp;dateStr=27.08.2020" style="margin-left: 2em; margin-right: 2em;"><img src="images/go-next.gif"></a>
	</div>
	<div style="">

		<form id="calendarform" name="calendarform" action="/rktermin/extern/appointment_showDay.do" method="get">
			<div id="wwgrp_date" class="input text s">
				<label for="date" class="label">Mittwoch:</label>
				<input type="text" name="date" value="26.08.2020" id="date" onchange="submit()" class="hasDatepicker">
				<span class="hint">Формат даты:&nbsp;дд.мм.гггг</span>
			</div>
			<input type="hidden" name="locationCode" value="nowo" id="calendarform_locationCode">
			<input type="hidden" name="realmId" value="1098" id="calendarform_realmId">
			<input type="hidden" name="categoryId" value="2266" id="calendarform_categoryId">
			<input type="hidden" name="openingPeriodId" value="" id="calendarform_openingPeriodId">
			<input type="hidden" name="rebooking" value="" id="calendarform_rebooking">
			<input type="hidden" name="token" value="" id="calendarform_token">
		</form>



	</div>
</div>
<br clear="all">










		<div style="width: 100%;">
			<div style="float: left;">
				<h4>
					09:15
					—
					10:00
				</h4>
			</div>

				<div style="margin-left: 20%;">
					<h5>
						В указанный период запись невозможна
					</h5>
				</div>




		</div>

			<hr style="clear: left;">


		<div style="width: 100%;">
			<div style="float: left;">
				<h4>
					10:00
					—
					10:45
				</h4>
			</div>

				<div style="margin-left: 20%;">
					<h5>
						В указанный период запись невозможна
					</h5>
				</div>




		</div>

			<hr style="clear: left;">


		<div style="width: 100%;">
			<div style="float: left;">
				<h4>
					10:45
					—
					11:30
				</h4>
			</div>



				<div style="margin-left: 20%;">
					Количество свободных мест: 1
					<a onclick="return startCommitRequest();" href="extern/appointment_showForm.do?locationCode=nowo&amp;realmId=1098&amp;categoryId=2266&amp;dateStr=26.08.2020&amp;openingPeriodId=51082" class="arrow">Записаться на прием</a>
				</div>


		</div>

			<hr style="clear: left;">


		<div style="width: 100%;">
			<div style="float: left;">
				<h4>
					11:30
					—
					12:15
				</h4>
			</div>



				<div style="margin-left: 20%;">
					Количество свободных мест: 1
					<a onclick="return startCommitRequest();" href="extern/appointment_showForm.do?locationCode=nowo&amp;realmId=1098&amp;categoryId=2266&amp;dateStr=26.08.2020&amp;openingPeriodId=51087" class="arrow">Записаться на прием</a>
				</div>


		</div>

			<hr style="clear: left;">


		<div style="width: 100%;">
			<div style="float: left;">
				<h4>
					13:00
					—
					13:45
				</h4>
			</div>



				<div style="margin-left: 20%;">
					Количество свободных мест: 1
					<a onclick="return startCommitRequest();" href="extern/appointment_showForm.do?locationCode=nowo&amp;realmId=1098&amp;categoryId=2266&amp;dateStr=26.08.2020&amp;openingPeriodId=51092" class="arrow">Записаться на прием</a>
				</div>


		</div>







<script language="javascript" type="text/javascript">

$(function() {
	$("#commit-request").dialog({
		resizable : false,
		height : 200,
		width: 350,
		modal : true,
		autoOpen: false, 
		buttons : {
			/* none */
		},
		close: function( event, ui ) {
			$('#commit-request').dialog('open');
		}
	});
 	$( "#commit-request-progressbar" ).progressbar({
	  value: false
	});
});

function startCommitRequest(event) {

	$("#commit-request").css('cursor', 'progress');

	setTimeout("innerStartCommitRequest()", 500);

	return true;

}

function innerStartCommitRequest() {
	$('#commit-request').dialog('open');
}

</script>




			</div>

			<div class="bottom"></div>

		</div>

		<div id="context">

			<div class="wrapper">
				&nbsp;
			</div>

		</div>

	</div> <!-- end: #main -->
	<div id="footer">




<div style="min-height: 15px;">
	<ul>
		<li>RK-Termin&nbsp;1.2.36.1</li>
		<li style="margin-left: 5em;">

				<a href="extern/dsgvo.do?request_locale=ru" target="_blank" title="Информация о защите данных и правила пользования"><img src="images/flags/ru.png" alt="Информация о защите данных и правила пользования" title="Информация о защите данных и правила пользования">&nbsp; Информация
					о защите данных и правила пользования</a>
			 </li>
	</ul>
</div>



	</div>
</div>

<div id="ui-datepicker-div" class="ui-datepicker ui-widget ui-widget-content ui-helper-clearfix ui-corner-all"></div><div class="ui-dialog ui-widget ui-widget-content ui-corner-all ui-front ui-draggable" tabindex="-1" role="dialog" aria-describedby="commit-request" style="display: none;" aria-labelledby="ui-id-1"><div class="ui-dialog-titlebar ui-widget-header ui-corner-all ui-helper-clearfix ui-draggable-handle"><span id="ui-id-1" class="ui-dialog-title">В обработке ... </span><button type="button" class="ui-button ui-widget ui-state-default ui-corner-all ui-button-icon-only ui-dialog-titlebar-close" role="button" title="Close"><span class="ui-button-icon-primary ui-icon ui-icon-closethick"></span><span class="ui-button-text">Close</span></button></div><div id="commit-request" class="ui-dialog-content ui-widget-content">
	<p>
		<span class="ui-icon ui-icon-alert" style="float: left; margin: 0 7px 20px 0; margin-bottom: 100px"></span>
		<span id="question">
			<b>подождите ...</b><br>Ваш запрос обрабатывается. Пожалуйста, дождитесь ответа. Перезагрузка страницы замедлит обработку.
		</span>

	</p>
	<div id="commit-request-progressbar" style="background: #7192b6;" class="ui-progressbar ui-widget ui-widget-content ui-corner-all ui-progressbar-indeterminate" role="progressbar" aria-valuemin="0">

		<div style="background: rgba(0,0,0,0) url('images/indet.gif'); opacity:0.25; height:2em;">
			&nbsp;
		</div>

	<div class="ui-progressbar-value ui-widget-header ui-corner-left" style="width: 100%;"><div class="ui-progressbar-overlay"></div></div></div>
</div></div></body></html>
"""

html_doc_with_form = """
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en"><head>
	<base href="https://service2.diplo.de/rktermin/">
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=9; IE=10; IE=11">
	<title>
		RK-Termin
	</title>	
	<link rel="stylesheet" type="text/css" href="style_css/reset.css">	
	<link rel="stylesheet" type="text/css" media="screen" href="style_css/screen.css">	
	<link rel="stylesheet" type="text/css" media="print" href="style_css/print.css">	
	<link rel="stylesheet" type="text/css" media="screen" href="style_css/rktermin.css">
	
	<!--[if gte IE 7]><link rel="stylesheet" type="text/css" media="screen" href="style_css/ie7.css" /><![endif]-->	
	<!--[if gte IE 6]><link rel="stylesheet" type="text/css" media="screen" href="style_css/ie6.css" /><![endif]-->	
	<!--[if lte IE 5.5000]><link rel="stylesheet" type="text/css" media="screen" href="style_css/ie5.css" /><![endif]-->	


	<link rel="stylesheet" type="text/css" href="css/redmond/jquery-ui-1.11.4.custom.min.css">
	<script type="text/javascript" src="js/jquery-1.6.2.min.js"></script> 
	<script type="text/javascript" src="js/jquery-ui-1.11.4.custom.min.js"></script> 
		
</head>
<body>
<div id="global">

	<div id="header">
	
		<div id="logo">
			<img src="style_images/auswaertiges-amt-logo-220x120.gif" alt="Auswärtiges Amt">
		</div>
		<div id="logo-app" style="background-image:  url('images/auswaertigesamt.gif'); min-height: 54px; width: 78%;">
			&nbsp;
		</div>
		<div id="nav-main" style="min-height: 28px;">
		

<ul>
	<li></li>
</ul>
		</div>		
	
	</div> <!-- end: #header -->			

	
	<div id="main" class="l-s">
			
		<div id="content">
		
			<div class="wrapper">	
			



<div style="font-size: 14pt; font-weight: bold; margin-bottom: 1em;">
Национальная виза
</div>








	<fieldset>
		<legend>Новая дата собеседования</legend>
		
		
		
		
		
			<div style="font-size: 120%; float: left; width: 20%;">
				Дата/время:
			</div>
			<div style="font-weight: bold;">
				26.08.2020
				10:00 
				—
				10:45
			</div><br style="clear: both;">
			<div style="font-size: 120%; float: left; width: 20%;">
				Место:
			</div>
			<div style="font-weight: bold;">
				Nowosibirsk
			</div><br style="clear: both;">
		
		
		        
<form id="appointment_newAppointmentForm" name="appointment_newAppointmentForm" onsubmit="startCommitRequest();" action="/rktermin/extern/appointment_showForm.do" method="post" class="top">
			<div id="wwgrp_appointment_newAppointmentForm_lastname" class="input text s">
<div id="wwlbl_appointment_newAppointmentForm_lastname" class="wwlbl">
<label for="appointment_newAppointmentForm_lastname" class="label">        Фамилия:
</label></div> 
<div id="wwctrl_appointment_newAppointmentForm_lastname">
<input type="text" name="lastname" value="" id="appointment_newAppointmentForm_lastname" class="input text s" onkeypress="doNothing(event)"></div> </div>

			<div id="wwgrp_appointment_newAppointmentForm_firstname" class="input text s">
<div id="wwlbl_appointment_newAppointmentForm_firstname" class="wwlbl">
<label for="appointment_newAppointmentForm_firstname" class="label">        Имя:
</label></div> 
<div id="wwctrl_appointment_newAppointmentForm_firstname">
<input type="text" name="firstname" value="" id="appointment_newAppointmentForm_firstname" class="input text s" onkeypress="doNothing(event)"></div> </div>

			<div id="wwgrp_appointment_newAppointmentForm_email" class="input text s">
<div id="wwlbl_appointment_newAppointmentForm_email" class="wwlbl">
<label for="appointment_newAppointmentForm_email" class="label">        Электронная почта:
</label></div> 
<div id="wwctrl_appointment_newAppointmentForm_email">
<input type="text" name="email" value="" id="appointment_newAppointmentForm_email" class="input text s" onkeypress="doNothing(event)"></div> </div>

			<div id="wwgrp_appointment_newAppointmentForm_emailrepeat" class="input text s">
<div id="wwlbl_appointment_newAppointmentForm_emailrepeat" class="wwlbl">
<label for="appointment_newAppointmentForm_emailrepeat" class="label">        Повторить адрес электронной почты:
</label></div> 
<div id="wwctrl_appointment_newAppointmentForm_emailrepeat">
<input type="text" name="emailrepeat" value="" id="appointment_newAppointmentForm_emailrepeat" class="input text s" onkeypress="doNothing(event)" onpaste="return false;" autocomplete="off"></div> </div>

			
			
			 
			
			
				
			
				
					
						<div id="wwgrp_appointment_newAppointmentForm_fields_0__content" class="input text l">
<div id="wwlbl_appointment_newAppointmentForm_fields_0__content" class="wwlbl">
<label for="appointment_newAppointmentForm_fields_0__content" class="label"><span class="required">*</span>        проживание:
</label></div> 
<div id="wwctrl_appointment_newAppointmentForm_fields_0__content">
<input type="text" name="fields[0].content" value="" id="appointment_newAppointmentForm_fields_0__content" class="input text l" onkeypress="doNothing(event)"></div> </div>

					
					
				

				
				
				
				
				
				<input type="hidden" name="fields[0].definitionId" value="5481" id="appointment_newAppointmentForm_fields_0__definitionId">
				<input type="hidden" name="fields[0].index" value="0" id="appointment_newAppointmentForm_fields_0__index">
			
				
			
				
					
						<div id="wwgrp_appointment_newAppointmentForm_fields_1__content" class="input text l">
<div id="wwlbl_appointment_newAppointmentForm_fields_1__content" class="wwlbl">
<label for="appointment_newAppointmentForm_fields_1__content" class="label"><span class="required">*</span>        номер заграничного паспорта:
</label></div> 
<div id="wwctrl_appointment_newAppointmentForm_fields_1__content">
<input type="text" name="fields[1].content" value="" id="appointment_newAppointmentForm_fields_1__content" class="input text l" onkeypress="doNothing(event)"></div> </div>

					
					
				

				
				
				
				
				
				<input type="hidden" name="fields[1].definitionId" value="5467" id="appointment_newAppointmentForm_fields_1__definitionId">
				<input type="hidden" name="fields[1].index" value="1" id="appointment_newAppointmentForm_fields_1__index">
			
				
			
				

				
				
				
				
					
						<div id="wwgrp_appointment_newAppointmentForm_fields_2__content" class="input select l">
<div id="wwlbl_appointment_newAppointmentForm_fields_2__content" class="wwlbl">
<label for="appointment_newAppointmentForm_fields_2__content" class="label"><span class="required">*</span>        Цель путешествия:
</label></div> 
<div id="wwctrl_appointment_newAppointmentForm_fields_2__content">
<select name="fields[2].content" id="appointment_newAppointmentForm_fields_2__content" class="input select l">
    <option value=""></option>
    <option value="Familienzusammenführung">Familienzusammenführung</option>
    <option value="Eheschließung">Eheschließung</option>
    <option value="Studium">Studium</option>
    <option value="Sprachkurs">Sprachkurs</option>
    <option value="Arbeitsaufnahme">Arbeitsaufnahme</option>
    <option value="Wiedereinreise">Wiedereinreise</option>
    <option value="Sonstiges">Sonstiges</option>


</select>

</div> </div>
					
					
					
				
				
				<input type="hidden" name="fields[2].definitionId" value="5473" id="appointment_newAppointmentForm_fields_2__definitionId">
				<input type="hidden" name="fields[2].index" value="2" id="appointment_newAppointmentForm_fields_2__index">
			
			<div>
				
				<div class="input text s">
					<captcha>
<div id="_1493842361" style="background:white url('data:image/jpg;base64,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') no-repeat scroll left top;width:350px;height:50px;margin:2em;display:block;">&nbsp;</div>
</captcha>

 

				</div>
				
				<div class="input submit left">
					<input type="submit" value="Загрузить новую картинку" id="appointment_newAppointmentForm_form_newappointment_refreshcaptcha" name="action:appointment_refreshCaptcha">

				</div>
			</div>
			<div id="wwgrp_appointment_newAppointmentForm_captchaText" class="input text s">
<div id="wwlbl_appointment_newAppointmentForm_captchaText" class="wwlbl">
<label for="appointment_newAppointmentForm_captchaText" class="label">        Введите код с картинки:
</label></div> 
<div id="wwctrl_appointment_newAppointmentForm_captchaText">
<input type="text" name="captchaText" value="" id="appointment_newAppointmentForm_captchaText" class="input text s" onkeypress="checkKey(event)"></div> </div>

			<input type="hidden" name="locationCode" value="jeka" id="appointment_newAppointmentForm_locationCode">
			<input type="hidden" name="realmId" value="881" id="appointment_newAppointmentForm_realmId">
			<input type="hidden" name="categoryId" value="1677" id="appointment_newAppointmentForm_categoryId">
			<input type="hidden" name="openingPeriodId" value="51077" id="appointment_newAppointmentForm_openingPeriodId">
			<input type="hidden" name="date" value="26.08.2020" id="appointment_newAppointmentForm_date">
			<input type="hidden" name="dateStr" value="26.08.2020" id="appointment_newAppointmentForm_dateStr">
			
				
				
				
				
			    <script type="text/javascript">
			    function checkKey(event){   
			        if(event.keyCode == 13){
			            document.appointment_newAppointmentForm.action="extern/appointment_addAppointment.do";
			            document.appointment_newAppointmentForm.submit();
			            event.preventDefault();
			        }
			    }
			    function doNothing(event){   
			        if(event.keyCode == 13){
			        	event.preventDefault();
			        	return false;
			        }
			    }
			      </script>
			<div class="input submit left">
	<input type="submit" value="Сохранить" id="appointment_newAppointmentForm_appointment_addAppointment" name="action:appointment_addAppointment">
<input type="submit" value="Отменить" id="appointment_newAppointmentForm_appointment_cancelAddAppointment" name="action:appointment_cancelAddAppointment">
</div>      

		
		</form>



	</fieldset>





<script language="javascript" type="text/javascript">

$(function() {
	$("#commit-request").dialog({
		resizable : false,
		height : 200,
		width: 350,
		modal : true,
		autoOpen: false, 
		buttons : {
			/* none */
		},
		close: function( event, ui ) {
			$('#commit-request').dialog('open');
		}
	});
 	$( "#commit-request-progressbar" ).progressbar({
	  value: false
	});
});

function startCommitRequest(event) {
	
	$("#commit-request").css('cursor', 'progress');
	
	setTimeout("innerStartCommitRequest()", 500);

	return true;
	
}

function innerStartCommitRequest() {
	$('#commit-request').dialog('open');
}

</script>




			</div>
			
			<div class="bottom"></div>
			
		</div>
		
		<div id="context">
		
			<div class="wrapper">
				&nbsp;
			</div>
			
		</div>
		
	</div> <!-- end: #main -->
	<div id="footer">
		



<div style="min-height: 15px;">
	<ul>
		<li>RK-Termin&nbsp;1.2.36.1</li>
		<li style="margin-left: 5em;">
			    
				<a href="extern/dsgvo.do?request_locale=ru" target="_blank" title="Информация о защите данных и правила пользования"><img src="images/flags/ru.png" alt="Информация о защите данных и правила пользования" title="Информация о защите данных и правила пользования">&nbsp; Информация
					о защите данных и правила пользования</a>
			 </li>
	</ul>
</div>



	</div>
</div>

<div class="ui-dialog ui-widget ui-widget-content ui-corner-all ui-front ui-draggable" tabindex="-1" role="dialog" aria-describedby="commit-request" aria-labelledby="ui-id-1" style="display: none;"><div class="ui-dialog-titlebar ui-widget-header ui-corner-all ui-helper-clearfix ui-draggable-handle"><span id="ui-id-1" class="ui-dialog-title">В обработке ... </span><button type="button" class="ui-button ui-widget ui-state-default ui-corner-all ui-button-icon-only ui-dialog-titlebar-close" role="button" title="Close"><span class="ui-button-icon-primary ui-icon ui-icon-closethick"></span><span class="ui-button-text">Close</span></button></div><div id="commit-request" class="ui-dialog-content ui-widget-content">
	<p>
		<span class="ui-icon ui-icon-alert" style="float: left; margin: 0 7px 20px 0; margin-bottom: 100px"></span>
		<span id="question">
			<b>подождите ...</b><br>Ваш запрос обрабатывается. Пожалуйста, дождитесь ответа. Перезагрузка страницы замедлит обработку.
		</span>
		
	</p>
	<div id="commit-request-progressbar" style="background: #7192b6;" class="ui-progressbar ui-widget ui-widget-content ui-corner-all ui-progressbar-indeterminate" role="progressbar" aria-valuemin="0">
	
		<div style="background: rgba(0,0,0,0) url('images/indet.gif'); opacity:0.25; height:2em;">
			&nbsp;
		</div>
	
	<div class="ui-progressbar-value ui-widget-header ui-corner-left" style="width: 100%;"><div class="ui-progressbar-overlay"></div></div></div>
</div></div></body></html>"""

hidden_inputs_target = {
    'fields[0].definitionId': '5481',
    'fields[0].index': '0',
    'fields[1].definitionId': '5467',
    'fields[1].index': '1',
    'fields[2].definitionId': '5473',
    'fields[2].index': '2',
    'locationCode': 'jeka',
    'realmId': '881',
    'categoryId': '1677',
    'openingPeriodId': '51077',
    'date': '26.08.2020',
    'dateStr': '26.08.2020'
}

html_doc_with_error ="""
<!DOCTYPE html
	PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">

<head>
	<base href="https://service2.diplo.de/rktermin/" />
	<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
	<meta http-equiv="X-UA-Compatible" content="IE=9; IE=10; IE=11" />
	<title>
		RK-Termin
	</title>
	<link rel="stylesheet" type="text/css" href="style_css/reset.css" />
	<link rel="stylesheet" type="text/css" media="screen" href="style_css/screen.css" />
	<link rel="stylesheet" type="text/css" media="print" href="style_css/print.css" />
	<link rel="stylesheet" type="text/css" media="screen" href="style_css/rktermin.css" />

	<!--[if gte IE 7]><link rel="stylesheet" type="text/css" media="screen" href="style_css/ie7.css" /><![endif]-->
	<!--[if gte IE 6]><link rel="stylesheet" type="text/css" media="screen" href="style_css/ie6.css" /><![endif]-->
	<!--[if lte IE 5.5000]><link rel="stylesheet" type="text/css" media="screen" href="style_css/ie5.css" /><![endif]-->


	<link rel="stylesheet" type="text/css" href="css/redmond/jquery-ui-1.11.4.custom.min.css" />
	<script type="text/javascript" src="js/jquery-1.6.2.min.js"></script>
	<script type="text/javascript" src="js/jquery-ui-1.11.4.custom.min.js"></script>

</head>

<body>
	<div id="global">

		<div id="header">

			<div id="logo">
				<img src="style_images/auswaertiges-amt-logo-220x120.gif" alt="Auswärtiges Amt" />
		</div>
				<div id="logo-app"
					style="background-image:  url('images/auswaertigesamt.gif'); min-height: 54px; width: 78%;">
					&nbsp;
				</div>
				<div id="nav-main" style="min-height: 28px;">


					<ul>
						<li></li>
					</ul>
				</div>

			</div> <!-- end: #header -->


			<div id="main" class="l-s">

				<div id="content">

					<div class="wrapper">


						<p style="font-size: 120%; color: red;">
							При обработке Вашей записи на прием выявлена ошибка. Причиной может являться, например, то,
							что окно браузера было открыто слишком долго или в строку с доменом страницы были внесены
							изменения. Закройте окно и начните ввод снова.
							<br />
							<br />
							<br />
	ref-id: 51542F538B89B53B1825B484CEC1500C
</p>
					</div>

					<div class="bottom"></div>

				</div>

				<div id="context">

					<div class="wrapper">
						&nbsp;
					</div>

				</div>

			</div> <!-- end: #main -->
			<div id="footer">




				<div style="min-height: 15px;">
					<ul>
						<li>RK-Termin&nbsp;1.2.36.1</li>
						<li style="margin-left: 5em;">

							<a href="extern/dsgvo.do?request_locale=ru" target="_blank"
								title="Информация о защите данных и правила пользования"><img
					src="images/flags/ru.png"
					alt="Информация о защите данных и правила пользования"
					title="Информация о защите данных и правила пользования" />&nbsp; Информация
					о защите данных и правила пользования</a>
						</li>
					</ul>
				</div>



			</div>
		</div>
</body>

</html>
"""
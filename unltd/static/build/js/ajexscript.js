var c = 0;
var e = 0;
function check() {
    if(document.getElementById('password').value ==
            document.getElementById('confirm_password').value ) {
            document.getElementById('message').innerHTML = "";
            if(e==0)
            {
             document.getElementById('uprofileSetting').disabled = false;
             }
            c=0
        } else {
            document.getElementById('message').style.color = 'red';
            document.getElementById('message').innerHTML = "no match";
            document.getElementById('uprofileSetting').disabled = true;
            c=1
        }
       }

$('#submit').click(function(){

    document.getElementById("submit").disabled = true;
     if(e==1 || c==1)
     {
 	    alert('Please Correct details')
 	    return
 	 }
 	 var user = $('#useras').val();
 	if(user == 'Staff')
 	{
 	    Staff();
    }
    if(user == 'Member')
    {
        Member();
    }
    if(user == 'Vendor')
    {
        Vendor();
    }
   });

$('#email').on('blur', function(){
 	var email = $('#email').val();
 	if (email == '') {
 		email_state = false;
 		return;
 	}
 	$.ajax({
      url: 'validateemail',
      type: 'post',
      data: {
      	'email' : email,
      	'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]').val()
      },
      success: function(response){
      	if (response == 'taken' ) {
           document.getElementById('error').style.color = 'red';
            document.getElementById('error').innerHTML = "Already Taken";
            e=1;
            }else{
             document.getElementById('error').innerHTML = "";
             e=0;
      	    }
      }
 	});
 });

$("#phone").keypress(function(){
    var ph = $('#phone').val();
//    newph = ph.replace("'","");
//    document.getElementById('phone').value = newph;
  if(ph.length<1)
  {
    document.getElementById('phone').value = "+";
  }
  if(ph.length==1 && ph != "+")
  {
    document.getElementById('phone').value = "+"+ph;
  }
});

$("#phone").change(function(){
    var ph = $('#phone').val();
//    newph = ph.replace("'","");
//    document.getElementById('phone').value = newph;
  if(ph.length<1)
  {
    document.getElementById('phone').value = "+";
  }

});

function Staff(){
    var user = $('#useras').val();
    var dname = $('#dname').val();
    var email = $('#email').val();
    var country = $('#country').val();
    var state = $('#state').val();
    var city = $('#city').val();
    var postal = $('#postal').val();
    var address = $('#address').val();
    var phone = $('#phone').val();
    var password = $('#password').val();
    var privilege = 'Not set'//$('#privilege').val();
    var department = 'Not Set'//$('#department').val();
    var nurl = $('#url').val();
//     if(user == '' || dname == '' || email == '' || state =='' || city == '' || postal == '' || address =='' || phone== '' || password == '' || privilege == '' || department == '' )
//      {
//       alert('All fields are required')
//       return
//       }
    $.ajax({
      url: 'createaccount',
      type: 'post',
       data: {
      	'dname' :dname,
      	'email' :email,
      	'country' :country,
      	'state' :state,
      	'city' :city,
      	'postal' :postal,
      	'address' :address,
      	'phone' :phone,
        'privilege' :privilege,
         'department' :department,
         'password' :password,
         'user' :   user,
      	 'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]').val()
      },
      success: function(response){
        document.getElementById("submit").disabled = false;
        if(response == 'Saved')
        {
            window.location.replace(nurl);
        }

      }
 	});
}

function Member(){
    var user = $('#useras').val();
    var dname = $('#dname').val();
    var email = $('#email').val();
    var country = $('#country').val();
    var state = $('#state').val();
    var city = $('#city').val();
    var postal = $('#postal').val();
    var address = $('#address').val();
    var phone = $('#phone').val();
    var password = $('#password').val();
    var rdate = $('#rdate').val();
    var nurl = $('#url').val();
    gender=$("input[name='gender']:checked").val();
    if(user == '' || dname == '' || email == '' || state =='' || city == '' || postal == '' || address =='' || phone== '' || password == '' || rdate == '' )
    {
     alert('All fields are required')
     return
     }
    $.ajax({
      url: 'createaccount',
      type: 'post',
       data: {
      	'dname' :dname,
      	'email' :email,
      	'country' :country,
      	'state' :state,
      	'city' :city,
      	'postal' :postal,
      	'address' :address,
      	'phone' :phone,
        'rdate' :rdate,
         'gender' :gender,
         'password' :password,
         'user' :   user,
      	 'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]').val()
      },
      success: function(response){
        document.getElementById("submit").disabled = false;
        if(response == 'Saved')
        {
            window.location.replace(nurl);
        }
      }
 	});
}

function Vendor(){
    var user = $('#useras').val();
    var dname = $('#dname').val();
    var email = $('#email').val();
    var country = $('#country').val();
    var state = $('#state').val();
    var city = $('#city').val();
    var postal = $('#postal').val();
    var address = $('#address').val();
    var phone = $('#phone').val();
    var password = $('#password').val();
    var bname = $('#bname').val();
    var bemail = $('#bemail').val();
    var bphone = $('#bphone').val();
    var industry = $('#industry').val();
    var sname = $('#sname').val();
    var baddress = $('#baddress').val();
    var nurl = $('#url').val();
//    if(user == '' || dname == '' || email == '' || state =='' || city == '' || postal == '' || address =='' || phone== '' || password == '' || bname == '' || bemail == '' || bphone == '' || industry ==''|| sname == ''|| baddress=='')
//     {
//      alert('All fields are required')
//      return
//     }
    $.ajax({

      url: 'createaccount',
      type: 'post',
       data: {
      	'dname' :dname,
      	'email' :email,
      	'country' :country,
      	'state' :state,
      	'city' :city,
      	'postal' :postal,
      	'address' :address,
      	'phone' :phone,
         'password' :password,
         'user' :   user,
         'bname' : bname,
         'bemail' : bemail,
         'bphone' : bphone,
         'industry' : industry,
         'sname' : sname,
         'baddress' : baddress,
      	 'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]').val()
      },
      success: function(response){
        document.getElementById("submit").disabled = false;
        alert(response);
        location.reload(true);
        if(response == 'Saved')
        {
            window.location.replace(nurl);
        }
      }
 	});
}

//validate password for profile
$('#opassword').on('blur', function(){
 	var password = $('#opassword').val();
 	if (password == '') {
 		return;
 	}
 	$.ajax({
      url: 'validatepass',
      type: 'post',
      data: {
      	'password' : password,
      	'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]').val()
      },
      success: function(response){
      	if (response == 'notmatch' ) {
           document.getElementById('error').style.color = 'red';
            document.getElementById('error').innerHTML = "Password Not Correct";
            document.getElementById('uprofileSetting').disabled = true;
            e=1;
            }else{
             document.getElementById('error').innerHTML = "";
             if(c==0){
              document.getElementById('uprofileSetting').disabled = false;
              }
             e=0;
      	  }
      }
 	});
 });


//Settings Work paypal

$('#btnedit').click(function(){
 	var selectindex=document.querySelector('input[name="selectedindex"]:checked').value;
    var email = $('#'+selectindex+'').html();
    try{
        document.getElementById('nmailpaypal').value = email;
    }
    catch(err){
        document.getElementById('nmailstrip').value = email;
    }

});

$('#btnUpstrip').click(function(){
  //  document.getElementById("pypalbtnupdate").disabled = false;
 	var selectindex = 'No'
 	selectindex = document.querySelector('input[name="selectedindex"]:checked').value;
    var mail = $('#nmailstrip').val();
     $.ajax({
      url: '/unltd/strip/',
      type: 'post',
       data: {
      	'mailstrip' :mail,
      	'upid' :selectindex,
      	'act': 'update',
      	 'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]').val()
      },
      success: function(response){
        location.reload(true);
      }
 	});
});
$('#btndelpaypal').click(function(){
  //  document.getElementById("pypalbtnupdate").disabled = false;
 	var selectindex = 'No'
 	selectindex = document.querySelector('input[name="selectedindex"]:checked').value;
    var mail = $('#mailpaypal').val();
     $.ajax({
      url: '/unltd/paypal/',
      type: 'post',
       data: {
      	'mailpaypal' :mail,
      	'upid' :selectindex,
      	'act': 'del',
      	 'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]').val()
      },
      success: function(response){
       // document.getElementById("pypalbtnupdate").disabled = false;
        location.reload(true);
      }
 	});
});

$('#btnUppaypal').click(function(){
  //  document.getElementById("pypalbtnupdate").disabled = false;
 	var selectindex = 'No'
 	selectindex = document.querySelector('input[name="selectedindex"]:checked').value;
    var mail = $('#nmailpaypal').val();
     $.ajax({
      url: '/unltd/paypal/',
      type: 'post',
       data: {
      	'mailpaypal' :mail,
      	'upid' :selectindex,
      	'act': 'update',
      	 'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]').val()
      },
      success: function(response){
        location.reload(true);
      }
 	});
});

$('#btnactpaypal').click(function(){
  //  document.getElementById("pypalbtnupdate").disabled = false;
 	var selectindex = 'No'
 	selectindex = document.querySelector('input[name="selectedindex"]:checked').value;
    var mail = $('#mailpaypal').val();
     $.ajax({
      url: '/unltd/paypal/',
      type: 'post',
       data: {
      	'mailpaypal' :mail,
      	'upid' :selectindex,
      	'act': 'activate',
      	 'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]').val()
      },
      success: function(response){
        location.reload(true);
      }
 	});
});
//paypal end

$('#btnactstrip').click(function(){
  //  document.getElementById("pypalbtnupdate").disabled = false;
 	var selectindex = 'No'
 	selectindex = document.querySelector('input[name="selectedindex"]:checked').value;
    var mail = $('#mailstrip').val();
     $.ajax({
      url: '/unltd/strip/',
      type: 'post',
       data: {
      	'mailstrip' :mail,
      	'upid' :selectindex,
      	'act': 'activate',
      	 'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]').val()
      },
      success: function(response){
        location.reload(true);
      }
 	});
});

$('#btnactbank').click(function(){
 	var selectindex = 'No'
 	selectindex = document.querySelector('input[name="selectedindex"]:checked').value;
     $.ajax({
      url: '/unltd/payment/',
      type: 'post',
       data: {
      	'upid' :selectindex,
      	'act': 'activate',
      	 'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]').val()
      },
      success: function(response){
        location.reload(true);
      }
 	});
});

$('#btnUpbank').click(function(){
  //  document.getElementById("pypalbtnupdate").disabled = false;
 	var selectindex = 'No'
 	selectindex = document.querySelector('input[name="selectedindex"]:checked').value;
    var bankname = $('#nNameBank').val();
    var accname = $('#nNameAcc').val();
    var accno = $('#nAccNo').val();
    var Ibanno = $('#nIbanNo').val();
     $.ajax({
      url: '/unltd/payment/',
      type: 'post',
       data: {
       'bankname': bankname,
       'accname': accname,
       'accno': accno,
       'Ibanno': Ibanno,
      	'upid' :selectindex,
      	'act': 'update',
      	 'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]').val()
      },
      success: function(response){
        location.reload(true);
      }
 	});
});

$('#btnactsms').click(function(){
 	var selectindex = 'No'
 	selectindex = document.querySelector('input[name="selectedindex"]:checked').value;
     $.ajax({
      url: '/unltd/sms_setup/',
      type: 'post',
       data: {
      	'upid' :selectindex,
      	'act': 'activate',
      	 'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]').val()
      },
      success: function(response){
        location.reload(true);
      }
 	});
});

$('#btndelsms').click(function(){
 	var selectindex = 'No'
 	selectindex = document.querySelector('input[name="selectedindex"]:checked').value;
     $.ajax({
      url: '/unltd/sms_setup/',
      type: 'post',
       data: {
      	'upid' :selectindex,
      	'act': 'del',
      	 'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]').val()
      },
      success: function(response){
       // document.getElementById("pypalbtnupdate").disabled = false;
        location.reload(true);
      }
 	});
});

$('#btnUpsms').click(function(){
  //  document.getElementById("pypalbtnupdate").disabled = false;
 	var selectindex = 'No'
 	selectindex = document.querySelector('input[name="selectedindex"]:checked').value;
    var napiservice = $('#napiservice').val();
    var napikey = $('#napikey').val();
    var ncost = $('#ncost').val();
    var nmrefil = $('#nmrefil').val();
    var nrecharge =  $('#nrecharge').val();
     $.ajax({
      url: '/unltd/sms_setup/',
      type: 'post',
       data: {
       'apiservice': napiservice,
       'apikey': napikey,
       'cost': ncost,
       'mrefil': nmrefil,
       'recharge': nrecharge,
      	'upid' :selectindex,
      	'act': 'update',
      	 'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]').val()
      },
      success: function(response){
        location.reload(true);
      }
 	});
});


$('#btndelgoogle').click(function(){
 	var selectindex = 'No'
 	selectindex = document.querySelector('input[name="selectedindex"]:checked').value;
     $.ajax({
      url: '/unltd/google_Setup/',
      type: 'post',
       data: {
      	'upid' :selectindex,
      	'act': 'del',
      	 'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]').val()
      },
      success: function(response){
       // document.getElementById("pypalbtnupdate").disabled = false;
        location.reload(true);
      }
 	});
});

$('#btnUpgoogle').click(function(){
  //  document.getElementById("pypalbtnupdate").disabled = false;
 	var selectindex = 'No'
 	selectindex = document.querySelector('input[name="selectedindex"]:checked').value;
    var mapapi = $('#nmapapi').val();
    var recaptchaapi = $('#nrecaptchaapi').val();
    var analyticCode = $('#nanalyticCode').val();
     $.ajax({
      url: '/unltd/google_Setup/',
      type: 'post',
       data: {
       'upid' :selectindex,
       'mapapi': mapapi,
       'recaptchaapi': recaptchaapi,
       'analyticCode': analyticCode,
      	'act': 'update',
      	 'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]').val()
      },
      success: function(response){
        location.reload(true);
      }
 	});
});




//function rchecked(){
//    var selectindex=document.querySelector('input[name="selectedindex"]:checked').value;
//    var email = $('#'+selectindex+'').html();
//    document.getElementById('mailpaypal').value = email;
//    document.getElementById('pypalbtnupdate').innerHTML = 'Update';
//
//}
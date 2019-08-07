function RadioButtonShuffler(value) {
    if(value == "email"){
        document.getElementById('emaildiv').style.display = 'block';
        document.getElementById('smsdiv').style.display = 'none';
    }else {
        document.getElementById('emaildiv').style.display = 'none';
        document.getElementById('smsdiv').style.display = 'block';
    }
}

function Clear() {
    document.getElementById('emailsubject').value = "";
    document.getElementById('emailbody').value = "";
    document.getElementById('smsbody').value = "";
}

function SendMessage(url) {
    var data = '';
    userid  = document.getElementById('userid').value;
    if (document.getElementById('email').checked) {
        type = 'email';
        email = document.getElementById('email').value;
        subject = document.getElementById('emailsubject').value;
        body =  CKEDITOR.instances['emailbody'].getData();
        data = {
            'userid' : userid,
            'MessageType': type,
            'emailid' : email,
            'subject' : subject,
            'body' : body,
            'contact' : "",
            'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]').val()
        }
    }else {
        if (document.getElementById('sms').checked) {
            type = 'sms';
            contact = document.getElementById('sms').value;
            body = document.getElementById('smsbody').value;
            data = {
                'userid' : userid,
                'MessageType': type,
                'emailid' : "",
                'subject' : "",
                'body' : body,
                'contact' : contact,
                'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]').val()
            }
        }
    }
    $.ajax({
        type : 'POST',
        url : url,
        dataType : 'json',
        async : true,
        data:data,
        success: function(json){
            alert (json.message);
        }
    });
}

$('#repassword').on('blur', function() {
    if(document.getElementById('password').value ==
        document.getElementById('repassword').value) {
        document.getElementById('message').innerHTML = "";
        document.getElementById('update').disabled = false;
    } else {
        document.getElementById('message').style.color = 'red';
        document.getElementById('message').innerHTML = "Passwrod Not Match";
        document.getElementById('update').disabled = true;
    }
});

function printData(id){
    var divToPrint=document.getElementById(id);
    newWin= window.open("");
    newWin.document.write(divToPrint.outerHTML);
    newWin.print();
    newWin.close();
}

function Search(url){
    try {
        var todate = document.getElementById('ToDate').value;
        var fromdate = document.getElementById('FromDate').value;
        var searchval = document.getElementById('search').value;
        var type = document.getElementById('head').innerText;
        if (todate != "" && fromdate != "" || searchval != "") {
            $.ajax({
                type: 'POST',
                url: url,
                dataType: 'json',
                async: true,
                data: {
                    'todate': todate,
                    'fromdate': fromdate,
                    'searchval': searchval,
                    'type': type,
                    'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]').val()
                },
                success: function (json) {
                     var tablebody = document.getElementById('tablebody');
                     tablebody.innerHTML = "";
                     json.Data.forEach(function (element) {
                        var tablecells = '<tr class="gradeX">\n';
                         tablecells += '<td>\n' +
                              '<input type="radio"  name="select"  value="'+ element[0]+'" class="label_radio r_off">\n' +
                          '</td>';
                         element.forEach(function (val) {
                              tablecells += '<td class="hidden-phone">' + val + '</td>';
                         });

                        tablecells += '</tr>';
                        tablebody.innerHTML += tablecells;
                     });
                }
            });
        } else {
            alert("Please Select the requirements");
        }
    }
    catch (e) {
       alter(e.toString());
    }
}

function Create_Table_Clear(){
    try {
        $('#basic-url1').val('');
        $('#basic-url2').val('');
        $('#basic-url3').val('');
    }
    catch (e) {
        alert(e);
    }
}
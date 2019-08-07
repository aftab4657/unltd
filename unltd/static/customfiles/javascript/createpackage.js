function package_creation () {

    try {
        var campaignTitle= CKEDITOR.instances['pd'].getData();
        $.ajax({
            type: 'POST',
            url: "ajax",
            dataType: 'json',
            async: true,
            data:
                {
                    PackageName: $('#pn').val(),
                    PackageDetail: campaignTitle,
                    PackageDuration: $('#pdu').val(),
                    charges: $('#ch').val(),
                    PackageType: $('#pt').val(),
                    'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]').val(),
                    msg:$

                },
            success: function (json) {
   $('#msg-success-alert').show();
                            setTimeout(
                                function()
                                {
                                    $('#msg-success-alert').hide();
                                }, 5000);

            }

        });

    }
    catch (e) {
 $('#msg-danger-alert').show();
                                setTimeout(
                                    function()
                                    {
                                        $('#msg-danger-alert').hide();
                                    }, 5000);    }
}




function package_Editing() {
    var campaignTitle= CKEDITOR.instances['pd'].getData();
    try {
        $.ajax({

            type: 'POST',
            url: 'editing',
            dataType: 'json',
            async: true,
            data:
                {
                    PackageName: $('#pn').val(),
                    PackageDetail: campaignTitle,
                    PackageDuration: $('#pdu').val(),
                    charges: $('#ch').val(),
                    hiddenid:$('#hiddenid').val(),
                    PackageType: $('#pt').val(),
                    'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]').val(),


                },
            success: function (json) {
   $('#msg-success-alert').show();
                            setTimeout(
                                function()
                                {
                                    $('#msg-success-alert').hide();
                                }, 5000);

            }

        });

    }
    catch (e) {
        console.log(e.message);
         $('#msg-danger-alert').show();
                                setTimeout(
                                    function()
                                    {
                                        $('#msg-danger-alert').hide();
                                    }, 5000);
    }

}




// //this is the <button class="btn btn-danger" onclick="send_msg()">Send</button> code for conversation
function send_msg() {

    var fileName = $("#file").val();
    var userimage=$("#userimage").attr('src');


    if(fileName) { // returns true if the string is not empty
        $('#send-btn').attr('type','submit');
    } else { // no file was selected


        let msg = CKEDITOR.instances['reply'].getData();
        let qid = $('#Qid').val();
        let colseticket=$('input[name="Cticket"]:checked').val();


        if (msg == "")
        {           $('#enter-msg').show();
            setTimeout(
                function()
                {
                    $('#enter-msg').hide();
                }, 5000);

            e.preventDefault();

        }
        else {


            try {
                $.ajax({

                    type: 'POST',
                    url: "/unltd/reply/",
                    dataType: 'json',
                    async: true,

                    data:
                        {
                            reply: msg,
                            Qid: qid,
                            Cticket:colseticket,
                            'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]').val(),


                        },
                    success: function (json) {
                        if (json.Data != 'close') {


                            let new_msg = '<div class="msg-time-chat">\n' +
                                '<a href="#" class="message-img"><img class="avatar" src="'+ userimage +'" alt=""></a>\n' +
                                '<div class="message-body msg-out">\n' +
                                '<span class="arrow"></span>\n' +
                                '<div class="text">\n' +
                                '<p class="attribution"> <a href="#">Admin</a> at July 16, 2019, 10:46 a.m.</p>\n' +
                                '<p>' + msg + '</p>\n' +
                                '</div>\n' +
                                '</div>\n' +
                                '</div>';
                            // alert(new_msg);
                            $('#msg-container').prepend(new_msg);
                            $('#msg-text').val('');
                            $('#lastid').val(json.Data);
                            $('#msg-success-alert').show();
                            setTimeout(
                                function()
                                {
                                    $('#msg-success-alert').hide();
                                }, 5000);
                            // alert(msg);
                        }
                        else {
                            try {
                                window.location.href= "/unltd/viewtutorial/";

                            }
                            catch (e) {
                                console.log(e);
                                $('#msg-danger-alert').show();
                                setTimeout(
                                    function()
                                    {
                                        $('#msg-danger-alert').hide();
                                    }, 5000);

                            }

                        }
                    }
                });
            }
            catch (e) {
                console.log(e.message);
            }

        }
    }
}

// function openimage() {
//     alert("open image");
//
// }


function unreadmsg()
{
    try {
        $.ajax({

            type: 'POST',
            url: DJANGO_STATIC_URLTOOPEN,
            dataType: 'json',
            async: true,
            data:
                {

                    'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]').val(),


                },
            success: function (json) {

                if (json.Count){

                    $('.msg-count').html(json.Count);
                }
                if (json.Replies)
                {
                     for (var i=0; i <json.Replies.length; i++) {
                         // alert('#reply' + json.Replies[i][3]);
                         if ($('#reply' + json.Replies[i][3]).length){}
                         else{
                             let notification = '                            <li id="reply' + json.Replies[i][3] + '">\n' +
                                 '                                <a href="#">\n' +
                                 '                                    <span class="photo"><img alt="avatar" src="{% static \'img/avatar-mini.jpg\' %}"></span>\n' +
                                 '                                    <span class="subject">\n' +
                                 '                                    <span class="from">' + json.Replies[i][1] + '</span>\n' +
                                 '                                    <span class="time">' + json.Replies[i][2] + '</span>\n' +
                                 '                                    </span>\n' +
                                 '                                    <span class="message">\n' + json.Replies[i][0] + ' </span>\n' +
                                 '                                </a>\n' +
                                 '                            </li>\n';
                             $('#after').after(notification);
                         }
                     }
                     let last_li ='<li id="see-all">\n' +
                             '<a href="#">See all messages</a>\n' +
                             '</li>';
                     if ($("#see-all").length) {}
                     else
                     $('#msg-notification').append(last_li);


                }
                if(json.Questions)
                {
                    for (var i=0; i <json.Questions.length; i++) {
                         //alert(json.Questions[i][0]);
                                             for (var i=0; i <json.Replies.length; i++) {
                         if (!($('#ques' + json.Replies[i][3]).find())) {
                             let notification = '                            <li id="ques' + json.Replies[i][3] + '">\n' +
                                 '                                <a href="#">\n' +
                                 '                                    <span class="photo"><img alt="avatar" src="{% static \'img/avatar-mini.jpg\' %}"></span>\n' +
                                 '                                    <span class="subject">\n' +
                                 '                                    <span class="from">' + json.Replies[i][1] + '</span>\n' +
                                 '                                    <span class="time">' + json.Replies[i][2] + '</span>\n' +
                                 '                                    </span>\n' +
                                 '                                    <span class="message">\n' + json.Replies[i][0] + ' </span>\n' +
                                 '                                </a>\n' +
                                 '                            </li>\n';
                             $('#msg-notification').prepend(notification);
                         }
                     }


                     }

                }

            }

        });

    }
    catch (e) {
        console.log(e.message);
    }
}
setInterval(unreadmsg,4000); //after 4 seconds





//SMS PACKAGE CREATION
function SMSpackage_creation () {

    try {
        var campaignTitle= CKEDITOR.instances['pd'].getData();

        $.ajax({
            type: 'POST',
            url: "smspackageCreationajax",
            dataType: 'json',
            async: true,
            data:
                {

                    PackageName: $('#pn').val(),
                    PackageDetail: campaignTitle,
                    PackageDuration: $('#pdu').val(),
                    total: $('#total').val(),
                    charges: $('#ch').val(),
                    PackageType: $('#pt').val(),
                    'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]').val(),
                    msg:$

                },
            success: function (json) {
              $('#msg-success-alert').show();
                            setTimeout(
                                function()
                                {
                                    $('#msg-success-alert').hide();
                                }, 5000);

            }

        });

    }
    catch (e) {
        console.log(e.message);
        $('#msg-danger-alert').show();
                                setTimeout(
                                    function()
                                    {
                                        $('#msg-danger-alert').hide();
                                    }, 5000);
    }
}

function package_SMSEditing() {
    var campaignTitle= CKEDITOR.instances['pd'].getData();
    try {
        $.ajax({

            type: 'POST',
            url: 'smsediting',
            dataType: 'json',
            async: true,
            data:
                {
                    PackageName: $('#pn').val(),
                    PackageDetail: campaignTitle,
                    PackageDuration: $('#pdu').val(),
                    total: $('#total').val(),
                    charges: $('#ch').val(),
                    hiddenid:$('#hiddenid').val(),
                    PackageType: $('#pt').val(),
                    'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]').val(),


                },
            success: function (json) {
               $('#msg-success-alert').show();
                            setTimeout(
                                function()
                                {
                                    $('#msg-success-alert').hide();
                                }, 5000);

            }

        });

    }
    catch (e) {
        console.log(e.message);
        $('#msg-danger-alert').show();
                                setTimeout(
                                    function()
                                    {
                                        $('#msg-danger-alert').hide();
                                    }, 5000);
    }

}

//Categories CREATION
function Categories_Creation () {

    try {
        $.ajax({
            type: 'POST',
            url: "CategoryCreation",
            dataType: 'json',
            async: true,
            data:
                {

                    CategoryName: $('#cn').val(),
                    CategoryDuration: $('#cdu').val(),
                    'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]').val(),

                },
            success: function (json) {
              $('#msg-success-alert').show();
                            setTimeout(
                                function()
                                {
                                    $('#msg-success-alert').hide();
                                }, 5000);

            }

        });

    }
    catch (e) {
        console.log(e.message);
        $('#msg-danger-alert').show();
                                setTimeout(
                                    function()
                                    {
                                        $('#msg-danger-alert').hide();
                                    }, 5000);
    }
}


function SubCategories_Creation() {
    try {
        $.ajax({
            type: 'POST',
            url: "SubCategoryCreation",
            dataType: 'json',
            async: true,
            data:
                {

                    SubCategoryName: $('#sn').val(),
                    SubCategoryDuration: $('#sdu').val(),
                    CategoryName: $('#co').val(),
                    'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]').val(),

                },
            success: function (json) {
            //sweet msgs
                $('#msg-success-alert').show();
                            setTimeout(
                                function()
                                {
                                    $('#msg-success-alert').hide();
                                }, 5000);

            }

        });

    }
    catch (e) {
        console.log(e.message);
         $('#msg-danger-alert').show();
                                setTimeout(
                                    function()
                                    {
                                        $('#msg-danger-alert').hide();
                                    }, 5000);
    }
}


function CategoryEditingFunction() {
    try {
        $.ajax({

            type: 'POST',
            url: 'editingcategory',
            dataType: 'json',
            async: true,
            data:
                {

                    CategoryName: $('#cn').val(),
                    CategoryDuration: $('#cdu').val(),
                    hiddenid:$('#hiddenid').val(),
                    'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]').val(),


                },
            success: function (json) {
               // $('#msg-success-alert').show();
               //              setTimeout(
               //                  function()
               //                  {
               //                      $('#msg-success-alert').hide();
               //                  }, 5000);
                              try {
                                window.location.href= "/unltd/viewcategories/";

                            }
                            catch (e) {
                                console.log(e);
                                $('#msg-danger-alert').show();
                                setTimeout(
                                    function()
                                    {
                                        $('#msg-danger-alert').hide();
                                    }, 5000);

                            }
            }

        });

    }
    catch (e) {
        console.log(e.message);
        $('#msg-danger-alert').show();
                                setTimeout(
                                    function()
                                    {
                                        $('#msg-danger-alert').hide();
                                    }, 5000);
    }

}




function SubCategoryEditingFunction() {
    try {
        $.ajax({

            type: 'POST',
            url: 'editingcategorysub',
            dataType: 'json',
            async: true,
            data:
                {

                    SubCategoryName: $('#sn').val(),
                    SubCategoryDuration: $('#sdu').val(),
                    CategoryName: $('#co').val(),
                    hiddenid:$('#hiddenid').val(),
                    'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]').val(),


                },
            success: function (json) {
               // $('#msg-success-alert').show();
               //              setTimeout(
               //                  function()
               //                  {
               //                      $('#msg-success-alert').hide();
               //                  }, 5000);
                            try {
                                window.location.href= "/unltd/viewsubcategories/";

                            }
                            catch (e) {
                                console.log(e);
                                $('#msg-danger-alert').show();
                                setTimeout(
                                    function()
                                    {
                                        $('#msg-danger-alert').hide();
                                    }, 5000);

                            }

            }

        });

    }
    catch (e) {
        console.log(e.message);
        $('#msg-danger-alert').show();
                                setTimeout(
                                    function()
                                    {
                                        $('#msg-danger-alert').hide();
                                    }, 5000);
    }

}



function ItemEditingFunction() {
    var fileName = $("#file").val();


    $('#file-upload-form').attr('action','editingitems');
    $('#send-btn').attr('type', 'submit');


}





function Add_Items() {
    var fileName = $("#file").val();

    if (fileName) { // returns true if the string is not empty
        $('#send-btn').attr('type', 'submit');
    }
    else { // no file was selected
        $('#msg-danger-alert').show();
            setTimeout(
                function () {
                    $('#msg-danger-alert').hide();
                }, 5000);


        }

}



//Offer CREATION
function Add_Offers () {
     var url = $("#url").val();
    try {
        $.ajax({
            type: 'POST',
            url: url,
            dataType: 'json',
            async: true,
            data:
                {

                    Offer: $('#oname').val(),
                    StartDate: $('#sdate').val(),
                    EndDate: $('#exdate').val(),
                    Charges: $('#ch').val(),
                    hiddenid:$('#hiddenid').val(),

                    'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]').val(),

                },
            success: function (json) {
              $('#msg-success-alert').show();
                            setTimeout(
                                function()
                                {
                                    $('#msg-success-alert').hide();
                                }, 5000);

            }

        });

    }
    catch (e) {
        console.log(e.message);
        $('#msg-danger-alert').show();
                                setTimeout(
                                    function()
                                    {
                                        $('#msg-danger-alert').hide();
                                    }, 5000);
    }
}




//View Offer
function view_offers() {

     var url = $("#url2").val();
     alert(url);
    try {
        $.ajax({
            type: 'POST',
            url: url,
            dataType: 'json',
            async: true,
            data:
                {


                    itemid:$('#select').val(),

                    'csrfmiddlewaretoken': $('[name="csrfmiddlewaretoken"]').val(),

                },
            success: function (json) {
              $('#msg-success-alert').show();
                            setTimeout(
                                function()
                                {
                                    $('#msg-success-alert').hide();
                                }, 5000);

            }

        });

    }
    catch (e) {
        console.log(e.message);
        $('#msg-danger-alert').show();
                                setTimeout(
                                    function()
                                    {
                                        $('#msg-danger-alert').hide();
                                    }, 5000);
    }
}



function EditOffer() {

    alert("ammar");
    $('#file-upload-form').attr('action','editingoffers');
    $('#send-btn').attr('type', 'submit');
}

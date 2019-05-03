//alert('Script Working');
function validateForm(){
    //Registration Id Validation
    var reg_no = document.forms['my_form']['reg_no'].value;
    if(reg_no.length==10 || reg_no.length<=11){
        //console.log('Perfect');
    }
    else{
        alert('Please Enter Proper Register Id!')
        document.getElementById("reg_no").value = "";
        return false;
    }

    function ddlValidate(dd_id) {

        var ddl = document.getElementById(dd_id);
        if (dd_id.value == 0) {
            //If the "Please Select" option is selected display error.
                alert("Please select an option!");
                document.getElementById(dd_id).options[dd_id.selectedIndex].value = "";
        }
        else {
            var optionSelectedText = dd_id.options[dd_id.selectedIndex].text;
            //alert(optionSelectedText+" Selected Success !!!"); ;
        }
    }

    //Section Validation
    var e = document.getElementById("section");
    ddlValidate(e);

    //Mobile Number Validation
    function mob_validate(mob_no,cid) {
        //console.log(cid,typeof cid)
        var res = mob_no.split('');
        if(mob_no.length!=10){
            alert('Mobile Number must be 10 digits!');
            document.getElementById(cid).value = "";
        }
        if(mob_no.length==10){
            switch (parseInt(res[0])) {
                case 6: //alert('Valid Mobile Number!');
                        break;
                case 7: //alert('Valid Mobile Number!');
                        break;
                case 8: alert('Valid Mobile Number!');
                        break;
                case 9: //alert('Valid Mobile Number!');
                        break;
                default:alert('Mobile Number is Invalid !');
                        document.getElementById("mob_no").value = "";

            }
        }
    }
    var mob_no = document.forms['my_form']['mob_no'].value;
    mob_validate(mob_no,'mob_no');
    //console.log(res[0])


    //10th marks validation
    var ssc_type = document.forms['my_form']['ssc_type'].value;
    let ssc_marks = document.forms['my_form']['ssc_marks'].value;
    switch (ssc_type) {
        case 'cgpa':
                    if(ssc_marks<=10){
                         //console.log('Valid CGPA !');
                    }
                    else{
                        alert('Please Enter Proper CGPA!');
                        document.getElementById("ssc_marks").value = "";
                    }
                    break;
        case 'marks':
                    if(ssc_marks<=600){
                        //console.log('Valid Marks !');
                    }
                    else{
                        alert('Please Enter Proper Marks!');
                        document.getElementById("ssc_marks").value = "";
                    }
                    break;
        default:alert('Please Select SSC TYPE !');

    }
    //SSC Percentage Validation
    let ssc_per = document.forms['my_form']['ssc_per'].value;
    if(ssc_per<=100){
        //alert('Valid Percentage !');
    }
    else{
        alert('Invalid Percentage');
        document.getElementById("ssc_per").value = "";
    }

    //Parents Mobile Validation
    var p_mob_no = document.forms['my_form']['p_mob_no'].value;
    mob_validate(p_mob_no,'p_mob_no');

    //Guardian Mobile Number
    let g_mob_no = document.forms['my_form']['g_mob_no'].value;
    mob_validate(p_mob_no,'g_mob_no');
}



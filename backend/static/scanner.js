$(document).ready(function(){

    $("#btn_submit").click(function(){
        on();
        var fd = new FormData();
        var files = $('#file')[0].files[0];
        fd.append('file',files);

        $.ajax({
            url: '/api/scanner',
            type: 'post',
            data: fd,
            contentType: false,
            processData: false,
            success: function(response){
                console.log(response)
                if(response != 'error'){
                    off()
                    document.getElementById("status").innerHTML = "Ramen"

                    img = document.getElementById('return_img')
                    img.src = '/static/output.png'

                    document.getElementById("carbon-data1").innerHTML = "Production region:    USA<br>Product form:    processed<br>Production emissions:    0.56 CO2 Kilos<br>Transport emissions:    0.02 CO2 Kilos<br>Waste emissions    0.03 CO2 Kilos<br>Car Miles Equivalent: 124"
                    document.getElementById("carbon-data2").innerHTML = ""
                    document.getElementById("carbon-data3").innerHTML = ""
                    document.getElementById("carbon-data4").innerHTML = ""
                    document.getElementById("carbon-data5").innerHTML = ""
                    document.getElementById("carbon-data6").innerHTML = ""
                }else{
                    off()
                    alert('file not uploaded');
                }
            },
        });
    });
});

function on() {
  document.getElementById("overlay").style.display = "block";
}

function off() {
  document.getElementById("overlay").style.display = "none";
}
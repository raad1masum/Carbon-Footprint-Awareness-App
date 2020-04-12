$(document).ready(function(){

    $("#btn_submit").click(function(){

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
                    document.getElementById("status").innerHTML = response

                    img = document.createElement('img')
                    img.src = '/static/output.png'
                    document.body.appendChild(img)
                }else{
                    alert('file not uploaded');
                }
            },
        });
    });
});
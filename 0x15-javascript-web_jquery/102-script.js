document.addEventListener("DOMContentLoaded", function () {
    $("#btn_translate").click(function (){
        let lng = $("#language_code").val();
        let url = "https://fourtonfish.com/hellosalut/?lang="+lng;
        $.getJSON(url, function (data) {
            $("#hello").text(data.hello);
        });
    });
});
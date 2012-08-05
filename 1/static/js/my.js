(function() {
    $(document).ready(function() {

        $('#apiList').delegate("li", "click", function(event) {
            event.stopPropagation();
            item = $(this);
            if(item.hasClass("nav-header")) {
                return;
            }
            item.siblings(".active").removeClass("active");
            item.addClass("active");
            $('#apiTitle').text(item.text());
        });

        $('#excute').click(function() {
            var url = "/api?method=" + $('#apiTitle').text();
            $.ajax({
                url: url,
                type: "GET",
                dataType: "json",
                success: fetchCallback
            });
        });

        fetchCallback = function(obj, textStatus, xhr) {
            xhr = null;
            if (obj.status && obj.status == 'success') {
                var j = JSON.stringify(obj, null, 4);
                $('.prettyprint').html(j);
                prettyPrint();
            }
        };
    });
})();


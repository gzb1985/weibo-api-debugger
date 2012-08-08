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
            $('#apiUrl').text('https://api.weibo.com/2/' + item.text() +'.json');
        });

        $('#apiList li:first').trigger('click');

        $('#excute').click(function(event) {
            event.stopPropagation();
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
            var j;
            if (obj.status && obj.status === 'success') {
                j = JSON.stringify(obj.rst, null, 4);
            } else {
                j = JSON.stringify(obj, null, 4);
            }
            $('.prettyprint').html(j);
            prettyPrint();
        };
    });
})();


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
            var json;
            if (obj.status && obj.status === 'success') {
                json = obj.rst;
            } else {
                json = obj;
            }
            $('#formatedJson').html(JSON.stringify(json, null, 4));
            prettyPrint();

            var element = JSONFormatter.prototype.jsonToHTML(json);
            $('#collapsedJson').empty()
            $('#collapsedJson').append(element);
            $(element).ready(function() {
              var items = document.getElementsByClassName('collapsible');
              for( var i = 0; i < items.length; i++) {
                addCollapser(items[i].parentNode);
              }
            });

            $('#rawJson').text(JSON.stringify(json, null, 0));
        };

        $('#myTab a').click(function (e) {
            e.preventDefault();
            $(this).tab('show');
        });
    });
})();


(function() {

    function ApiDbg() {
        this.markup = '<li><a>${name}</a></li>';
        this.apiTemplName = 'ApiTemplate';
        this.apis = [];
    }

    ApiDbg.prototype.init = function() {
        $('#myTab a').click(function (e) {
            e.preventDefault();
            $(this).tab('show');
        });
    };

    ApiDbg.prototype.fetchApiList = function() {
        $.ajax({
            url: '/api/list',
            type: "GET",
            dataType: "json",
            context: this,
            success: this.fetchApiListCallback
        });
    };

    ApiDbg.prototype.fetchApiListCallback = function(obj, textStatus, xhr) {
        xhr = null;
        if (obj.status && obj.status === 'success') {
            $.template(this.apiTemplName, this.markup);
            $.tmpl(this.apiTemplName, obj.rst).appendTo("#apiList");
            this.apis = obj.rst;

            this.handleApiList();
            this.handleApiExcution();
        }
    };

    ApiDbg.prototype.handleApiList = function(obj, textStatus, xhr) {
        (function(apis) {
            $('#apiList').delegate("li", "click", function(event) {
                event.stopPropagation();
                item = $(this);
                if(item.hasClass("nav-header")) {
                    return;
                }
                item.siblings(".active").removeClass("active");
                item.addClass("active");
                $('#apiTitle').text(item.text());
                var apiUrlManual = 'https://api.weibo.com/2/' + item.text() +'.json';
                for (var i = 0; i < apis.length; i++) {
                    if (apis[i]['name'] == item.text()) {
                        len = apis[i]['param'].length;
                        if (len > 0) apiUrlManual += '?';
                        for (var j = 0; j < len; j++) {
                            if (j > 0) apiUrlManual += '&';
                            apiUrlManual += apis[i]['param'][j] + '=';
                        }
                    }
                };
                $('#apiUrlManual').val(apiUrlManual);
            });
        })(this.apis);

        $('#apiList li:first').trigger('click');
    };

    ApiDbg.prototype.handleApiExcution = function(obj, textStatus, xhr) {
        var context = this;
        $('#excuteManual').click(function(event) {
            event.stopPropagation();
            var url = "/apiManual?method=" + $('#apiTitle').text();
            var param = context.parseParams($('#apiUrlManual').val());
            $('#apiRequest').text($('#apiUrlManual').val());
            $.ajax({
                url: url,
                type: "GET",
                dataType: "json",
                data: param,
                context: context,
                success: context.fetchApiExcResult
            });
        });
    };

    ApiDbg.prototype.parseParams = function(url) {
        var urlParams = {};
        (function () {
            var match,
                pl     = /\+/g,  // Regex for replacing addition symbol with a space
                search = /([^&=]+)=?([^&]*)/g,
                decode = function (s) { return decodeURIComponent(s.replace(pl, " ")); },
                ind = url.indexOf('?'),
                query  = ind != -1 ? url.substring(ind + 1) : '';

            while (match = search.exec(query))
               urlParams[decode(match[1])] = decode(match[2]);
        })();
        console.log(urlParams);
        return urlParams;
    };

    ApiDbg.prototype.fetchApiExcResult = function(obj, textStatus, xhr) {
        xhr = null;
        var json;
        if (obj.status && obj.status === 'success') {
            json = obj.rst;
        } else {
            json = obj;
        }
        this.displayJson(json);
    };

    ApiDbg.prototype.displayJson = function(json) {
        this.displayFormatedJson(json);
        this.displayCollapsedJson(json);
        this.displayRawJson(json);
    };

    ApiDbg.prototype.displayFormatedJson = function(json) {
        $('#formatedJson').html(JSON.stringify(json, null, 4));
        prettyPrint();
    };

    ApiDbg.prototype.displayCollapsedJson = function(json) {
        var element = JSONFormatter.prototype.jsonToHTML(json);
        $('#collapsedJson').empty()
        $('#collapsedJson').append(element);
        $(element).ready(function() {
          var items = document.getElementsByClassName('collapsible');
          for( var i = 0; i < items.length; i++) {
            addCollapser(items[i].parentNode);
          }
        });
    };

    ApiDbg.prototype.displayRawJson = function(json) {
        $('#rawJson').text(JSON.stringify(json));
    };

    $(document).ready(function() {
        var dbg = new ApiDbg();
        dbg.init();
        dbg.fetchApiList();
    });
})();


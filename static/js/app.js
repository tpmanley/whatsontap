var app = angular.module("app", [])

app.controller("AppCtrl", function($http) {
    var app = this;

    $http.get('/api/tap').success(function(data) {
        app.taps = data.objects;
    });

    app.addTap = function() {
        $http.post('/api/tap', {"name":"new",
                                "style":"N/A",
                                "image":"http://www.placekitten.com/100/100/?image=" + app.taps.length})
            .success(function(data) {
                app.taps.push(data);
            })
    };
});

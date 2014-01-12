var app = angular.module("app", [])

app.controller("AppCtrl", function($http) {
    var app = this;

    $http.get('/api/tap').success(function(data) {
        app.taps = data.objects;
    });

    app.addTap = function() {
        $http.post('/api/tap', {"name":"new", "style":"N/A"})
            .success(function(data) {
                app.taps.push(data);
            })
    };
});

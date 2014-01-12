var app = angular.module("app", [])

app.controller("AppCtrl", function($http) {
    var app = this;

    $http.get('/api/tap').success(function(data) {
        app.taps = data.objects;
    })
});

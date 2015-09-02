'use strict';

var app = angular.module('app', ['ngRoute', 'angularFileUpload']);

app.config(['$routeProvider', function($routeProvider) {
    $routeProvider
        .when('/', {
            templateUrl: 'partials/classifier.html',
            controller: 'IrisController'
        })
        .when('/color', {
            templateUrl: 'partials/color.html',
            controller: 'ColorController'
        })
}]);

'use strict';

app.controller('IrisController', ['$scope', '$http', 'FileUploader', 'CsvParser',
    function($scope, $http, FileUploader, CsvParser) {
        $scope.payload = {};
        $scope.classification = {};

        $scope.uploader = new FileUploader({
            url: 'http://localhost:5000/upload'
        });

        $scope.uploader.onAfterAddingFile = function(fileItem) {
            CsvParser(fileItem).then(function(res) {
                $scope.payload.data = res['data'];
                $scope.availableFields = res['fields'];
            });
        };

        $scope.send = function() {
            $scope.payload.features = parse($scope.featuresObj);
            $http.post('http://localhost:5000/classify', $scope.payload)
                .then(function(response) {
                    $scope.classification.results = response['data']['results'];
                    $scope.classification.labels = Object.keys(response['data']['results']);
                    $scope.classification.accuracy = response['data']['accuracy'];
                }, function(err) {
                    console.log(err);
                });
        };
    }]);


app.controller('ColorController', ['$scope', '$http', 'FileUploader',
    function($scope, $http, FileUploader) {
        $scope.uploader = new FileUploader({
            url: 'http://localhost:5000/color',
            autoUpload: true
        });

        $scope.uploader.onAfterAddingFile = function(fileItem) {
            if ($scope.uploader.queue.length > 1) {
                $scope.uploader.queue.splice(0, 1);
                $scope.colors = [];
            }
        };

        $scope.uploader.onSuccessItem = function(fileItem, response, status, headers) {
            $scope.colors = response['colors'];
        };
}]);

var parse = function(obj) {
    var clean = [];
    for (var key in obj) {
        if (obj[key]) {
            clean.push(key);
        }
    }
    return clean;
};

app.factory('CsvParser', function($q,$rootScope) {
    function parse(fileItem, callback) {
        Papa.parse(fileItem['_file'], {
            header: true,
            skipEmptyLines: true,
            worker: false,
            complete: function(results) {
                callback(results);
            }
        });
    }

    function format(results) {
        return {"data": results["data"],
                "fields": results["meta"]["fields"]};
    }

    return function(fileItem) {
        var deferred = $q.defer();
        parse(fileItem, function(results) {
            var final = format(results);
            $rootScope.$apply(function() {
                deferred.resolve(final);
            });
        });
        return deferred.promise;
    };
});

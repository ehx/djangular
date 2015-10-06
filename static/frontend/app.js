//para hacer uso de $resource debemos colocarlo al crear el modulo
var app = angular.module('app', ["ngResource", 'ngCookies']);

app.config(function ($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
});

app.run(['$http', '$cookies', function($http, $cookies) {
  $http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken'];
}]);

//de esta forma tan sencilla consumimos con $resource en AngularJS
app.factory('taskResource', function ($resource) {
    return $resource('/task/:id', {})
});

app.controller('appController', function ($scope, $http, taskResource) {

    function getTasks() {
        $scope.tasks = taskResource.query({done:0});
        $scope.ctasks = taskResource.query({done:1});
    }
    
    getTasks();

    $scope.updateTask = function(taskId) {
        upTask = new taskResource()
        task = upTask.$get({id:taskId});
        task.done = 1
        task.$save();
    };

    $scope.deleteTask = function(taskId) {
        taskResource.delete({ id: taskId });
        getTasks();
    };
})

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
  return $resource('/task/:taskId', {taskId:'@id'},
    {
      'get':    {method:'GET'},
      'save':   {method:'POST'},
      'update': {method:'PUT'},
      'query':  {method:'GET', isArray:true},
      'remove': {method:'DELETE'},
      'delete': {method:'DELETE'} 
    });
});

app.controller('appController', function ($scope, $http, taskResource) {
  function getTasks() {
    $scope.tasks = taskResource.query({done: false});
    $scope.ctasks = taskResource.query({done: true});
  }
  
  getTasks();

  $scope.doneTask = function(taskId) {
    taskResource.get({ taskId:taskId }, function(task) {
      task.done = true;
      taskResource.update({ taskId:task.id }, task);
    });
    getTasks();
  };

  $scope.deleteTask = function(taskId) {
    taskResource.delete({ taskId : taskId });
    getTasks();
  };
})
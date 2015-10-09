//para hacer uso de $resource debemos colocarlo al crear el modulo
var app = angular.module('app', ["ngResource", 'ngCookies', 'ui.bootstrap']);

app.config(function ($httpProvider, $resourceProvider) {
  $httpProvider.defaults.xsrfCookieName = 'csrftoken';
  $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
  $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
  $resourceProvider.defaults.stripTrailingSlashes = false;
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

app.factory('clientResource', function ($resource) {
  return $resource('/client/:clientId', {clientId:'@id'},
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

app.controller('modalController', function ($scope, taskResource, clientResource) {

  clientResource.query({}, function(data){
    $scope.clients = data;
  });

  $scope.saveEntry = function() {
    $scope.task.start_date = "2015-12-12";
    $scope.task.userId = 1;
    taskResource.save($scope.task);
  };

})
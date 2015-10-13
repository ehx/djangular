//para hacer uso de $resource debemos colocarlo al crear el modulo
var app = angular.module('app', ["ngResource", 'ngCookies', 'ngRoute']);

app.config(function ($httpProvider, $resourceProvider) {
  $httpProvider.defaults.xsrfCookieName = 'csrftoken';
  $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
  $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
  $resourceProvider.defaults.stripTrailingSlashes = false;
});

app.run(['$http', '$cookies', function($http, $cookies) {
  $http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken'];
}]);


// rutas
app.config(function($routeProvider) {
  $routeProvider
    // home
    .when('/', {
      templateUrl : 'task.html',
      controller  : 'taskController'
    })

    // history
    .when('/task/:taskId', {
      templateUrl : 'detailTask.html',
      controller  : 'commentsController'
    })

    .otherwise({
      redirectTo: '/'
    });
});


app.directive('jqdatepicker', function () {
    return {
        restrict: 'A',
        require: 'ngModel',
         link: function (scope, element, attrs, ngModelCtrl) {
            element.datepicker({
                dateFormat: 'yy-mm-dd',
                onSelect: function (date) {
                    scope.date = date;
                    scope.$apply();
                }
            });
        }
    };
});

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

app.factory('taskCommentsResource', function ($resource) {
  return $resource('/taskComments/?task', {task:'@id'},
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

app.controller('taskController', function ($scope, taskResource) {

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
    $scope.task.userId = 1;
    taskResource.save($scope.task);
  };

})

app.controller('commentsController', function ($scope, taskCommentsResource, $routeParams, taskResource) {

  var taskId = $routeParams.taskId

  taskResource.query({ id : taskId }, function(task){
    $scope.task = task[0];    
  });
  
  taskCommentsResource.query({ task : taskId }, function(data){
    $scope.allComments = data;    
  });
})

app.controller('mainController', function ($scope, taskCommentsResource) {

  //taskCommentsResource.query({task: 2}, function(data){
  //  $scope.allComments = data;
  //});
})
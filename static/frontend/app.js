//para hacer uso de $resource debemos colocarlo al crear el modulo
var app = angular.module('app', ["ngResource", 'ngCookies', 'ngRoute', 'ui.bootstrap']);

app.config(function ($httpProvider, $resourceProvider) {
  $httpProvider.defaults.xsrfCookieName = 'csrftoken';
  $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
  $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
  $resourceProvider.defaults.stripTrailingSlashes = false;
});

app.run(['$http', '$cookies', function($http, $cookies) {
  $http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken'];
}]);

app.filter('moment', function() {
    return function(dateString, format) {
        return moment(dateString).format(format);
	};
});

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
  return $resource('/task/:id', {id:'@id'},
    {
      'get':    {method:'GET'},
      'save':   {method:'POST'},
      'update': {method:'PUT'},
      'query':  {method:'GET', isArray:true},
      'remove': {method:'DELETE'},
      'delete': {method:'DELETE'} 
    });
});

app.factory('notificationResource', function ($resource) {
  return $resource('/notification/:id', {id:'@id'},
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
  return $resource('/taskComment/:id', {id:'@id'},
    {
      'get':    {method:'GET'},
      'save':   {method:'POST'},
      'update': {method:'PUT'},
      'query':  {method:'GET', isArray:true},
      'remove': {method:'DELETE'},
      'delete': {method:'DELETE'} 
    });
});

app.factory('taskCommentsResource2', function ($resource) {
  return $resource('/taskComment2/:id', {id:'@id'},
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
  return $resource('/client/:id', {id:'@id'},
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

app.controller('commentsController', function ($scope, taskCommentsResource, $routeParams, taskResource, 
  notificationResource, taskCommentsResource2, $timeout, $log) {
  
$scope.totalItems = 64;
$scope.currentPage = 4;

$scope.setPage = function (pageNo) {
$scope.currentPage = pageNo;
};

$scope.pageChanged = function() {
$log.log('Page changed to: ' + $scope.currentPage);
};

$scope.maxSize = 5;
$scope.bigTotalItems = 175;
$scope.bigCurrentPage = 1;

  var taskId = parseInt($routeParams.taskId, 10);

  function getComments() {
    $scope.tasks = taskResource.query({done: false});
    $scope.ctasks = taskResource.query({done: true});
  }


  function getComments(){
    taskCommentsResource.query({ task : taskId }, function(data){
      $scope.allComments = data;    
    })
  };

  getComments();

  taskResource.query({ task : taskId }, function(task){
    $scope.task = task[0];    
  });
  
  $scope.newComment = function () {
    var cm = new taskCommentsResource2;
    cm.task = taskId;
    cm.user = 1;
    cm.comment = $scope.cm.comment;
    taskCommentsResource.save(cm);

    //create notification to user
    var nt = new notificationResource;
    nt.user = 1;
    nt.ntype = "comment";
    nt.notificationId = taskId;
    notificationResource.save(nt);
    $timeout(getComments, 500);
    
  }

})

app.controller('mainController', function ($scope, notificationResource) {

  notificationResource.get({}, function(data){
    $scope.countNotification = data.count;
  });

  //taskCommentsResource.query({task: 2}, function(data){
  //  $scope.allComments = data;
  //});
})
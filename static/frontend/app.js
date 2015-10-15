//para hacer uso de $resource debemos colocarlo al crear el modulo
var app = angular.module('app', ["ngResource", 'ngCookies', 'ngRoute', 'ui.bootstrap', 'ui.select', 'ngSanitize']);

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

app.config(function(uiSelectConfig) {
  uiSelectConfig.theme = 'bootstrap';
  uiSelectConfig.resetSearchInput = true;
  uiSelectConfig.appendToBody = true;
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

    .when('/todo', {
      templateUrl : 'todo.html',
      controller  : 'todoController'
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

app.factory('todoResource', function ($resource) {
  return $resource('/todo/:id', {id:'@id'},
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

  // carga select con clientes
  clientResource.query({}, function(data){
    $scope.clients = data;
  });

  // crea trea
  $scope.newTask = function() {
    $scope.task.userId = 1;
    taskResource.save($scope.task);
  };

})

app.controller('commentsController', function ($scope, taskCommentsResource, $routeParams, taskResource, 
  notificationResource, taskCommentsResource2, $timeout) {

  // numero de pagina inicial para paginador
  $scope.currentPage = 1;

  // obtiene el id de la tarea desde la url y la convierte a int
  var taskId = parseInt($routeParams.taskId, 10);

  // obtiene comentarios de la tarea seleccionada
  function getComments(){
    taskCommentsResource.get({ task : taskId }, function(data){
      $scope.allComments = data.results;    
      $scope.totalItems = data.count;
    })
  };

  getComments();

  // cuando cambia la pagina , setea numero de pagina en la consulta y actualiza los resultados
  $scope.pageChanged = function() {
    taskCommentsResource.get({ task : taskId , page : $scope.currentPage}, function(data){
      $scope.allComments = data.results;    
    })
  };

  taskResource.query({ task : taskId }, function(task){
    $scope.task = task[0];    
  });
  
  // crea nuevo comentario
  $scope.newComment = function () {
    var cm = new taskCommentsResource2;
    cm.task = taskId;
    cm.user = 1;
    cm.comment = $scope.cm.comment;
    taskCommentsResource.save(cm);

    // notifica al usuario
    var nt = new notificationResource;
    nt.user = 1;
    nt.ntype = "comment";
    nt.notificationId = taskId;
    notificationResource.save(nt);
    $timeout(getComments, 500);
  }
})

app.controller('mainController', function ($scope, notificationResource) {

  var allNotifications = notificationResource.get({user: 1}, function(data){
    $scope.countNotification = data.count;
    $scope.notifications = data.results;
  });

  $scope.allRead = function () {
    var cm = new taskCommentsResource2;
    cm.task = taskId;
    cm.user = 1;
    cm.comment = $scope.cm.comment;
    taskCommentsResource.save(cm);

    // notifica al usuario
    var nt = new notificationResource;
    nt.user = 1;
    nt.ntype = "comment";
    nt.notificationId = taskId;
    notificationResource.save(nt);
    $timeout(getComments, 500);
  }
})

app.controller('mainController', function ($scope, notificationResource) {

  var allNotifications = notificationResource.get({user: 1}, function(data){
    $scope.countNotification = data.count;
    $scope.notifications = data.results;
  });

  $scope.allRead = function () {
    var cm = new taskCommentsResource2;
    cm.task = taskId;
    cm.user = 1;
    cm.comment = $scope.cm.comment;
    taskCommentsResource.save(cm);

    // notifica al usuario
    var nt = new notificationResource;
    nt.user = 1;
    nt.ntype = "comment";
    nt.notificationId = taskId;
    notificationResource.save(nt);
    $timeout(getComments, 500);
  }

})

app.controller('todoController', function ($scope, todoResource) {

  TodoResource.get({user: 1}, function(data){
    $scope.countNotification = data.count;
    $scope.notifications = data.results;
  });

  $scope.allRead = function () {
    var cm = new taskCommentsResource2;
    cm.task = taskId;
    cm.user = 1;
    cm.comment = $scope.cm.comment;
    taskCommentsResource.save(cm);

    // notifica al usuario
    var nt = new notificationResource;
    nt.user = 1;
    nt.ntype = "comment";
    nt.notificationId = taskId;
    notificationResource.save(nt);
    $timeout(getComments, 500);
  }

})










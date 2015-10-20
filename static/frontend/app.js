//para hacer uso de $resource debemos colocarlo al crear el modulo
var app = angular.module('app', ["ngResource", 'ngCookies', 'ngRoute', 'ui.bootstrap', 'ui.select',
 'ngSanitize', 'xeditable']);

app.config(function ($httpProvider, $resourceProvider) {
  $httpProvider.defaults.xsrfCookieName = 'csrftoken';
  $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
  $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
  $resourceProvider.defaults.stripTrailingSlashes = false;
});

app.run(['$http', '$cookies', function($http, $cookies) {
  $http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken'];
}]);

app.run(function(editableOptions) {
  editableOptions.theme = 'bs3'; // bootstrap3 theme. Can be also 'bs2', 'default'
});

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

    .when('/todo/', {
      templateUrl : 'todo.html',
      controller  : 'todoController'
    })

    .when('/todo/:done', {
      templateUrl : 'todo.html',
      controller  : 'todoController'
    })

    .when('/client/', {
      templateUrl : 'client.html',
      controller  : 'clientController'
    })

    .when('/2/', {
      templateUrl : 'task2.html',
      controller  : 'taskController'
    })

    .when('/3/', {
      templateUrl : 'task3.html',
      controller  : 'taskController'
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
      'get':    {method:'GET', isArray:false},
      'save':   {method:'POST'},
      'update': {method:'PUT'},
      'query':  {method:'GET', isArray:true},
      'remove': {method:'DELETE'},
      'delete': {method:'DELETE'} 
    });
});

app.factory('organizationResource', function ($resource) {
  return $resource('/organization/:id', {id:'@id'},
    {
      'get':    {method:'GET', isArray:false},
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
      'delete': {method:'DELETE'},
      'markAsRead': { method: 'POST', isArray: true }
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
    $scope.task.user = 1;
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

  // crea nuevo comentario
  $scope.newComment = function () {
    var cm = new taskCommentsResource2;
    cm.task = taskId;
    cm.user = 1;
    cm.comment = $scope.cm.comment;
    cm.$save();

    // notifica al usuario
    var nt = new notificationResource;
    nt.user = 1;
    nt.ntype = "comment";
    nt.notification = taskId;
    nt.$save();
    $timeout(getComments, 500);
  }

  // obtengo tarea actual
  cTask = taskResource.get({ id : taskId }, function(task){
    $scope.task = task;   
  });

  // actualiza tarea actual
  $scope.updateTask = function(){
    cTask = $scope.task;
    cTask.$update();
  }


})

app.controller('mainController', function ($scope, notificationResource, $timeout) {

  getAllNotifications = function() {
    notificationResource.get({read: 'False'}, function(data){
      $scope.countNotification = data.count;
      $scope.notifications = data.results;
    });
  };

  // obtiene todas las notificaciones
  getAllNotifications();

  // marca todas como leidas
  $scope.markAsRead = function(all){
    all.forEach(function(data) {
      data.read = true;
      notificationResource.update({id : data.id}, data);
    });
    $timeout(getAllNotifications, 500);
  }
})

app.controller('todoController', function ($scope, todoResource, $timeout, $routeParams) {

  getTodoTask = function() {
    todoResource.query({user: 1}, function(data){
      $scope.todoTasks = data;
    });
  };

  getTodoTask();

  $scope.addTodo = function () {
    var td = new todoResource;
    td.description = $scope.description;
    td.user = 1;
    td.$save();
    $timeout(getTodoTask, 500);
  }

  $scope.deleteTodo = function (todoId) {
    todoResource.get({id: todoId}, function(data){
      todoResource.delete({id : data.id});
      $timeout(getTodoTask, 500);
    });
  }

  $scope.doneTodo = function (todoId) {
    var td = todoResource.get({id : todoId}, function(data){
      var td = data;
      td.done = !td.done;
      td.$update();
      $timeout(getTodoTask, 500);
    });
  }
})

app.controller('clientController', function ($scope, clientResource, organizationResource) {
  $scope.vm = {
    selectedOrg : null
  };

  getOrganizations = function() {
    organizationResource.query({}, function(data){
      $scope.organizations = data;
    });
  };

  getClients = function() {
    clientResource.query({}, function(data){
      $scope.clients = data;
    });
  };

  getClients();
  getOrganizations();

  $scope.getClient = function(id) {
    clientResource.get({id}, function(data){
      $scope.client = data;
    });
  };

  $scope.setOrganization = function(id) {  
    $scope.org = id;
  }
})
pom.factory('ModelUtils', function($http, $log) {

	var ModelUtils = {
		todos: [],

		get: function () {

			return $http.get('/api/todos/')
				.then(function (response){
					angular.copy(response.data, ModelUtils.todos);
					return ModelUtils.todos;
				});

		},

		create: function (todo) {
			var originalTodos = ModelUtils.todos.slice(0);
			return $http.post('/api/todo/', todo)
				.then(function success(response){
					todo.id = response.data.id;
					ModelUtils.todos.push(todo);
					return ModelUtils.todos;
				}, function error(){
					angular.copy(originalTodos, ModelUtils.todos);
					return ModelUtils.todos;
				});
		},

		put: function (todo) {
			var originalTodos = ModelUtils.todos.slice(0);

			return $http.put('/api/todo/' + todo.pk, todo)
				.then(function success() {
					return ModelUtils.todos;
				}, function error() {
					angular.copy(originalTodos, ModelUtils.todos);
					return originalTodos;
				});

		},

		delete: function (todo) {
			var originalTodos = ModelUtils.todos.slice(0);

			ModelUtils.todos.splice(ModelUtils.todos.indexOf(todo),1);
			console.log(todo)
			return $http.delete('/api/todo/'+todo.pk)
				.then(function success() {
					return ModelUtils.todos;
				}, function error() {
					angular.copy(originalTodos, ModelUtils.todos);
					return originalTodos;
				});
		},
	};
	
	return ModelUtils;
});
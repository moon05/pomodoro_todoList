pom.controller('ListCtrl', function ListCtrl($scope, $log, $http, ModelUtils, $timeout) {

	$scope.intialize = function(data) {
		$log.log('initialize',data);
		$scope.initData = "InitializingData";
	};

	$scope.loadItems = function() {
		$scope.items = $http.get('/api/todo/').then(function(response) {
			return response.data;
		});

		$timeout(function(){
			$scope.loadItems();
		}, 50000);
	};

	$scope.loadItems();

	$scope.currentItem = {};

	//POSTING WORKS!!!!
	$scope.addItem = function() {
		
		if (!$scope.currentItem.description) {
			return;
		}
		$scope.saving = true;
		ModelUtils.create($scope.currentItem);
		$scope.currentItem = {};
		$scope.saving = false;
		ModelUtils.get();
		$scope.loadItems();
	};

	$scope.editedItem = {};
	$scope.selected = {};

	$scope.newField = {};
	$scope.editing = false;
	$scope.pk = 0;


	//EDITING WORKS !!!!
	$scope.editFields = function(todo) {
		$scope.editing = todo.pk;
		$scope.newField = angular.copy(todo);
		$scope.pk = $scope.newField.pk;

	}
	$scope.saveField = function(newtodo){
		console.log($scope.editing);
		if ($scope.editing !== false){
			$scope.pk = $scope.newField.pk;
			ModelUtils.put(newtodo);
			$scope.editing = false;
		}
	};
	$scope.cancel = function(){
		console.log($scope.editing);
		if ($scope.editing !== false){
			$scope.editing = false;
		}
	};

	//REMOVING WORKS!!!!
	$scope.removeItem = function (todo) {
		ModelUtils.delete(todo);
		ModelUtils.get();
		$scope.loadItems();

	}
});
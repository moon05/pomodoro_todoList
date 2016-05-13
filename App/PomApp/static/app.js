var pom = angular.module('pom', ['ngCookies']);

pom.config(function($interpolateProvider) {
	$interpolateProvider.startSymbol('{[{');
	$interpolateProvider.endSymbol('}]}');
});

pom.run(function($rootScope, $log, $http, $cookies) {
	$http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken'];
});

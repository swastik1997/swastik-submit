var front=angular.module('front',['ngRoute']);

front.config(function($routeProvider){
	$routeProvider
	.when('/',{
		templateUrl: 'login.html'
	})
	.when('/register',{
		templateUrl: 'register.html'
	})
	.when('/dashboard',{
		templateUrl: 'dashboard.html',
		controller: 'logoutCtrl'
	})
	.when('/profile',{
		templateUrl: 'profile.html',
		controller: 'logoutCtrl'
	})
	.otherwise({
		redirectTo: '/'
	});
});

front.config(function ($qProvider) {
    $qProvider.errorOnUnhandledRejections(false);
});

front.controller('loginCtrl',function($scope,$location,$http){
	$scope.login=function(){
		var loginData=[{'username':$scope.username,'password':$scope.password}];
		$http({
			method:'POST',
			url:'http://127.0.0.1:8000/PhotoDrive/login/',
			data:loginData,
			headers: {'Content-Type':'application/json'}
		}).then(function successCallback(response){
            if (response.status==200)
            {
            	//alert("Wrong username or password");
            	$location.path('/dashboard');
            }
            else
            {
            	alert("Wrong username or password");
            	$location.path('/');
            }
        },function errorCallback(response) {
            alert(response.status+" Something went wrong");
            $location.path('/');
        });
	}
	$scope.register=function(){
		var loginData=[{
			'username':$scope.username,
			'first':$scope.first,
			'last':$scope.last,
			'gender':$scope.gender,
			'profilepic':$scope.profilepic,
			'email':$scope.email,
			'password':$scope.password,
		}];
		$http({
			method:'GET',
			url:'http://127.0.0.1:8000/PhotoDrive/create/',
			data:loginData,
			headers: {'Content-Type':'application/json'}
		}).then(function successCallback(response){
            if (response.status==200)
            {
            	//alert("Wrong username or password");
            	$location.path('/');
            }
            else
            {
            	alert("Something went Wrong");
            	$location.path('/register');
            }
        },function errorCallback(response) {
            alert(response.status+" Something went wrong");
            $location.path('/');
        });
	}
});

front.controller('logoutCtrl',function($scope,$location,$http){
	$scope.user;
	$scope.logout=function(){
		$http({
			method:'POST',
			url:'http://127.0.0.1:8000/PhotoDrive/logout/',
			headers: {'Content-Type':'application/json'}
		}).then(function successCallback(response){
            if (response.status==200){
            	$location.path('/');
            }
            else{
            	alert("Can't logout");
            	$location.path('/dashboard');
            }
        },function errorCallback(response) {
            alert(response.status+" Something went wrong");
            $location.path('/dashboard');
        });
	}

	$scope.profile=function(){
		$http({
			method:'GET',
			url:'http://127.0.0.1:8000/PhotoDrive/',
			headers: {'Content-Type':'application/json'}
		}).then(function successCallback(response){
            if (response.status==200){
            	$scope.user=response.data;
            	$location.path('/profile');
            }
            else{
            	alert("Can't logout");
            	$location.path('/dashboard');
            }
        },function errorCallback(response) {
            alert(response.status+" Something went wrong");
            $location.path('/dashboard');
        });
	}

	$scope.dashboard=function(){
    	$location.path('/dashboard');
	}
});







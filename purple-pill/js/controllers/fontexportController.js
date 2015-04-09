app.controller('fontexportController', function($scope, $http, sharedScope) {
    $scope.data = sharedScope.data;

    $scope.checkAll = function() {
        angular.forEach($scope.data.families, function(family) {
            angular.forEach(family.instances, function(instance) {
                instance.exportFont = true;
            });
        }); 
        $scope.data.localmenu.fonts = false;
    };
    
    $scope.uncheckAll = function() {
        angular.forEach($scope.data.families, function(family) {
            angular.forEach(family.instances, function(instance) {
                instance.exportFont = false;
            });
        }); 
        $scope.data.localmenu.fonts = false;
    };
    
    $scope.data.exportFonts = function (){
        console.log("exporting");
    };


});
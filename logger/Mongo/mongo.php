<?php



class mongoDao{

	private $manager;

	function __construct() {
       $this->manager=new MongoDB\Driver\Manager("mongodb://localhost:27017");
   }

   function executeSimpleQuery($collection,$query){
	return $this->manager->executeQuery($collection, $query);

   }


}



?>
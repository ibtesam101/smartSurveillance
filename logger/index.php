
<!DOCTYPE html>
<html>
<head>
	<title>Logger</title>
	 <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
 
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
	
</head>
<body>
<h3 class="text text-primary"> Date Based Search</h3>
<form method="post" action="index.php">
<input type="date" name="date" id="searchdate" />
<button type="submit" class="btn btn-primary">Search</button>
</form>
<br>


<h3 class="text text-primary"> Location Search</h3>
	<form method="post" action="index.php">
	<input type="text" name="location" id="location" />
	<button type="submit" class="btn btn-primary">Search</button>
</form>
<br>

<div class="result"> </div>
</body>
</html>


<?php
//  Mongo to PHP Date Converter
function mongo_phpDate($date){
	$utcdatetime = ($date);
	$datetime = $utcdatetime->toDateTime();
	return $datetime;

}


require_once('Mongo/mongo.php');

$mongoManager=new mongoDao;

if(isset($_POST['date'])){
	 $val=$_POST['date'];
	$query = new MongoDB\Driver\Query([]);
	$cursor = $mongoManager->executeSimpleQuery('database.collection', $query);

	foreach ($cursor as $document) {
     	$doc=(array)$document;
    	$datetime=mongo_phpDate($doc['detection_time']);
		$curr=($datetime->format('Y-m-d'));
		$fullDate=$datetime->format("Y-m-d H:i:s");
 		if(!($curr ==($val))){
 			continue;
 		}

echo<<<_ENDL
<div>
<h2 class="text text-primary"> $fullDate </h2>
<h4 class="text text-primary">Location: $doc[location] </h4>
<img src="$doc[path]" />
</div>

_ENDL;

		}

}

if(isset($_POST['location'])){

$query = new MongoDB\Driver\Query(['location'=>$_POST['location']]);

$cursor = $mongoManager->executeSimpleQuery('database.collection', $query);

	foreach ($cursor as $document) {
     	$doc=(array)$document;
     	$datetime=mongo_phpDate($doc['detection_time']);
		$fullDate=$datetime->format("Y-m-d H:i:s");

echo<<<_ENDL
<div>
<h2 class="text text-primary"> $fullDate </h2>
<h4 class="text text-primary">Location: $doc[location] </h4>
<img src="$doc[path]" />
</div>

_ENDL;

		}


}






 

?>
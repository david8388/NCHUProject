<?php
header('Access-Control-Allow-Origin: *');
$servername = "172.16.100.134";
$username = "test123";
$password = "test123";
$dbname = "aiotdb";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT * FROM sensors";
// Perform query
if ($result = $conn -> query("$sql")) {
  echo "Returned rows are: " . $result -> num_rows;
  $output=[];
  $i=0;
  while($row = $result -> fetch_array(MYSQLI_NUM)){
    $output[$i]=$row;
    $i = $i + 1;
  }
}

echo json_encode($output);
// Free result set
$result -> free_result();
$conn->close();
?>
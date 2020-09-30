<?php

    // Cross-Origin Resource Sharing Header
    header('Access-Control-Allow-Origin: *');
    header('Access-Control-Allow-Methods: GET, POST, PUT, DELETE, OPTIONS');
    header('Access-Control-Allow-Headers: X-Requested-With, Content-Type, Accept');

    //使用者資訊
    $host = "localhost";
    $user = "test123";
    $pass = "test123";

    //資料庫資訊
    $databaseName = "aiotdb";
    $tableName = "sensors";


    //連結資料庫
    $con = mysqli_connect($host,$user,$pass, $databaseName);
    //$dbs = mysql_select_db($databaseName, $con);


    //資料庫Sql query語法
    $sql = "UPDATE $tableName SET status = ".rand(0,1)."
        where id > 0";

    //執行query語法
    $result = mysqli_query($con,$sql);
   
    mysqli_close($con);
	header("Location: http://localhost/aiot/")
?>

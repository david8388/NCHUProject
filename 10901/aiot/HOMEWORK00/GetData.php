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
    $sql = "SELECT * FROM $tableName";

    //執行query語法
    $result = mysqli_query($con,$sql);

       
   
    //取出資料
    $data=array();
    while ($row = mysqli_fetch_array($result)){
      array_push($data, $row);
    }

    //輸出並且轉成json格式
    echo json_encode($data);
    mysqli_close($con);
?>

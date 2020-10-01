<?php

    //使用者資訊
    $host = "127.0.0.1";
    $user = "test123";
    $pass = "test123";

    //資料庫資訊
    $databaseName = "aiotdb"; //資料庫名稱
    $tableName = "sensors"; // 資料表單名稱

    //連結資料庫t
    $con = mysqli_connect($host,$user,$pass, $databaseName);
    
    for ($i=0; $i < 40; $i++) { 
        //新增資料至資料庫
        $humi = rand (0, 100);
        $temp = rand (0, 100);
        $value = rand (0, 100);
        $status = rand(0,1);
        $sql = "insert into $tableName (humi,temp,value,status) VALUES (".$humi.",".$temp.",".$value.",".$status.")";
        $result=mysqli_query($con,$sql);
    }     

	header("Location: http://localhost/aiot/")
?>

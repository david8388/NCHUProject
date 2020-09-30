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
    //檢查是否有接收到資料
    if( $_GET["h"] || $_GET["t"] || $_GET["l"] ) {
        $humi = $_GET['h'];
        $temp = $_GET['t'];
        $value = $_GET['l'];
        $staus = 0;
        //新增資料至資料庫
        $sql = "insert into $tableName (humi,temp,value,status) VALUES (".$humi.",".$temp.",".$value.",".$staus.")";
        $result=mysqli_query($con,$sql);
    }else{
        echo "_GET error";
    }
	header("Location: http://localhost/aiot/")
?>

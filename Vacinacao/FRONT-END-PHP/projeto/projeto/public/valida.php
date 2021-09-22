<?php
    
    $id = filter_input(INPUT_POST, 'userID',FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'userEmail',FILTER_SANITIZE_STRING);
    $name = filter_input(INPUT_POST, 'userName',FILTER_SANITIZE_STRING);
    $picture = filter_input(INPUT_POST, 'userPicture',FILTER_SANITIZE_STRING);

    $_SESSION['userID'] = $id;
    $_SESSION['userEmail'] = $email;
    $_SESSION['userName'] = $name;
    $_SESSION['userPicture'] = $picture;


echo $email;
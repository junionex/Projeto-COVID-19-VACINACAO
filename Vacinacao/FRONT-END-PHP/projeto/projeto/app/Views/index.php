<!doctype html>
<html lang="en">
  <head>


<!------ Include the above in your HEAD tag ---------->
<!--GOOGLE-->
<script src="https://apis.google.com/js/platform.js" async defer></script>
<meta name="google-signin-client_id" content="389047770490-4hr89plamfc0oh8b3m6crs3bv18q1sni.apps.googleusercontent.com">
    <title>Entrar com Google</title>
    <link href="https://fonts.googleapis.com/css2?family=Righteous&display=swap" rel="stylesheet">
    <link rel="icon" href="https://imunizarvacinas.com.br/wp-content/uploads/2018/02/Icon-seringa-03.png">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Audiowide">
    <link rel="stylesheet" type="text/css" href="<?=base_url('css/login.css')?>" media="screen" class="white-mode">

    <style>
        body {
          background: #FFFFFF url("https://cdn.the-scientist.com/assets/articleNo/66312/aImg/33161/syringe-l.jpg") no-repeat ;
          background-size: 1550px 700px;
}
      #field{
        
        position: fixed;
        text-align: center;
        width: 31%;
        height: 50%;
        margin: 80px;
        background-color: rgb(244, 250, 252);
        border-radius: 30px;
        margin-left: 30px;
        background-image: url('https://i.pinimg.com/474x/d7/23/e0/d723e02b40b8f0be7f6eb7a527415375.jpg');
        background-repeat: no-repeat;
        background-position: bottom;
        
        
        background-size: 100%;
      }
      #a{
       position: fixed;
       margin-top: 300px;
      margin-left: 200px;
      }
     h5{
       color: black;
     }
     
    </style>

  </head>

  <body>
    <fieldset id="field">
    
      <div class="title"><br>
      <h1 style="margin-right: px;font-weight: 800; ">Vacinas<br/>RN</h1>

</div></fieldset>
  <p id="msg">
  <br>
  <div id="a"  class="g-signin2" data-onsuccess="onSignIn"></div>

                          <script>
                            function renderButton() {
                             
                                gapi.signin2.render('onSignIn', {
                                  'scope': 'profile email',
                                  'width': 240,
                                  'height': 50,
                                  'longtitle': true,
                                  'theme': 'dark',
                                  'onsuccess': onSuccess,
                                  'onfailure': onFailure
                                });
                              }

                            function onSignIn(googleUser) {
                              /*var profile = googleUser.getBasicProfile();
                              console.log("ID:" + profile.getId());
                              console.log("Name: " + profile.getName());
                              console.log('Image URL' + profile.getImageUrl());
                              console.log('Email:' + profile.getEmail());*/
                              var profile = googleUser.getBasicProfile();
                              var userID = profile.getId(); 
                              var userName = profile.getName(); 
                              var userPicture = profile.getImageUrl(); 
                              var userEmail = profile.getEmail(); 			 
                              var userToken = googleUser.getAuthResponse().id_token;

                              //document.getElementById('msg').innerHTML = userEmail;
                              if(userName !== ''){
                                var dados = {
                                  userID:userID,
                                  userName:userName,
                                  userPicture:userPicture,
                                  userEmail,userEmail
                                }
                                $.post('Home/logar',dados, function(retorna){
                                  document.getElementById('msg').innerHTML = retorna;
                                  window.location.href="ControllerVacinacao";
                                });
                              }else{
                                var msg = 'Usuario não encontrado!';
                                document.getElementById('msg').innerHTML = msg;
                              }
                            }
                             
                          </script>
                          <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script> 
                                     
				</div></p>
			</div>
		</div>
	</div>
</div>   
      
</body>
</html>
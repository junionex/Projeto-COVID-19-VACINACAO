<?php

namespace App\Controllers;

class Home extends BaseController
{
	public function index()
	{
		return view('index');
	}
	public function logar()
	{
		$id = filter_input(INPUT_POST, 'userID',FILTER_SANITIZE_STRING);
		$email = filter_input(INPUT_POST, 'userEmail',FILTER_SANITIZE_STRING);
		$name = filter_input(INPUT_POST, 'userName',FILTER_SANITIZE_STRING);
		$picture = filter_input(INPUT_POST, 'userPicture',FILTER_SANITIZE_STRING);
		$_SESSION['user'] = [];
		$_SESSION['user']['ID'] = $id;
		$_SESSION['user']['Email'] = $email;
		$_SESSION['user']['Name'] = $name;
		$_SESSION['user']['Picture'] = $picture;

		//return $_SESSION['user']['Name'];
	}
	public function logout()
	{
		session_destroy();
     	return redirect()->to(site_url("home"));
	}
	public function faixaetaria()
	{

     	return view("faixaetaria");
	}
	public function santoantonioview()
	{

     	return view("santoantonioview");
	}

}

<?php

namespace App\Controllers;

class ControllerVacinacao extends BaseController
{
	public function _remap($method, ...$params) { 
        if (isset($_SESSION["user"]) == false){ 
            return redirect()->to(site_url("home")); 
        } 
        //caso esteja, chama o metodo 
        return $this->$method(...$params); 
    }
    public function index()
	{
		$curl = curl_init();
		curl_setopt_array($curl, array(
			CURLOPT_URL => 'localhost:5000',
			CURLOPT_RETURNTRANSFER => true,
			CURLOPT_ENCODING => '',
			CURLOPT_MAXREDIRS => 10,
			CURLOPT_TIMEOUT => 0,
			CURLOPT_FOLLOWLOCATION => true,
			CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
			CURLOPT_CUSTOMREQUEST => 'GET',
		));
			$response = curl_exec($curl);
			
			$arr = ['dados' => json_decode($response)];
			//print($arr['dados']->total[0][0]);
			//die();
			

		return view('ViewVacinacao',$arr);
	}
	public function cidade($cidade)
	{

		if($cidade == "LAGOA D'ANTA"){
			$cidade = "LAGOA D''ANTA";
		}
		if($cidade == "OLHO-D'AGUA DO BORGES"){
			$cidade = "OLHO-D''AGUA DO BORGES";
		}

		//Chamando API
		$curl = curl_init();
		

		curl_setopt_array($curl, array(
		CURLOPT_URL => 'localhost:5000/cidade',
		CURLOPT_RETURNTRANSFER => true,
		CURLOPT_ENCODING => '',
		CURLOPT_MAXREDIRS => 10,
		CURLOPT_TIMEOUT => 0,
		CURLOPT_FOLLOWLOCATION => true,
		CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
		CURLOPT_CUSTOMREQUEST => 'GET',
		CURLOPT_POSTFIELDS =>'{
			"city":"'.$cidade.'"
		}',
		CURLOPT_HTTPHEADER => array(
			'Content-Type: application/json'
		),
		));

		$response = curl_exec($curl);
		curl_close($curl);
		$arr = ['dados' => json_decode($response)];
		return view("ViewCidade",$arr);
	}
	public function faixaetaria(){
		$curl = curl_init();
		curl_setopt_array($curl, array(
			CURLOPT_URL => 'localhost:5000/idade',
			CURLOPT_RETURNTRANSFER => true,
			CURLOPT_ENCODING => '',
			CURLOPT_MAXREDIRS => 10,
			CURLOPT_TIMEOUT => 0,
			CURLOPT_FOLLOWLOCATION => true,
			CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
			CURLOPT_CUSTOMREQUEST => 'GET',
		));
			$response = curl_exec($curl);
			
			$arr = ['dados' => json_decode($response)];

		return view("faixaetaria",$arr);
	}
}

?>

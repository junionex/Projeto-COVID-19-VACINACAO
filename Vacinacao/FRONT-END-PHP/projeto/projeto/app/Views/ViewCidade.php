<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <!-- This file has been downloaded from Bootsnipp.com. Enjoy! -->
    <title>Vacinas RN</title>
    <link href="https://fonts.googleapis.com/css2?family=Righteous&display=swap" rel="stylesheet">
    <link rel="icon" href="https://imunizarvacinas.com.br/wp-content/uploads/2018/02/Icon-seringa-03.png">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.0/css/bootstrap.min.css" rel="stylesheet">
    <link href="<? site_url('css/estilo.css')?>" rel="stylesheet">
    <style type="text/css">
        @import url('https://maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css');
        @import url("https://fonts.googleapis.com/icon?family=Material+Icons");
@media(min-width:768px) {
    body {
        margin-top: 50px;
        
    }
    /*html, body, #wrapper, #page-wrapper {height: 100%; overflow: hidden;}*/
}

#wrapper {
    padding-left: 0;    
    background-color: 'white';
    
}

#page-wrapper {
    width: 100%;        
    padding: 50px;
    
   
}

@media(min-width:768px) {
    #wrapper {
        padding-left: 225px;
        
    }

    #page-wrapper {
        padding: 22px 10px;
        background-image: url("data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBw4NDQ0NDQ0NDw0NDQ0NDQ0NDQ8ODQ0NFREWFhURFRUYHSggGBolGxUVITEhJSkrLi4uFx8zODMsNygtLisBCgoKDQ0NFg0PFSsZFRkrLSsrKysrKysrKys3Kys3NystKysrKysrKy0tKystLSsrKysrKysrKysrKysrKysrK//AABEIAKwBJgMBIgACEQEDEQH/xAAXAAEBAQEAAAAAAAAAAAAAAAAAAQIH/8QAIhABAQABAgUFAAAAAAAAAAAAAAERIWECgcHw8SIxQVFx/8QAFAEBAAAAAAAAAAAAAAAAAAAAAP/EABQRAQAAAAAAAAAAAAAAAAAAAAD/2gAMAwEAAhEDEQA/AO4gAAAlu3P6UAAAASQFAAAAAAAAAAAAAAAAZ4rZeHEtluLdPTMXXpzaAAAAAAAAAAAAAAAAAAAAAAAAAAAAABM+VAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEuygAAAABAAAAAAAAAAAAAAAAAAAE7/VAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEsBQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAmFAAAAASVQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAS5+NPbfTKgAAAAAAAAAAAAAAAYAAAAAAAAASqAAAAAP/9k=");
        background-size: 100%;
        background-repeat: no-repeat;
        
    }
}

/* Top Navigation */

.top-nav {
    padding: 0 15px;
   
}

.top-nav>li {
    display: inline-block;
    float: left;
    
}

.top-nav>li>a {
    padding-top: 20px;
    padding-bottom: 20px;
    line-height: 20px;
    color: #fff;
    
}

.top-nav>li>a:hover,
.top-nav>li>a:focus,
.top-nav>.open>a,
.top-nav>.open>a:hover,
.top-nav>.open>a:focus {
    color: #fff;
    background-color: #5882FA;
    
}

.top-nav>.open>.dropdown-menu {
    float: left;
    position: absolute;
    margin-top: 0;
    /*border: 1px solid rgba(0,0,0,.15);*/
    border-top-left-radius: 0;
    border-top-right-radius: 0;
    background-color: #fff;
    -webkit-box-shadow: 0 6px 12px rgba(0,0,0,.175);
    box-shadow: 0 6px 12px rgba(0,0,0,.175);
    
}

.top-nav>.open>.dropdown-menu>li>a {
    white-space: normal;
    border: #222;
}

/* Side Navigation */

@media(min-width:768px) {
    .side-nav {
        position: fixed;
        top: 60px;
        left: 225px;
        width: 225px;
        margin-left: -225px;
        border: none;
        border-radius: 0;
        border-top: 1px rgba(0,0,0,.5) solid;
        overflow-y: auto;
        background-color: #222;
        /*background-color: #5A6B7D;*/
        bottom: 0;
        overflow-x: hidden;
        padding-bottom: 40px;
    }

    .side-nav>li>a {
        width: 225px;
        border-bottom: 1px rgba(0,0,0,.3) solid;
    }

    .side-nav li a:hover,
    .side-nav li a:focus {
        outline: none;
        background-color: #5882FA !important;
    }
    }

    .side-nav>li>ul {
        padding: 0;
        border-bottom: 1px rgba(0,0,0,.3) solid;
    }

    .side-nav>li>ul>li>a {
        display: block;
        padding: 10px 15px 10px 38px;
        text-decoration: none;
        color: #999;    
    }

    .side-nav>li>ul>li>a:hover {
        color: #fff;
    }

    .navbar .nav > li > a > .label {
    -webkit-border-radius: 50%;
    -moz-border-radius: 50%;
    border-radius: 50%;
    position: absolute;
    top: 14px;
    right: 6px;
    font-size: 10px;
    font-weight: normal;
    min-width: 15px;
    min-height: 15px;
    line-height: 1.0em;
    text-align: center;
    padding: 2px;
    }

    .navbar .nav > li > a:hover > .label {
    top: 10px;
    }

    .navbar-brand {
        padding: 5px 15px;
        
    }
    #dashboardcenter{
        
        font-size: 17px;
    }
    #borda-top{
        border: none;
    }
    #bg-vacinados{
        background-image: url("data:image/jpeg;base64,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");
        background-size: 100%;
        background-repeat: no-repeat;
    }
    #submenu-1, li{
        font-size: 13px;
        color: gray;
        
    }
    </style>
    <script src="http://code.jquery.com/jquery-1.11.1.min.js"></script>
    <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.0/js/bootstrap.min.js"></script>
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">
      google.charts.load('current', {'packages':['bar']});
      google.charts.setOnLoadCallback(drawChart);
      function drawChart() {
        var data = google.visualization.arrayToDataTable([
          ['Sexo', 'Total'],
          ['Homens', <?=$dados->resposta->total_masculino[0][0] ?>],
          ['Mulheres', <?=$dados->resposta->total_feminino[0][0] ?>],
        ]);
        var options = {
          chart: {
            title: 'Total de Vacinados por Sexo (Mil)',
            subtitle: '',
           
          }
        };
        var chart = new google.charts.Bar(document.getElementById('columnchart_material'));
        //var chart2 = new google.charts.Bar(document.getElementById('columnchart_material2'));
        chart.draw(data, google.charts.Bar.convertOptions(options));
        //chart2.draw(data, google.charts.Bar.convertOptions(options));
      }
    </script>
    <!--Segundo grafico-->
    
</head>
<body>

<div id="throbber" style="display:none; min-height:120px;"></div>
<div id="noty-holder"></div>
<div id="wrapper">
    <!-- Navigation -->
    <nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <!-- Brand and toggle get grouped for better mobile display -->
        <div class="navbar-header">
            <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-ex1-collapse">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
        </div>
            <a class="navbar-brand" href="<?= site_url("ControllerVacinacao/index");?>">
                <img src="https://www.ssm.gov.mo/docs//18772//18772_c217bde127534df0b5f346ec55db76b5_000.png" style="position:relative; margin-left: 8px; width: 60px; height: 60px"   alt="LOGO">
            </a>
        
        <!-- Top Menu Items -->
        <p style="font-size: 35px; color: white; text-align: center; position:absolute;float: left;right: 78%; top: 10px; font-family:'Righteous', cursive">Vacinas RN</p>
        <ul class="nav navbar-right top-nav">
            
            <li><a href="<?= site_url("ControllerVacinacao/index"); ?>" data-placement="bottom" data-toggle="tooltip" href="#" data-original-title="Stats"><i class="fa fa-bar-chart-o"></i>
                </a>
            </li>            
            <li class="dropdown">
                <a href="#" class="dropdown-toggle" data-toggle="dropdown"><?php print($_SESSION['user']['Name'])?> <b class="fa fa-angle-down"></b></a>
                <ul class="dropdown-menu">
                    <!--<li><a href="#"><i class="fa fa-fw fa-user"></i> Edit Profile</a></li>
                    <li><a href="#"><i class="fa fa-fw fa-cog"></i> Change Password</a></li>
                    <li class="divider"></li>-->
                    <li><a href="<?= site_url("home/logout"); ?>"><i class="fa fa-fw fa-power-off"></i> Sair</a></li>
                </ul>
            </li>
        </ul>
        <!-- Sidebar Menu Items - These collapse to the responsive navigation menu on small screens -->
        
        <div id="borda-top" class="collapse navbar-collapse navbar-ex1-collapse"><br><br>
    
            <ul id="dashboardcenter" class="nav navbar-nav side-nav">
                <li></br>
                    <a href="<?= site_url("ControllerVacinacao"); ?>" rel="https://img.icons8.com/ios/2x/dashboard.png"  ></i>
                    <span class="material-icons">dashboard</span> Dashboard</i></a>
                    
                </li>
                <li>
                    <a href="#" data-toggle="collapse" data-target="#submenu-1"><i class="material-icons"></i>
                    <span class="material-icons">place</span> Cidades <i class="fa fa-fw fa-angle-down pull-right"></i></a>

                    <ul id="submenu-1" class="collapse">
                        <?php foreach ($dados->cidades as $item):?>
                            <li><a href="<?= site_url("ControllerVacinacao/cidade/{$item[0]}")?>"> <?php print($item[0]) ?> </a></li>
                        <?php endforeach; ?>
                    </ul>
                </li>
                <li>
                    <a href="<?= site_url("ControllerVacinacao/faixaetaria"); ?>" > 
                    <span class="material-icons">family_restroom</span> Faixa Etária</a>

                </li>
                <!--<li>
                    <a href="sugerencias"><i class="fa fa-fw fa-paper-plane-o"></i> MENU 4</a>
                    <ul id="submenu-1" class="collapse">
                        <li><a href="#"><i class="fa fa-angle-double-right"></i> SUBMENU 1.1</a></li>
                        <li><a href="#"><i class="fa fa-angle-double-right"></i> SUBMENU 1.2</a></li>
                        <li><a href="#"><i class="fa fa-angle-double-right"></i> SUBMENU 1.3</a></li>
                    </ul>
                </li>
                <li>
                    <a href="faq"><i class="fa fa-fw fa fa-question-circle"></i> MENU 5</a>
                </li>-->
            </ul>
        </div>
        
        <!-- /.navbar-collapse -->
    </nav>

    <div id="page-wrapper">
        <div class="container-fluid">
            <!-- Page Heading -->
            <div class="row" id="main" >
                <div id="bg-vacinados" class="col-sm-12 col-md-12 well" id="content">
                    <h1 style="font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif; text-align:center; color:white"><?=$dados->pesquisado?></h1>
                </div>
                <p style="font-family:sans-serif; text-align: center; font-size:30px; font-family: Arial"> Dados de Vacinados na Cidade de <?=$dados->pesquisado?>.</p>
            </div>
            <div id="page-wrapper">
        <div class="container-fluid">
            <!-- Page Heading -->
            <div class="row" id="main" >
                <div class="col-sm-12 col-md-12 well" id="content" style="margin-right: 10%;width: 40%;background-color: white;">
                    <div id="columnchart_material" style="width: 400px; height: 400px;"></div>
                </div>
                <div class="col-sm-12 col-md-12 well" id="content" style="margin-right: 10%;width: 40%;background-color: white">
                    <h5 style="font-family: arial; font-size: 16px; color: gray">Número de vacinados por dose (Mil)</h5>
                    <canvas id="myChart" width="300px" height="350"></canvas>
                    <script src='https://cdnjs.cloudflare.com/ajax/libs/Chart.js/1.0.2/Chart.min.js'></script>
                    <script type="text/javascript">
                        // http://www.chartjs.org/docs/#doughnut-pie-chart-introduction
                                        
                                        var data = [{
                                            value: <?=$dados->resposta->total_primeira_dose[0][0] ?>,
                                            color: "#5882FA",
                                            highlight: "#2571a7",
                                            label: "1º Dose"
                                        },
                                        {
                                            value: <?=$dados->resposta->total_segunda_dose[0][0] ?>,
                                            color:"#FF5A5E",
                                            highlight: "#F7464A",
                                            label: "2º Dose"
                                        },
                                        
                                       
                                    ];
                                   

                                    var ctx = document.getElementById("myChart").getContext("2d");
                                    new Chart(ctx).Pie(data);
                                    //new Chart(ctx).Doughnut(data);
                    </script>
                </div>
            </div>
            
                                
            <div class="col-sm-12 col-md-12 well" id="content" style="margin-right: 10%;width: 100%;background-color: white">
                    <h5 style="font-family: arial; font-size: 16px; color: gray">Total  de Vacinados por Faixa Etária (Mil)</h5>
                    <canvas id="myChart2" style="margin-right: 10%;width: 100%;" width="1200px" height="400px"></canvas>
                    <script src='https://cdnjs.cloudflare.com/ajax/libs/Chart.js/1.0.2/Chart.min.js'></script>
                    <script type="text/javascript">
                        var data = {
                        labels: ["15 a 19", "20 a 24",'25 a 29','30 a 34','35 a 39','40 a 44','45 a 49','50 a 54','55 a 59','60 a 64','65 a 69','70 a 74','75 a 79','80 a 84','85 a 89','90 a 94','95 a 99','100 a 104'],
                        datasets: [
                            {
                                label: "Faixa Etária",
                                fillColor: "#5882FA",
                                strokeColor: "rgba(0,0,0,0)",
                                highlightFill: "rgb(60, 85, 213)",
                                //highlightStroke: "rgba(220,220,220,1)",
                                data: [<?=$dados->resposta->idade_15_a_19[0][0]?>,
                                        <?=$dados->resposta->idade_20_a_24[0][0]?>,
                                        <?=$dados->resposta->idade_25_a_29[0][0]?>,
                                        <?=$dados->resposta->idade_30_a_34[0][0]?>,
                                        <?=$dados->resposta->idade_35_a_39[0][0]?>,
                                        <?=$dados->resposta->idade_40_a_44[0][0]?>,
                                        <?=$dados->resposta->idade_45_a_49[0][0]?>,
                                        <?=$dados->resposta->idade_50_a_54[0][0]?>,
                                        <?=$dados->resposta->idade_55_a_59[0][0]?>,
                                        <?=$dados->resposta->idade_60_a_64[0][0]?>,
                                        <?=$dados->resposta->idade_65_a_69[0][0]?>,
                                        <?=$dados->resposta->idade_70_a_74[0][0]?>,
                                        <?=$dados->resposta->idade_75_a_79[0][0]?>,
                                        <?=$dados->resposta->idade_80_a_84[0][0]?>,
                                        <?=$dados->resposta->idade_85_a_89[0][0]?>,
                                        <?=$dados->resposta->idade_90_a_94[0][0]?>,
                                        <?=$dados->resposta->idade_100_a_104[0][0]?>]
                            }
                        ]
                        };
                        var ctx2 = document.getElementById("myChart2").getContext("2d");
                        var myBarChart2 = new Chart(ctx2).Bar(data);
                        
                    </script>
            </div>
            <p style="font-size: 20px; color:black">Última atualização dos dados: <?=$dados->resposta->ultimo[0][0] ?></p>
            

            
            
            <!-- /.row -->
        </div>
        <!-- /.container-fluid -->
    </div>
    
        </div>
        <!-- /.container-fluid -->
    </div>
    <!-- /#page-wrapper -->
</div><!-- /#wrapper -->

<script type="text/javascript">
$(function(){
    $('[data-toggle="tooltip"]').tooltip();
    $(".side-nav .collapse").on("hide.bs.collapse", function() {                   
        $(this).prev().find(".fa").eq(1).removeClass("fa-angle-right").addClass("fa-angle-down");
    });
    $('.side-nav .collapse').on("show.bs.collapse", function() {                        
        $(this).prev().find(".fa").eq(1).removeClass("fa-angle-down").addClass("fa-angle-right");        
    });
})    
    
</script>
</body>
</html>

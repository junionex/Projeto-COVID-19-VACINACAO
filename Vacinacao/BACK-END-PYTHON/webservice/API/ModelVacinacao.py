#from _typeshed import Self
import psycopg2
##class ModelVacinacao:
host = 'localhost'
dbname = 'Vacinacao'
user = 'postgres'
password = '1234'
sslmode = 'require'
conn_string = "host={0} user={1} dbname={2} password={3}".format(host, user, dbname, password)
conn = psycopg2.connect(conn_string)
print('conectado')
cursor = conn.cursor()

def criarTabela():
    cursor.execute("CREATE TABLE documento(id serial PRIMARY KEY,timestamp VARCHAR(50),paciente_idade INTEGER, paciente_endereco_nmMunicipio VARCHAR(64), vacina_descricao_dose VARCHAR(50), vacina_fabricante_nome varchaR(64), vacina_categoria_nome VARCHAR(50),vacina_nome VARCHAR(64), paciente_enumSexoBiologico VARCHAR(1));")

def addPaciente(cursor,timestamp, paciente_idade, paciente_endereco_nmMunicipio, vacina_descricao_dose, vacina_fabricante_nome, vacina_categoria_nome, vacina_nome,paciente_enumSexoBiologico,id):
    cursor.execute("INSERT INTO documento (timestamp, paciente_idade, paciente_endereco_nmMunicipio, vacina_descricao_dose, vacina_fabricante_nome, vacina_categoria_nome, vacina_nome,paciente_enumSexoBiologico, id) VALUES (%s,%s, %s,%s,%s,%s,%s,%s,%s);", (timestamp, paciente_idade, paciente_endereco_nmMunicipio, vacina_descricao_dose, vacina_fabricante_nome, vacina_categoria_nome, vacina_nome,paciente_enumSexoBiologico, id))
    print('adicionado --'+ timestamp + str("--" +id))

def selecionarTotalCadastrado():
    cursor.execute("SELECT COUNT(*) FROM documento")
    rows = cursor.fetchall()
    return rows
def selecionarPorSexoMasculino():
    cursor.execute("SELECT COUNT(*) FROM documento WHERE paciente_enumSexoBiologico = 'M'")
    rows = cursor.fetchall()
    return rows
def selecionarPorSexoFeminino():
    cursor.execute("SELECT COUNT(*) FROM documento WHERE paciente_enumSexoBiologico = 'F'")
    rows = cursor.fetchall()
    return rows
def selecionarPorCidade(cidade):
    cursor.execute("SELECT COUNT(*) FROM documento WHERE paciente_endereco_nmMunicipio ='"+cidade+"';")
    rows = cursor.fetchall()
    return rows
def selecionarPorIdade18a24():
    cursor.execute("SELECT COUNT(*) FROM documento WHERE paciente_idade >= 18 and paciente_idade <= 24")
    rows = cursor.fetchall()
    return rows
def selecionarPorIdade25a60():
    cursor.execute("SELECT COUNT(*) FROM documento WHERE paciente_idade >= 25 and paciente_idade <= 60")
    rows = cursor.fetchall()
    return rows
def selecionarPorIdadeMaiorQue61():
    cursor.execute("SELECT COUNT(*) FROM documento WHERE paciente_idade >= 61")
    rows = cursor.fetchall()
    return rows
def selecionarPrimeiraDose():
    cursor.execute("SELECT COUNT(*) FROM documento WHERE vacina_descricao_dose = '1ª Dose'")
    rows = cursor.fetchall()
    return rows
def selecionarSegundaDose():
    cursor.execute("SELECT COUNT(*) FROM documento WHERE vacina_descricao_dose = '2ª Dose'")
    rows = cursor.fetchall()
    return rows

#sicronizar dados com a tabela
def sicronizar_vacina_aplicada():
    resposta = selecionarTotalCadastrado()
    totalM = selecionarPorSexoMasculino()
    totalF = selecionarPorSexoFeminino()
    totalIdade18a24 = selecionarPorIdade18a24()
    totalIdade25a60 = selecionarPorIdade25a60()
    totalIdadeMaiorque61 = selecionarPorIdadeMaiorQue61()
    totalPrimeiradose = selecionarPrimeiraDose()
    totalSegundadose = selecionarSegundaDose()
    #cmd sql
    cursor.execute("INSERT INTO vacina_aplicada (total_habitante_ibge, total, total_feminino, total_masculino, total_primeira_dose, total_segunda_dose, total_idade_18a24, total_idade_25a60, total_idade_maiorque61, data_de_sicronizacao) VALUES (3534165,%s,%s, %s,%s,%s,%s,%s,%s,now());",(resposta[0],totalF[0],totalM[0],totalPrimeiradose[0],totalSegundadose[0],totalIdade18a24[0],totalIdade25a60[0],totalIdadeMaiorque61[0]))
    fecharConexao(conn,cursor)
    print("atualizado")

def pega_ultimo_dado():
    cursor.execute("SELECT timestamp FROM documento order by timestamp DESC LIMIT 1")
    rows = cursor.fetchall()
    return rows

def pega_as_cidade():
    cursor.execute("SELECT DISTINCT paciente_endereco_nmmunicipio FROM documento ORDER BY paciente_endereco_nmmunicipio ASC")
    rows = cursor.fetchall()
    return rows

def buscar_por_cidade(cidade):
    #cursor.execute("SELECT COUNT(*) FROM documento WHERE paciente_endereco_nmMunicipio ='"+cidade+"';")
    #total = cursor.fetchall()
    cursor.execute("SELECT COUNT(*) FROM documento WHERE paciente_endereco_nmMunicipio ='"+cidade+"' and paciente_enumSexoBiologico = 'M';")
    totalM = cursor.fetchall()
    cursor.execute("SELECT COUNT(*) FROM documento WHERE paciente_endereco_nmMunicipio ='"+cidade+"' and paciente_enumSexoBiologico = 'F';")
    totalF = cursor.fetchall()
    cursor.execute("SELECT COUNT(*) FROM documento WHERE paciente_endereco_nmMunicipio ='"+cidade+"' and paciente_idade >= 18 and paciente_idade <= 24")
    totalIdade18a24 = cursor.fetchall()
    cursor.execute("SELECT COUNT(*) FROM documento WHERE paciente_endereco_nmMunicipio ='"+cidade+"' and paciente_idade >= 25 and paciente_idade <= 60")
    totalIdade25a60 = cursor.fetchall()
    cursor.execute("SELECT COUNT(*) FROM documento WHERE paciente_endereco_nmMunicipio ='"+cidade+"' and paciente_idade >= 61")
    totalIdadeMaiorque61 = cursor.fetchall()
    cursor.execute("SELECT COUNT(*) FROM documento WHERE paciente_endereco_nmMunicipio ='"+cidade+"' and vacina_descricao_dose = '1ª Dose'")
    primeiraDose = cursor.fetchall()
    cursor.execute("SELECT COUNT(*) FROM documento WHERE paciente_endereco_nmMunicipio ='"+cidade+"' and vacina_descricao_dose = '2ª Dose'")
    segundaDose = cursor.fetchall()
    #FOCADADO NAS IDADE
    cursor.execute("SELECT COUNT(*) FROM documento WHERE paciente_endereco_nmMunicipio ='"+cidade+"' and paciente_idade >= 15 and paciente_idade <= 19")
    idade_15_a_19 = cursor.fetchall()
    cursor.execute("SELECT COUNT(*) FROM documento WHERE paciente_endereco_nmMunicipio ='"+cidade+"' and paciente_idade >= 20 and paciente_idade <= 24")
    idade_20_a_24 = cursor.fetchall()
    cursor.execute("SELECT COUNT(*) FROM documento WHERE paciente_endereco_nmMunicipio ='"+cidade+"' and paciente_idade >= 25 and paciente_idade <= 29")
    idade_25_a_29 = cursor.fetchall()
    cursor.execute("SELECT COUNT(*) FROM documento WHERE paciente_endereco_nmMunicipio ='"+cidade+"' and paciente_idade >= 30 and paciente_idade <= 34")
    idade_30_a_34 = cursor.fetchall()
    cursor.execute("SELECT COUNT(*) FROM documento WHERE paciente_endereco_nmMunicipio ='"+cidade+"' and paciente_idade >= 35 and paciente_idade <= 39")
    idade_35_a_39 = cursor.fetchall()
    cursor.execute("SELECT COUNT(*) FROM documento WHERE paciente_endereco_nmMunicipio ='"+cidade+"' and paciente_idade >= 40 and paciente_idade <= 44")
    idade_40_a_44 = cursor.fetchall()
    cursor.execute("SELECT COUNT(*) FROM documento WHERE paciente_endereco_nmMunicipio ='"+cidade+"' and paciente_idade >= 45 and paciente_idade <= 49")
    idade_45_a_49 = cursor.fetchall()
    cursor.execute("SELECT COUNT(*) FROM documento WHERE paciente_endereco_nmMunicipio ='"+cidade+"' and paciente_idade >= 50 and paciente_idade <= 54")
    idade_50_a_54 = cursor.fetchall()
    cursor.execute("SELECT COUNT(*) FROM documento WHERE paciente_endereco_nmMunicipio ='"+cidade+"' and paciente_idade >= 55 and paciente_idade <= 59")
    idade_55_a_59 = cursor.fetchall()
    cursor.execute("SELECT COUNT(*) FROM documento WHERE paciente_endereco_nmMunicipio ='"+cidade+"' and paciente_idade >= 60 and paciente_idade <= 64")
    idade_60_a_64 = cursor.fetchall()
    cursor.execute("SELECT COUNT(*) FROM documento WHERE paciente_endereco_nmMunicipio ='"+cidade+"' and paciente_idade >= 65 and paciente_idade <= 69")
    idade_65_a_69 = cursor.fetchall()
    cursor.execute("SELECT COUNT(*) FROM documento WHERE paciente_endereco_nmMunicipio ='"+cidade+"' and paciente_idade >= 70 and paciente_idade <= 74")
    idade_70_a_74 = cursor.fetchall()
    cursor.execute("SELECT COUNT(*) FROM documento WHERE paciente_endereco_nmMunicipio ='"+cidade+"' and paciente_idade >= 75 and paciente_idade <= 79")
    idade_75_a_79 = cursor.fetchall()
    cursor.execute("SELECT COUNT(*) FROM documento WHERE paciente_endereco_nmMunicipio ='"+cidade+"' and paciente_idade >= 80 and paciente_idade <= 84")
    idade_80_a_84 = cursor.fetchall()
    cursor.execute("SELECT COUNT(*) FROM documento WHERE paciente_endereco_nmMunicipio ='"+cidade+"' and paciente_idade >= 85 and paciente_idade <= 89")
    idade_85_a_89 = cursor.fetchall()
    cursor.execute("SELECT COUNT(*) FROM documento WHERE paciente_endereco_nmMunicipio ='"+cidade+"' and paciente_idade >= 90 and paciente_idade <= 94")
    idade_90_a_94 = cursor.fetchall()
    cursor.execute("SELECT COUNT(*) FROM documento WHERE paciente_endereco_nmMunicipio ='"+cidade+"' and paciente_idade >= 95 and paciente_idade <= 99")
    idade_95_a_99 = cursor.fetchall()
    cursor.execute("SELECT COUNT(*) FROM documento WHERE paciente_endereco_nmMunicipio ='"+cidade+"' and paciente_idade >= 100 and paciente_idade <= 104")
    idade_100_a_104 = cursor.fetchall()
	
    cursor.execute("SELECT timestamp FROM documento WHERE paciente_endereco_nmMunicipio ='"+cidade+"' order by timestamp DESC LIMIT 1")
    ultimo = cursor.fetchall()

    return {"total_masculino":totalM,"total_feminino":totalF,"total_idade_18a24":totalIdade18a24,"total_idade_25a60":totalIdade25a60,"total_idade_Maiorque61":totalIdadeMaiorque61,"total_primeira_dose":primeiraDose,"total_segunda_dose":segundaDose,"idade_15_a_19":idade_15_a_19,"idade_20_a_24":idade_20_a_24,"idade_25_a_29":idade_25_a_29,
            "idade_30_a_34":idade_30_a_34,"idade_35_a_39":idade_35_a_39,"idade_40_a_44":idade_40_a_44,
            "idade_45_a_49":idade_45_a_49,"idade_45_a_49":idade_45_a_49,"idade_50_a_54":idade_50_a_54,
            "idade_55_a_59":idade_55_a_59,"idade_60_a_64":idade_60_a_64,"idade_65_a_69":idade_65_a_69,
            "idade_70_a_74":idade_70_a_74,"idade_75_a_79":idade_75_a_79,"idade_80_a_84":idade_80_a_84,
            "idade_85_a_89":idade_85_a_89,"idade_90_a_94":idade_90_a_94,"idade_95_a_99":idade_95_a_99,
            "idade_100_a_104":idade_100_a_104, "ultimo": ultimo}

def pega_idade():
    cursor.execute("SELECT COUNT(*) FROM documento WHERE paciente_idade >= 15 and paciente_idade <= 19")
    idade_15_a_19 = cursor.fetchall()
    cursor.execute("SELECT COUNT(*) FROM documento WHERE paciente_idade >= 20 and paciente_idade <= 24")
    idade_20_a_24 = cursor.fetchall()
    cursor.execute("SELECT COUNT(*) FROM documento WHERE paciente_idade >= 25 and paciente_idade <= 29")
    idade_25_a_29 = cursor.fetchall()
    cursor.execute("SELECT COUNT(*) FROM documento WHERE paciente_idade >= 30 and paciente_idade <= 34")
    idade_30_a_34 = cursor.fetchall()
    cursor.execute("SELECT COUNT(*) FROM documento WHERE paciente_idade >= 35 and paciente_idade <= 39")
    idade_35_a_39 = cursor.fetchall()
    cursor.execute("SELECT COUNT(*) FROM documento WHERE paciente_idade >= 40 and paciente_idade <= 44")
    idade_40_a_44 = cursor.fetchall()
    cursor.execute("SELECT COUNT(*) FROM documento WHERE paciente_idade >= 45 and paciente_idade <= 49")
    idade_45_a_49 = cursor.fetchall()
    cursor.execute("SELECT COUNT(*) FROM documento WHERE paciente_idade >= 50 and paciente_idade <= 54")
    idade_50_a_54 = cursor.fetchall()
    cursor.execute("SELECT COUNT(*) FROM documento WHERE paciente_idade >= 55 and paciente_idade <= 59")
    idade_55_a_59 = cursor.fetchall()
    cursor.execute("SELECT COUNT(*) FROM documento WHERE paciente_idade >= 60 and paciente_idade <= 64")
    idade_60_a_64 = cursor.fetchall()
    cursor.execute("SELECT COUNT(*) FROM documento WHERE paciente_idade >= 65 and paciente_idade <= 69")
    idade_65_a_69 = cursor.fetchall()
    cursor.execute("SELECT COUNT(*) FROM documento WHERE paciente_idade >= 70 and paciente_idade <= 74")
    idade_70_a_74 = cursor.fetchall()
    cursor.execute("SELECT COUNT(*) FROM documento WHERE paciente_idade >= 75 and paciente_idade <= 79")
    idade_75_a_79 = cursor.fetchall()
    cursor.execute("SELECT COUNT(*) FROM documento WHERE paciente_idade >= 80 and paciente_idade <= 84")
    idade_80_a_84 = cursor.fetchall()
    cursor.execute("SELECT COUNT(*) FROM documento WHERE paciente_idade >= 85 and paciente_idade <= 89")
    idade_85_a_89 = cursor.fetchall()
    cursor.execute("SELECT COUNT(*) FROM documento WHERE paciente_idade >= 90 and paciente_idade <= 94")
    idade_90_a_94 = cursor.fetchall()
    cursor.execute("SELECT COUNT(*) FROM documento WHERE paciente_idade >= 95 and paciente_idade <= 99")
    idade_95_a_99 = cursor.fetchall()
    cursor.execute("SELECT COUNT(*) FROM documento WHERE paciente_idade >= 100 and paciente_idade <= 104")
    idade_100_a_104 = cursor.fetchall()
    return {"idade_15_a_19":idade_15_a_19,"idade_20_a_24":idade_20_a_24,"idade_25_a_29":idade_25_a_29,
            "idade_30_a_34":idade_30_a_34,"idade_35_a_39":idade_35_a_39,"idade_40_a_44":idade_40_a_44,
            "idade_45_a_49":idade_45_a_49,"idade_45_a_49":idade_45_a_49,"idade_50_a_54":idade_50_a_54,
            "idade_55_a_59":idade_55_a_59,"idade_60_a_64":idade_60_a_64,"idade_65_a_69":idade_65_a_69,
            "idade_70_a_74":idade_70_a_74,"idade_75_a_79":idade_75_a_79,"idade_80_a_84":idade_80_a_84,
            "idade_85_a_89":idade_85_a_89,"idade_90_a_94":idade_90_a_94,"idade_95_a_99":idade_95_a_99,
            "idade_100_a_104":idade_100_a_104}

    #criarTabela()
def getPegarConexao():
    return  cursor
def getPegarOConn():
    return conn

def fecharConexao(conn,cursor):
    conn.commit()
    #cursor.close()
    #conn.close()

#sicronizar_vacina_aplicada()
    #fecharConexao(conn,cursor)
#addPaciente(cursor,'12/12/12',18,'nc','vicinacao','nome da vacincao','fabricante','categoria','m','idid')
#fecharConexao(conn,cursor)
#fecharConexao()

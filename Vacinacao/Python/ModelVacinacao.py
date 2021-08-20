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

"""def __init__(self,id, timestamp, paciente_idade, paciente_endereco_nmMunicipio, vacina_descricao_dose, vacina_fabricante_nome, vacina_categoria_nome, vacina_nome,paciente_enumSexoBiologico):
        self.id = id,
        self.timestamp = timestamp,
        self.paciente_idade = paciente_idade,
        self.paciente_endereco_nmMunicipio = paciente_endereco_nmMunicipio,
        self.vacina_descricao_dose = vacina_descricao_dose,
        self.vacina_fabricante_nome = vacina_fabricante_nome,
        self.vacina_categoria_nome = vacina_categoria_nome,
        self.vacina_nome = vacina_nome,
        self.paciente_enumSexoBiologico = paciente_enumSexoBiologico"""

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

    #criarTabela()
def getPegarConexao():
    return  cursor
def getPegarOConn():
    return conn

def fecharConexao(conn,cursor):
    conn.commit()
    #cursor.close()
    #conn.close()

    #fecharConexao(conn,cursor)
#addPaciente(cursor,'12/12/12',18,'nc','vicinacao','nome da vacincao','fabricante','categoria','m','idid')
#fecharConexao(conn,cursor)
#fecharConexao()

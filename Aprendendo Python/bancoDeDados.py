import psycopg2

#configuração

host = 'localhost'
dbname = 'teste'
user = 'postgres'
password = '1234'
sslmode = 'require'

#string de conexão 
conn_string = "host={0} user={1} dbname={2} password={3}".format(host, user, dbname, password)
conn = psycopg2.connect(conn_string)

print('conectado')

cursor = conn.cursor()

# CRIAR TABELA 
def criarTabela():
    cursor.execute("CREATE TABLE inventory(id serial PRIMARY KEY, nome VARCHAR(50), quantity INTEGER);")

#INSERIR NA TABELA
def addnome(id,nome,quantidade):
    cursor.execute("INSERT INTO inventory (id,nome, quantity) VALUES (%s,%s, %s);", (id,nome,quantidade))
    print('adicionado -'+nome)

#LER TABELA
def lerTabela():
    cursor.execute("SELECT * FROM inventory;")
    rows = cursor.fetchall()
    print(rows)
    #for row in rows:
    #    print("Data row = (%s, %s, %s)" %(str(row[0]), str(row[1]), str(row[2])))
#ATUALIZAR DADOS
def atualizarDados(quantidade,id,nome):
    cursor.execute("UPDATE inventory SET quantity = %s,nome = %s WHERE id = %s;", (quantidade,nome,id))
    print("Atualizou 1 linha dos dados")

def deletarDados(id):
    cursor.execute("DELETE FROM inventory WHERE id = %s;", (str(id)))
    print("Deletando 1 linha dos dados")

#addnome(3,"cuscuz",462)
#atualizarDados(785,1,"tapioca")
deletarDados(1)
lerTabela()
conn.commit()

cursor.close()
conn.close()
import mysql.connector

# Configurações de conexão com o banco de dados
db_config = {
    'host': 'seu_host_mysql',
    'user': 'seu_usuario',
    'password': 'sua_senha',
    'database': 'seu_banco_de_dados',
}

# Query que você deseja executar
query = "SELECT * FROM sua_tabela;"

try:
    # Conectar ao banco de dados
    connection = mysql.connector.connect(**db_config)

    # Criar um cursor para executar comandos SQL
    cursor = connection.cursor()

    # Executar a query
    cursor.execute(query)

    # Obter todos os resultados
    results = cursor.fetchall()

    # Exibir os resultados
    for row in results:
        print(row)

except mysql.connector.Error as err:
    print(f"Erro: {err}")

finally:
    # Fechar o cursor e a conexão, independentemente de ter ocorrido um erro ou não
    if 'cursor' in locals() and cursor is not None:
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()

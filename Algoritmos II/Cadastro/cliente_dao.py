import mysql.connector
from cliente import Cliente
class ClienteDAO:
  def incluir(self, cliente):
    conn = mysql.connector.connect(
      host="127.0.0.1",
      user="aluno",
      password="aluno",
      database="lojabd"
    )
    cursor = conn.cursor()
    sql = (f"insert into clientes(email,nome,estado_civil,estuda,trabalha,genero,cep,"
          f"endereco,numero,bairro,cidade,estado,telefone,celular) "
          f"values ('{cliente.getEmail()}','{cliente.getNome()}',{cliente.getEstado_civil()},"
          f"{cliente.getEstuda()},{cliente.getTrabalha()},'{cliente.getGenero()}',"
          f"'{cliente.getCep()}','{cliente.getEndereco()}','{cliente.getNumero()}',"
          f"'{cliente.getBairro()}','{cliente.getCidade()}','{cliente.getEstado()}',"
          f"'{cliente.getTelefone()}','{cliente.getCelular()}')")
    print(sql)
    cursor.execute(sql)
    conn.commit()
    conn.close()
    return True
  
  def excluir(self, email):
    conn = mysql.connector.connect(
      host="127.0.0.1",
      user="aluno",
      password="aluno",
      database="lojabd"
    )
    cursor = conn.cursor()
    sql = (f"delete from clientes where email='{email}'")
    print(sql)
    cursor.execute(sql)
    conn.commit()
    conn.close()
    return True
  
  def atualizar(self, cliente):
    conn = mysql.connector.connect(
      host="127.0.0.1",
      user="aluno",
      password="aluno",
      database="lojabd"
    )
    cursor = conn.cursor()
    sql = (f"update clientes "
          f"set nome='{cliente.getNome()}', estado_civil={cliente.getEstado_civil()},"
          f"estuda={cliente.getEstuda()},trabalha={cliente.getTrabalha()},genero='{cliente.getGenero()}',"
          f"cep='{cliente.getCep()}',endereco='{cliente.getEndereco()}',numero='{cliente.getNumero()}',"
          f"bairro='{cliente.getBairro()}',cidade='{cliente.getCidade()}',estado='{cliente.getEstado()}',"
          f"telefone='{cliente.getTelefone()}',celular='{cliente.getCelular()}'")
    print(sql)
    cursor.execute(sql)
    conn.commit()
    conn.close()
    return True
  
  def consultar(self, email):
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='aluno',
        password='aluno',
        database='lojabd'
    )
    cursor = conn.cursor()
    # structure query language
    sql = f"select * from clientes where email='{email}'" 
    print(sql)
    cursor.execute(sql)
    resultado = cursor.fetchone()
    conn.close()
    if resultado:
        cliente_encontrado = Cliente(*resultado)
        return cliente_encontrado
    else:
        return None
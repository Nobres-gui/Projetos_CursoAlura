import mysql.connector
from mysql.connector import errorcode


print("Conectando...")
try:
      conn = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='*'
      )
except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Existe algo errado no nome de usuário ou senha')
      else:
            print(err)

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS `ong`;")

cursor.execute("CREATE DATABASE `ong`;")

cursor.execute("USE `ong`;")

# criando tabelas
TABLES = {}
TABLES['usuarios'] = ('''
      create table `usuarios` (
      `idUsuario` INT PRIMARY KEY AUTO_INCREMENT,
      `nome` VARCHAR(50),
      `email` VARCHAR(30),
      `senha` VARCHAR(100),
      `funcionario` varchar(20)
      ); ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['animai'] = ('''
      create table `animais`(
      `idAnimal` INT PRIMARY KEY AUTO_INCREMENT,
      `nome` VARCHAR(20) NOT NULL,
      `tipo` VARCHAR(10) NOT NULL,
      `idade` INT NOT NULL,
      `sexo` VARCHAR(10) NOT NULL,
      `descricao` VARCHAR(200) NOT NULL,
      `dataInclusao` DATE DEFAULT (CURRENT_DATE)
      ); ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['adocoes'] = ('''
      create table `adocoes`(
      `idAdocao` INT PRIMARY KEY AUTO_INCREMENT,
      `fk_usuario` INT NOT NULL,
      `fk_animal` INT NOT NULL UNIQUE,
      FOREIGN KEY (fk_animal) REFERENCES animais(idAnimal),
      FOREIGN KEY (fk_usuario) REFERENCES usuarios(idUsuario),
      `dataAdocao` DATE DEFAULT (CURRENT_DATE),
      `statusAdocao` VARCHAR(20) DEFAULT("Pendente")
      ); ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

for tabela_nome in TABLES:
      tabela_sql = TABLES[tabela_nome]
      try:
            print('Criando tabela {}:'.format(tabela_nome), end=' ')
            cursor.execute(tabela_sql)
      except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                  print('Já existe')
            else:
                  print(err.msg)
      else:
            print('OK')

# inserindo usuarios
usuario_sql = 'INSERT INTO usuarios (nome, email, senha, funcionario) VALUES (%s, %s, %s, %s)'
usuarios = [
      ('João Silva', 'joaosilva@ong.com', '12345GNS*', 'sim'),
      ('Roberto Lima', 'robertolima@gmail.com', '12345GNS*', 'não')
]
cursor.executemany(usuario_sql, usuarios)

cursor.execute('select * from ong.usuarios')
print(' -------------  Usuários:  -------------')
for user in cursor.fetchall(): # type: ignore
    print(user[1])

# inserindo jogos
animais_sql = 'INSERT INTO animais (nome, tipo, idade, sexo, descricao) VALUES (%s, %s, %s, %s, %s)'
Animais = [
      ('Marla', 'Passaro', 9, 'Femea', 'Cachorro amigável e brincalhão'),
      ('Cleiton', 'Gato', 4, 'Macho', 'Cachorro amigável e brincalhão'),
      ('Bidu', 'Cachorro', 5, 'Macho', 'Cachorro amigável e brincalhão'),
]
cursor.executemany(animais_sql, Animais)

cursor.execute('select * from ong.animias')
print(' -------------  Animais:  -------------')
for jogo in cursor.fetchall(): # type: ignore
    print(jogo[1])

# commitando se não nada tem efeito
conn.commit()

cursor.close()
conn.close()
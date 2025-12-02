class Cliente:
    def __init__(self, email=None, nome=None,estado_civil=None, 
                 estuda=None, trabalha=None,
                 genero=None, cep=None, endereco=None, numero=None,
                 cidade=None, bairro=None, estado=None, 
                 telefone=None, celular=None):
#(email,nome,estado_civil,estuda,trabalha,genero,
#cep,endereco,numero,bairro,cidade,estado,telefone,celular
        # Atributos Privados
        # Usei nomes padronizados em snake_case (email, nome, telefone, etc.) 
        # para os atributos internos, que é a convenção Python.
        self.__email = email
        self.__nome = nome
        self.__telefone = telefone
        self.__celular = celular
        self.__genero = genero
        self.__cep = cep
        self.__endereco = endereco
        self.__estado = estado
        self.__cidade = cidade
        self.__bairro = bairro
        self.__numero = numero
        self.__estado_civil = estado_civil
        self.__estuda = estuda
        self.__trabalha = trabalha

    # --- Getters e Setters ---
    # Email
    def getEmail(self):
        return self.__email
    def setEmail(self, email):
        self.__email = email

    # Nome
    def getNome(self):
        return self.__nome
    def setNome(self, nome):
        self.__nome = nome

    # Telefone
    def getTelefone(self):
        return self.__telefone
    def setTelefone(self, telefone):
        self.__telefone = telefone

    # Celular
    def getCelular(self):
        return self.__celular
    def setCelular(self, celular):
        self.__celular = celular

    # Gênero
    def getGenero(self):
        return self.__genero
    def setGenero(self, genero):
        self.__genero = genero

    # CEP
    def getCep(self):
        return self.__cep
    def setCep(self, cep):
        self.__cep = cep

    # Endereço
    def getEndereco(self):
        return self.__endereco
    def setEndereco(self, endereco):
        self.__endereco = endereco

    # Estado
    def getEstado(self):
        return self.__estado
    def setEstado(self, estado):
        self.__estado = estado

    # Cidade
    def getCidade(self):
        return self.__cidade
    def setCidade(self, cidade):
        self.__cidade = cidade

    # Bairro
    def getBairro(self):
        return self.__bairro
    def setBairro(self, bairro):
        self.__bairro = bairro

    # Número
    def getNumero(self):
        return self.__numero
    def setNumero(self, numero):
        self.__numero = numero

    # Estado Civil (est_cv no seu código de validação)
    def getEstado_civil(self):
        return self.__estado_civil
    def setEstado_civil(self, estado_civil):
        self.__estado_civil = estado_civil

    # Estuda (estuda)
    def getEstuda(self):
        return self.__estuda
    def setEstuda(self, estuda):
        self.__estuda = estuda

    def getTrabalha(self):
        return self.__trabalha
    def setTrabalha(self, trabalha):
        self.__trabalha = trabalha

    # --- Representação de String ---
    def __str__(self):
        return (f"Informações do Cliente:\n"
                f"  Email: {self.getEmail()}\n"
                f"  Nome: {self.getNome()}\n"
                f"  Telefone: {self.getTelefone()}\n"
                f"  Celular: {self.getCelular()}\n"
                f"  Gênero: {self.getGenero()}\n"
                f"  CEP: {self.getCep()}\n"
                f"  Endereço: {self.getEndereco()}, Nº {self.getNumero()}\n"
                f"  Bairro: {self.getBairro()}\n"
                f"  Cidade/Estado: {self.getCidade()}/{self.getEstado()}\n"
                f"  Estado Civil: {self.getEstado_civil()}\n"
                f"  Estuda: {self.getEstuda()}\n"
                f"  Trabalha: {self.getTrabalha()}")
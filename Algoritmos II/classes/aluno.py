class Aluno:
  def __init__(self, nome=None, n1=None, n2=None):
    self.__nome = nome
    self.__n1 = n1
    self.__n2 = n2
  
  def getNome(self):
    return self.__nome
  def setNome(self, nome):
    self.__nome = nome
  def getN1(self):
    return self.__n1
  def setN1(self, n1):
    self.__n1 = n1
  def getN2(self):
    return self.__n2
  def setN2(self, n2):
    self.__n2 = n2

  def media(self):
    return (self.__n1+self.__n2)/2

  def __str__(self):
    return f"Nome: {self.__nome}\nNota 1: {self.__n1}\nNota 2: {self.__n2}\nMédia: {self.media()}"
  
class Turma:
  def __init__(self, codigo=None, alunos=None):
    self.codigo = codigo
    self.alunos = alunos

  def adicionarAluno(self,aluno):
    self.alunos.append(aluno.getNome())

  def __str__(self):
    return f"Turma: {self.codigo} Alunos: {self.alunos}"
# principal

afranio = Aluno("Afrânio",10,9)
print(afranio)
camila = Aluno("Camila",9,7)
print(camila)
turma301 = Turma(301,[])
turma301.adicionarAluno(afranio)
turma301.adicionarAluno(camila)
print(turma301)
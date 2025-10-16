import mysql.connector
from PyQt5 import uic, QtWidgets    # uic = Módulo pra importar interfaces em xml
from pathlib import Path

script_dir = Path(__file__).resolve().parent

banco = mysql.connector.connect(
   host = "localhost",
   user = "root",
   password = "",
   database = "crud_agenda"
)

def main():
   campoNome = telaPrincipal.campoNome.text()
   print("Nome: ", campoNome)
   campoEmail= telaPrincipal.campoEmail.text()
   print("Email: ", campoEmail)
   campoTelefone = telaPrincipal.campoTelefone.text()
   print("Telefone: ", campoTelefone)

   tipoTelefone = ""

   if telaPrincipal.rbResidencial.isChecked():
      print("Tipo de Telefone é residencial.")
      tipoTelefone = "Residencial"
   elif telaPrincipal.rbCelular.isChecked():
      print("Tipo de Telefone é celular.")
      tipoTelefone = "Celular"
   else:
      print("Informe o tipo de telefone.")
      tipoTelefone = "Não informado"

   cursor = banco.cursor()
   comando_SQL = "INSERT INTO contatos (nome, email, telefone, tipoTelefone) VALUES (%s, %s, %s, %s)"
   dados = (str(campoNome), str(campoEmail), str(campoTelefone), tipoTelefone)
   cursor.execute(comando_SQL, dados)
   banco.commit()

   telaPrincipal.campoNome.setText("")
   telaPrincipal.campoEmail.setText("")
   telaPrincipal.campoTelefone.setText("")

   print("Contato cadastrado com sucesso")

def consultarContatos():
   telaConsulta.show()
   
   cursor = banco.cursor()
   comando_SQL = "SELECT * FROM contatos"
   cursor.execute(comando_SQL)
   contatosLidos = cursor.fetchall()
   
   telaConsulta.formContatos.setRowCount(len(contatosLidos))
   telaConsulta.formContatos.setColumnCount(5)
   
   for i in range(0, len(contatosLidos)):
      for j in range(0, 5):
            telaConsulta.formContatos.setItem(i, j, QtWidgets.QTableWidgetItem(str(contatosLidos[i][j])))

# def alterarContato():
# def excluirContato():
# def gerarPDF():

def voltar():
   telaConsulta.close()
   
# Criar um app = Importar dependencias
app=QtWidgets.QApplication([])

# Objeto a ser criado = uic(módulo do PyQt5).(carregar interface)("objeto com os parametros de interface em XML")
telaPrincipal=uic.loadUi(str(script_dir) + "\\telaInicial.ui")
telaConsulta=uic.loadUi(str(script_dir) + "\\listaContatos.ui")

# NomeDoObjeto.{BuscarObjeto}.{Função}
telaPrincipal.botaoCadastrar.clicked.connect(main)
telaPrincipal.botaoConsultar.clicked.connect(consultarContatos)

# telaConsulta.botaoPDF.clicked.connect(gerarPDF)
telaConsulta.botaoVoltar.clicked.connect(voltar)

telaPrincipal.show()
app.exec()
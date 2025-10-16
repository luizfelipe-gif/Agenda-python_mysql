import mysql.connector
from PyQt5 import uic, QtWidgets    # uic = Módulo pra importar interfaces em xml

banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "crud_agenda"
)

def main():
    campoNome = agenda.campoNome.text()
    print("Nome: ", campoNome)

    campoEmail= agenda.campoEmail.text()
    print("Email: ", campoEmail)

    campoTelefone = agenda.campoTelefone.text()
    print("Telefone: ", campoTelefone)

    tipoTelefone = ""

    if agenda.rbResidencial.isChecked():
        print("Tipo de Telefone é residencial.")
        tipoTelefone = "Residencial"
    elif agenda.rbCelular.isChecked():
        print("Tipo de Telefone é celular.")
        tipoTelefone = "Celular"
    else:
        print("Informe o tipo de telefone.")
        tipoTelefone = "Não informado"

# Criar um app = Importar dependencias
app=QtWidgets.QApplication([])

# Objeto a ser criado = uic(módulo do PyQt5).(carregar interface)("objeto com os parametros de interface em XML")
agenda=uic.loadUi("1/telaInicial.ui")

# NomeDoObjeto.{BuscarObjeto}.{Função}
agenda.botaoEnviar.clicked.connect(main)

agenda.show()
app.exec()
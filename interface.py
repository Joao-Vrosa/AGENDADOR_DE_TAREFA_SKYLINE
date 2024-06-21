from tkinter import *
from tkinter.filedialog import askopenfilenames
from tkinter import messagebox
import logging

# Configuração básica de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class Interface:
    def __init__(self, master=None):
        self.dados = {}  # Armazenar dados inseridos
        self.caminho_do_arquivo = ""  # Caminho do arquivo executavel Skyline
        self.fonte_padrao = ('Arial', 10,)  # Fonte padrão da aplicação
        
        # Armazenando o valor do Radiobutton
        self.radio_value = IntVar()
        self.radio_value.set(0)  # Valor padrão
        
        # ##### CONTAINERS ##### #
        self.containerPai = Frame(master)  # Conteiner pai
        self.containerPai["pady"] = 10
        self.containerPai.pack()
        
        self.container2 = Frame(master)
        self.container2['padx'] = 20
        self.container2.pack()
        
        self.container3 = Frame(master)
        self.container3['padx'] = 20
        self.container3.pack()
        
        self.container4 = Frame(master)
        self.container4['padx'] = 20
        self.container4.pack()
        
        self.container5 = Frame(master)
        self.container5['padx'] = 20
        self.container5.pack()
        
        self.container6 = Frame(master)
        self.container6['pady'] = 20
        self.container6.pack()
        
        self.container7 = Frame(master)
        self.container7['pady'] = 20
        self.container7.pack()

        self.container8 = Frame(master)
        self.container8['pady'] = 20
        self.container8.pack()
        
        # ##### ELEMENTOS DA JANELA ##### #
        
        # LABEL - Titulo da tarefa
        self.titulo_tarefa_label = Label(self.container2, text='Titulo da Tarefa', font=self.fonte_padrao, width=20)
        self.titulo_tarefa_label.pack(side=LEFT)
        # INPUT - Titulo da tarefa
        self.titulo_tarefa = Entry(self.container2)
        self.titulo_tarefa['width'] = 30
        self.titulo_tarefa['font'] = self.fonte_padrao
        self.titulo_tarefa.pack(side=RIGHT)
        
        # LABEL - Tempo (minutos)
        self.tempo_label = Label(self.container3, text='Tempo (minutos)', font=self.fonte_padrao, width=20)
        self.tempo_label.pack(side=LEFT)
        # INPUT - Tempo (minutos)
        self.tempo = Entry(self.container3)
        self.tempo['width'] = 30
        self.tempo['font'] = self.fonte_padrao
        self.tempo.pack(side=RIGHT)
        
        # LABEL - Senha Skyline
        self.senha_label = Label(self.container4, text='Senha Skyline', font=self.fonte_padrao, width=20)
        self.senha_label.pack(side=LEFT)
        # INPUT - Senha Skyline
        self.senha = Entry(self.container4)
        self.senha['width'] = 30
        self.senha['font'] = self.fonte_padrao
        self.senha['show'] = '*'
        self.senha.pack(side=RIGHT)
        
        # LABEL - Caminho do Executavel
        self.caminho_executavel_label = Label(self.container5, text='Caminho do Executavel', font=self.fonte_padrao, width=20)
        self.caminho_executavel_label.pack(side=LEFT)
        # INPUT - Caminho do Executavel
        self.caminho_executavel = Button(self.container5, background="light green")
        self.caminho_executavel['text'] = 'Selecionar .EXE'
        self.caminho_executavel['width'] = 12
        self.caminho_executavel['font'] = self.fonte_padrao
        self.caminho_executavel['command'] = self.buscar_caminho_arquivo
        self.caminho_executavel.pack()
        
        # Titulo
        self.titulo = Label(self.containerPai, text='Menu de Configuração')
        self.titulo['font'] = ("Arial", 10, "bold")
        self.titulo.pack(side=TOP)
        
        # LABEL - Usuário ADM ou PADRÂO
        self.label_sistema = Label(self.container6, text='Permissão do seu usuário', font=self.fonte_padrao, width=20)
        self.label_sistema.pack(side=TOP)
        # RADIOBUTTON 1 - Usuário ADM ou PADRÂO
        self.sistema_adm = Radiobutton(self.container6, text='Administrador', value=1, indicator=0, variable= self.radio_value, command=self.tipo_de_permicao, background="light green")
        self.sistema_adm['font'] = self.fonte_padrao
        self.sistema_adm['width'] = 12
        self.sistema_adm.pack(side=TOP)
        # RADIOBUTTON 2 - Usuário ADM ou PADRÂO
        self.sistema = Radiobutton(self.container6, text='Padão', value=2, indicator=0, variable= self.radio_value, command=self.tipo_de_permicao, background="light green")
        self.sistema['font'] = self.fonte_padrao
        self.sistema['width'] = 12
        self.sistema.pack(side=TOP)
        
        # Botão Sair
        self.sair = Button(self.container8, background="light green")
        self.sair['text'] = 'Sair'
        self.sair['font'] = self.fonte_padrao
        self.sair['width'] = 12
        self.sair['command'] = self.containerPai.quit
        self.sair.pack(side=LEFT)
        
        # Botão Criar Tarefa
        self.criar_tarefa = Button(self.container8, background="light green")
        self.criar_tarefa['text'] = 'Criar Tarefa'
        self.criar_tarefa['font'] = self.fonte_padrao
        self.criar_tarefa['width'] = 12
        self.criar_tarefa['command'] = self.criar_script_tarefa
        self.criar_tarefa.pack(side=RIGHT)
        
        # LABEL - Output
        self.output_label = Label(self.container7, text='SCRIPT', font=self.fonte_padrao, width=20)
        self.output_label.pack(side=TOP)
        # OUTPUT
        self.output = Text(self.container7)
        self.output['font'] = self.fonte_padrao
        self.output['width'] = 50
        self.output['height'] = 5
        self.output.pack(side=TOP)
        
        
    def buscar_caminho_arquivo(self):
        caminho_arquivo = askopenfilenames(
            title='Selcionar arquivo Skyline.exe',
            filetypes=[("Executable files", "*.exe")],
            defaultextension=".exe"
        )
        
        if caminho_arquivo:
            logging.info(f'Caminho do arquivo Skyline: {caminho_arquivo[0]}')
            self.caminho_do_arquivo = caminho_arquivo[0]
        else:
            logging.warning('Nenhum arquivo foi selecionado!')
            self.caminho_do_arquivo = ''
        
        
    def validar_campos(self):
        if not self.titulo_tarefa.get():
            messagebox.showerror("ERRO", "O campo 'Titulo da Tarefa' deve ser preenchido!")
            return False
        
        if not self.tempo.get():
            messagebox.showerror("ERRO", "O campo 'Tempo (minutos)' deve ser preenchido!")
            return False
        
        if not self.senha.get():
            messagebox.showerror("ERRO", "O campo 'Senha Skyline' deve ser preenchido!")
            return False
        
        if not self.caminho_do_arquivo:
            messagebox.showerror("ERRO", "O caminho do executável deve ser selecionado!")
            return False
        
        if not self.radio_value.get():
            messagebox.showerror("ERRO", "O tipo de permissão deve ser selecionado!")
            return False
        
        return True
    

    def criar_script_tarefa(self):
        logging.info('Iniciando processo de criação de Script para tarefa...')
        if self.validar_campos():
            self.dados = {
                'titulo': self.titulo_tarefa.get(),
                'tempo': self.tempo.get(),
                'senha': self.senha.get(),
                'caminho': self.caminho_do_arquivo,
            }
            
            if self.radio_value.get() == 1:
                script = f'SCHTASKS /CREATE /TN {self.dados["titulo"]} /TR "{self.dados["caminho"]} /SE={self.dados["senha"]}" /SC DAILY /ST 07:00 /RI {self.dados["tempo"]} /DU 24:00 /F /RU "SYSTEM" /RL HIGHEST'
            else:
                script = f'SCHTASKS /CREATE /TN {self.dados["titulo"]} /TR "{self.dados["caminho"]} /SE={self.dados["senha"]}" /SC DAILY /ST 07:00 /RI {self.dados["tempo"]} /DU 24:00 /F'
            
            logging.info(f'SCRIPT: {script}')
            self.output.insert(END, script)
        else:
            logging.warning('Erro ao criar a tarefa: Todos os campos devem ser preenchidos!')


root = Tk()  # Permite que os widgets possam ser utilizados na aplicação.
root.title('Agendador Skyline')
Interface(root)
root.mainloop()  # Para exibirmos a tela. Sem o event loop, a interface não será exibida.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import random

class UserLoginTests(StaticLiveServerTestCase):

    # Função para configurar o WebDriver
    def setup_driver(self):
        driver = webdriver.Chrome()  # ou o WebDriver adequado, como Firefox ou Edge
        driver.get("http://localhost:8000/polls/")  # Usando a URL do servidor ao vivo do Django
        driver.maximize_window()  # Maximiza a janela do navegador
        return driver

    # Função para login de um utilizador
    def login(self, driver, username, password):
        driver.find_element(By.ID, 'id_username').send_keys(username)  # Preenche o campo de nome de utilizador
        driver.find_element(By.ID, 'id_password').send_keys(password)  # Preenche o campo de senha
        driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()  # Clica no botão de login

    # Função para aguardar que um elemento esteja presente na página
    def wait_for_element(self, driver, by, value, timeout=10):
        """Função para esperar até que um elemento esteja presente e visível"""
        return WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )

    # Teste TU01: Criação de Tópico com Dados Válidos
    def test_criacao_topico_valido(self):
        driver = self.setup_driver()
        self.login(driver, 'novo', 'olaola#00')
        
        # Criação de um novo tópico
        driver.find_element(By.LINK_TEXT, 'Create Topic').click()  # Acessa a página de criação de tópico
        driver.find_element(By.ID, 'id_title').send_keys('Tópico 1')  # Preenche o título do tópico
        driver.find_element(By.ID, 'id_description').send_keys('Descrição válida')  # Preenche a descrição do tópico
        driver.find_element(By.CSS_SELECTOR, 'button[type="submit"].btn.btn-primary').click()  # Submete o formulário
        
        # Verifica se o tópico foi criado com sucesso
        self.assertIn("Tópico 1", driver.page_source)
        
        driver.quit()

    # Teste TU02: Rejeição de título vazio
    def test_titulo_vazio(self):
        driver = self.setup_driver()
        self.login(driver, 'novo', 'olaola#00')

        # Acessa a página para criar um tópico
        driver.find_element(By.LINK_TEXT, 'Create Topic').click()

        # Deixa o campo de título vazio e preenche a descrição
        driver.find_element(By.ID, 'id_title').send_keys('')  # Deixa o título vazio
        driver.find_element(By.ID, 'id_description').send_keys('Descrição válida')
        driver.find_element(By.CSS_SELECTOR, 'button[type="submit"].btn.btn-primary').click()

        # Verifica se o pop-up com o erro é visível
        error_tooltip = driver.find_element(By.CSS_SELECTOR, 'input#id_title:invalid')  # Verifica se o campo está em estado inválido

        # Verifica se o pop-up está visível
        self.assertTrue(error_tooltip.is_displayed(), "O erro de 'Por favor preencha este campo' não foi exibido.")

        driver.quit()

    # Teste TU03: Validação de autenticação com dados corretos
    def test_login_valid(self):
        driver = self.setup_driver()
        self.login(driver, 'novo', 'olaola#00')
        
        # Verifica se o login foi bem-sucedido
        self.assertIn('Discussion Forum', driver.title)
        
        driver.quit()

    # Teste TU04: Validação de rejeição de autenticação com dados incorretos
    def test_login_invalid(self):
        driver = self.setup_driver()
        driver.get('http://localhost:8000/polls/login/')
        
        username_input = self.wait_for_element(driver, By.NAME, 'username')
        password_input = self.wait_for_element(driver, By.NAME, 'password')
        
        username_input.send_keys('invaliduser')  # Envia um nome de utilizador inválido
        password_input.send_keys('wrongpassword')  # Envia uma senha inválida
        password_input.send_keys(Keys.RETURN)  # Submete o formulário
        
        # Verifica se a mensagem de erro é exibida
        error_message = self.wait_for_element(driver, By.CLASS_NAME, 'alert-danger')
        self.assertTrue(error_message.is_displayed())
        
        driver.quit()

    # Teste TF01: Registo de Novo Utilizador
    def test_registo_usuario(self):
        driver = self.setup_driver()
        driver.find_element(By.LINK_TEXT, 'Registe-se').click()

        # Geração do nome de usuário e e-mail com números aleatórios
        username = str(random.randint(10000, 99999))  # Gera um nome de utilizador aleatório
        email = username + '@exemplo.com'  # Gera um e-mail único baseado no nome de utilizador

        # Preenche os campos do registo
        driver.find_element(By.ID, 'id_username').send_keys(username)
        driver.find_element(By.ID, 'id_email').send_keys(email)
        driver.find_element(By.ID, 'id_password1').send_keys('senha_secreta')
        driver.find_element(By.ID, 'id_password2').send_keys('senha_secreta')
        driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

        # Verifica se o utilizador foi redirecionado para a página de login
        self.assertIn("/login", driver.current_url)

        driver.quit()

    # Teste TI01: Redirecionamento ao Tentar Criar Tópico sem Login
    def test_redirecionamento_para_login(self):
        driver = self.setup_driver()
        
        driver.get('http://localhost:8000/polls/create/')
        
        # Verifica se há um redirecionamento para a página de login
        self.assertIn("/login", driver.current_url)
        
        driver.quit()

    # Teste TI02: Verificação da Ligação Correta Entre Tópicos e Comentários
    def test_verificacao_ligacao_topicos_comentarios(self):
        driver = self.setup_driver()
        self.login(driver, 'novo', 'olaola#00')

        # Criação de tópico
        driver.find_element(By.LINK_TEXT, 'Create Topic').click()
        driver.find_element(By.ID, 'id_title').send_keys('Tópico com Comentário')
        driver.find_element(By.ID, 'id_description').send_keys('Descrição do Tópico')
        driver.find_element(By.CSS_SELECTOR, 'button[type="submit"].btn.btn-primary').click()
        
        driver.get('http://localhost:8000/polls/')

        # Clicar no botão "View Details" do primeiro tópico       
        driver.find_element(By.CSS_SELECTOR, "a.btn.btn-info").click()
        
        # Comentar no tópico
        driver.find_element(By.ID, 'id_text').send_keys('Comentário de Teste')      
        driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary').click()

        # Verifica se o comentário está associado corretamente ao tópico
        self.assertIn("Comentário de Teste", driver.page_source)

        driver.quit()

    # Teste TI03: Exclusão de Comentário por Outro Utilizador
    def test_exclusao_comentario_outro_usuario(self):
        driver = self.setup_driver()
        self.login(driver, 'novo', 'olaola#00')
        
        # Clicar no botão "View Details" do primeiro tópico
        driver.find_element(By.CSS_SELECTOR, "a.btn.btn-info").click()

        # Verificar se o botão de exclusão está visível ou presente
        try:
            excluir_buttons = driver.find_elements(By.CSS_SELECTOR, 'button[type="submit"].btn.btn-danger.mt-2')
            
            if len(excluir_buttons) > 0:  # Se o botão de exclusão estiver presente
                excluir_buttons[0].click()

                # Verifica se o erro de acesso negado foi exibido
                self.assertIn("Apenas o autor pode excluir comentários", driver.page_source)
            else:
                print("O botão de exclusão não está disponível para este comentário.")

        except Exception as e:
            print(f"Erro ao tentar verificar/excluir comentário: {str(e)}")
        
        driver.quit()

    # Teste TF02: Edição de Comentário por outro autor
    def test_exclusao_topico_autor(self):
        driver = self.setup_driver()
        self.login(driver, 'novo', 'olaola#00')
        
        # Criação de tópico
        driver.find_element(By.LINK_TEXT, 'Create Topic').click()
        driver.find_element(By.ID, 'id_title').send_keys('Tópico com Comentário')
        driver.find_element(By.ID, 'id_description').send_keys('Descrição do Tópico')
        driver.find_element(By.CSS_SELECTOR, 'button[type="submit"].btn.btn-primary').click()
        
        # Clicar no botão "View Details" do primeiro tópico
        driver.find_element(By.CSS_SELECTOR, "a.btn.btn-info").click()

        # Encontrar e clicar no botão de exclusão de tópico
        excluir_buttons = driver.find_elements(By.CSS_SELECTOR, "a.btn.btn-danger.mt-2")

        if len(excluir_buttons) > 0:  # Se o botão de exclusão estiver presente
            excluir_buttons[0].click()
        
            # Verifica se foi para a página inicial
            self.assertIn("/polls", driver.current_url)
        else:
            print("O botão de exclusão não está disponível para este tópico.")

        driver.quit()

    # Teste TF03: Edição de Comentário pelo Autor
    def test_edicao_comentario_autor(self):
        driver = self.setup_driver()
        self.login(driver, 'novo', 'olaola#00')
        
        # Criação de tópico
        driver.find_element(By.LINK_TEXT, 'Create Topic').click()
        driver.find_element(By.ID, 'id_title').send_keys('Tópico com Comentário')
        driver.find_element(By.ID, 'id_description').send_keys('Descrição do Tópico')
        driver.find_element(By.CSS_SELECTOR, 'button[type="submit"].btn.btn-primary').click()

        # Clicar no botão "View Details" do primeiro tópico
        driver.find_element(By.CSS_SELECTOR, "a.btn.btn-info").click()
        
        # Comentar no tópico
        driver.find_element(By.ID, 'id_text').send_keys('Comentário de Teste')
        driver.find_element(By.CSS_SELECTOR, 'button[type="submit"].btn.btn-primary').click()
        
        # Editar comentário
        driver.find_element(By.CSS_SELECTOR, 'a.btn.btn-warning.mt-2').click()
        driver.find_element(By.ID, 'id_title').clear()  # Limpa o campo de texto
        driver.find_element(By.ID, 'id_title').send_keys("Comentário Editado")
        driver.find_element(By.CSS_SELECTOR, 'button[type="submit"].btn.btn-primary').click()

        # Verifica se o comentário foi editado corretamente
        self.assertIn("Comentário Editado", driver.page_source)

        driver.quit()

    # TR02 - Verificação de persistência de sessão após alterações no sistema
    def test_regressao_persistencia_sessao(self):
        driver = self.setup_driver()

        # Passo 1: Login
        self.login(driver, 'novo', 'olaola#00')

        # Verifica se o login foi bem-sucedido
        self.assertIn('Discussion Forum', driver.title)

        # Passo 2: Criar Tópico
        driver.find_element(By.LINK_TEXT, 'Create Topic').click()  # Acessa a página de criação de tópico
        driver.find_element(By.ID, 'id_title').send_keys('Tópico Persistência de Sessão')  # Preenche o título do tópico
        driver.find_element(By.ID, 'id_description').send_keys('Teste para verificar persistência de sessão.')  # Preenche a descrição do tópico
        driver.find_element(By.CSS_SELECTOR, 'button[type="submit"].btn.btn-primary').click()  # Submete o formulário para criar o tópico
        
        # Verifica que o tópico foi criado com sucesso
        self.assertIn("Tópico Persistência de Sessão", driver.page_source)

        # Passo 3: Adicionar Comentário ao Tópico
        driver.find_element(By.CSS_SELECTOR, "a.btn.btn-info").click()  # Clica no link para visualizar o tópico
        driver.find_element(By.ID, 'id_text').send_keys('Comentário de Teste')  # Escreve um comentário
        driver.find_element(By.CSS_SELECTOR, 'button[type="submit"].btn.btn-primary').click()  # Submete o comentário
        
        # Verifica que o comentário foi adicionado ao tópico
        self.assertIn("Comentário de Teste", driver.page_source)

        # Abre uma nova aba e fecha a aba atual para simular a troca de contexto
        driver.execute_script("window.open('');")  # Abre uma nova aba
        driver.switch_to.window(driver.window_handles[1])  # Muda para a nova aba
        driver.switch_to.window(driver.window_handles[0])  # Retorna para a aba principal

        # Navega para o site novamente
        driver.get("http://127.0.0.1:8000/polls/")

        # Atualiza a página para aplicar os cookies e restaurar a sessão do utilizador
        driver.refresh()

        # Verifica que a sessão foi restaurada após a atualização da página
        self.assertIn('Discussion Forum', driver.title)

        # Passo 6: Logout Explícito
        driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()  # Clica no botão de logout

        # Verifica que a sessão foi encerrada com sucesso
        self.assertIn('Login - Discussion Forum', driver.title)  # Verifica se está na página de login
        self.assertIn("/login", driver.current_url)  # Verifica a URL de login

        # Passo 7: Verificar que a sessão não persiste após logout
        driver.quit()  # Fecha o driver atual
        driver = self.setup_driver()  # Reabre o driver novamente

        # Navega novamente para o site
        driver.get("http://127.0.0.1:8000/polls/")
        
        # Verifica se a página de login é carregada, o que indica que a sessão não foi restaurada
        self.assertIn('Login - Discussion Forum', driver.title)

        driver.quit()  # Fecha o driver ao fim do teste
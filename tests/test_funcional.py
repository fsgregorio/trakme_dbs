from selenium import webdriver
from time import sleep
import pytest
import subprocess
from selenium.webdriver.common.by import By
import os
#from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager  # Gerenciando o ChromeDriver automaticamente


@pytest.fixture
def driver():
    # Iniciar Streamlit em background
    process = subprocess.Popen(["streamlit", "run", "src/app.py"])
    options = Options()
    options.headless = True # Executar em modo headless
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    # Iniciar o WebDriver usando GeckoDriver
    driver.set_page_load_timeout(5)
    yield driver

    # Fechar o WebDriver e o Streamlit após o test
    driver.quit()
    process.kill()

def test_app_opens(driver):
    # Verificar se a página abre
    driver.get("http://localhost:8501")
    sleep(2)

# def test_check_title_is(driver):
#     # Verificar se a página abre
#     driver.get("http://localhost:8501")
#     sleep(2)
#     # Capturar o título da página
#     page_title = driver.title

#     # Verificar se o título da página é o esperado
#     expected_title = "Validador de schema excel" # Substitua com o título real esperado
#     assert page_title == expected_title

# def test_check_streamlit_h1(driver):
#     # Acessar a página do Streamlit
#     driver.get("http://localhost:8501")

#     # Aguardar para garantir que a página foi carregada
#     sleep(2) # Espera 5 segundos

#     # Capturar o primeiro elemento <h1> da página
#     h1_element = driver.find_element(By.TAG_NAME, "h1")

#     # Verificar se o texto do elemento <h1> é o esperado
#     expected_text = "Insira o seu excel para validação"
#     assert h1_element.text == expected_text

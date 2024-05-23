<p align="center">
<img loading="lazy" src="https://github.com/Dev-JoaoM/Janos-Park-Project/blob/master/_referencia/img/Logo%20editado.png"/>
</p>

<p align="center">
<img loading="lazy" src="http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=yellow&style=for-the-badge"/>
</p>


## Ferramentas utilizadas

[![Git](https://img.shields.io/badge/Git-E44C30?style=for-the-badge&logo=git&logoColor=fff)](https://git-scm.com/doc) 
[![GitHub](https://img.shields.io/badge/GitHub-000?style=for-the-badge&logo=github&logoColor=fff)](https://docs.github.com/pt)
![Windows](https://img.shields.io/badge/Windows-000?style=for-the-badge&logo=windows&logoColor=2CA5E0)
[![Pycharm](https://img.shields.io/badge/PyCharm-gray.svg?&style=for-the-badge&logo=PyCharm&logoColor=green)](https://www.jetbrains.com/pt-br/pycharm/)
![SQLite](https://img.shields.io/badge/SQLite-fff?style=for-the-badge&logo=sqlite&logoColor=07405E)

![Python Version](https://img.shields.io/badge/Python-v3.11.5-blue?logo=python)
![Pip Version](https://img.shields.io/badge/Pip_Install-v23.2.1-yellow?)
![Django Version](https://img.shields.io/badge/Django-v5.0.6-green?logo=django&logoColor=green)
![Bootstrap Version](https://img.shields.io/badge/Bootstrap_5-v2.1-purple?logo=bootstrap&logoColor=purple)



## 📢 Sobre o [Projeto](https://github.com/Dev-JoaoM/Janos-Park-Project/blob/master/_referencia/Sobre%20o%20Projeto.md)

## 📝 Anotações do [Projeto](https://github.com/Dev-JoaoM/Janos-Park-Project/blob/master/_referencia/janos_notes.md)

## 📜 Versionamento de código com [Git e GitHub](https://github.com/Dev-JoaoM/Versionamento-com-Git-e-GitHub/tree/master)

##  💻Instalação do Projeto (Windows)

#### 1. Clone o repositório
   ```
    git clone https://github.com/Dev-JoaoM/Janos-Park-Project.git
   ```

#### 2. Abra essa pasta no Pycharm 

#### 3. Abra o terminal e crie o Ambiente virtual
   ```
    py -m venv .venv
   ```

##### 3.1 Se não deixar criar o ambiente virtual, abra o cmd do windows como admin e execute
   ```
   Set-ExecutionPolicy Unrestricted
   ```
**Obs:** Tente criar o ambiente virtual novamente.

#### 4. Ative o ambiente virtual
   ```	
   .venv\Scripts\Activate
   ```

#### 5. Instale os requerimentos (Bibliotecas usadas)
```
pip install -r requirements.txt
```

#### 6. Execute as migrações (Criação do arquivo do BD)
  ```
  python manage.py migrate
  ```

#### 7. Inicie o servidor
  ```
  python manage.py runserver
  ```

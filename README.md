# Projeto Janos Park

### 📢 Sobre o [Projeto](https://github.com/Dev-JoaoM/Janos-Park-Project/blob/master/_referencia/Sobre%20o%20Projeto.md)

### 📝 Anotações do [Projeto](https://github.com/Dev-JoaoM/Janos-Park-Project/blob/master/_referencia/janos_notes.md)

###  💻Instalação do Projeto (Windows)

#### Crie um Projeto no Pycharm com as opções da imagem
![Projeto Pycharm](https://github.com/Dev-JoaoM/Janos-Park-Project/blob/master/_referencia/Criando%20um%20projeto%20no%20Pycharm.png)


### Se não deixar criar o ambiente virtual, abra o cmd como admin e execute
```
Set-ExecutionPolicy Unrestricted
```
### Tente criar o Projeto novamente

### Se não estiver ativado, ative o ambiente virtual
```	
.venv\Scripts\Activate
```	

#### Dentro da pasta do projeto clone este repositório

  ```
  git clone https://github.com/Dev-JoaoM/Janos-Park-Project.git
  ```

#### Instale os requerimentos (Bibliotecas usadas)
```
pip install -r requirements.txt
```

#### Execute as migrações (Criação do arquivo do BD)
  ```
  python manage.py migrate
  ```

#### Inicie o servidor
  ```
  python manage.py runserver
  ```	
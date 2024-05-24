## Comandos úteis no projeto

model --> views --> url --> template.html

- Instalar todas as bibliotecas usadas
    ```
    pip install -r requirements.txt
    ```
- Exporta todas bibliotecas instaladas e suas respectivas versões
    ``` 
    pip freeze > requirements.txt 
    ```
- Criar um projeto
    ```
    django-admin startproject "nome do projeto"
    ```
    **Obs:** É interessante criar uma pasta com o nome do projeto e dentro dela executar esse comando com o nome de  **``` setup .```** 
    **Ex:**
    ```
    django-admin startproject setup .
    ```
- Criar um app dentro da pasta do projeto
    ```
    django-admin start app "nome do app"
    ```
- Executa o projeto
    ```
    python manage.py runserver
    ```
- Faz os comandos SQL do BD
    ```
    python manage.py makemigrations
    ```
- Cria o arquivo do BD
    ```
    python manage.py migrate
    ```


## Extenções do VS Code


- Django by Baptiste Darthenay (Para adicionar sintaxe nos templates do django)
- SQLite Viewer
- MySQL by Weijan Chen


## Bibliotecas Recomendadas

- Para tirar do código as informações importantes e chaves de acesso do projeto
    ```
    pip install python-decouple
    ```
- Para converter o formato de string de conexão que os bd usam para um padrão que o django utiliza
    ```
    pip install dj-database-url
    ```
- Para corrigir intentações e espaços a mais no código
    ```
    pip install black
    ```
	**Para executar no terminal**
	``` 
    black . 
    ```
- Removendo [Pacotes](https://horadecodar.com.br/como-remover-pacotes-instalados-em-python/)
    ```
    pip uninstall package
    ```

- Biblioteca para estilização dos templates
    - Precisa ser adiciona como um app no arquivo **setup/settings.py**

    ```
    pip install crispy-bootstrap5
    ```


### LINKS ADICIONAIS

- Códigos de páginas [HTML do Bootstrap5](https://getbootstrap.com/docs/5.3/content/tables/#overview)

- Curso [TreinaWeb](https://www.treinaweb.com.br)
    - Valor de [12x de 75,00](https://www.treinaweb.com.br/checkout/pagamento/plano/anual?forma=cartao)

*Não é propaganda*
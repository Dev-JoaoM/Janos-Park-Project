## 📢 Requisitos


### 🚨 Back-end (João)
- [ ]  Login e autenticação dos usuários (João)
      - [ ] CRUD de morador feito pelos ADM
      - [ ] CRUD de apartamento feito pelos ADM
      - [ ] CRUD de porteiro feito pelos ADM
      - [ ] CRUD de visita feito pelos porteiros
      - [X] Validação de senha
      - [ ] Geração de senha provisória
        - [ ] Alerta para alterar a senha provisória

- [X]  Registro de entrada e saida de morador (João)
      - [X] Entrada
        - [X] Saída
        - [X] video de tarefas
        - [ ] Inserir o funcionário de acordo com o login

- [ ]  Registro de entrada e saida de visitante (João)
      - [X] Entrada
      - [X] Saída
      - [X] Alterar a data limite de saida (3 dias)
      - [X] Não permitir a entrada sem autorização do morador
      - [ ] Inserir o funcionário de acordo com o login
      - [ ] Quando inserir o visitante retornar o carro dele se estiver de carro
        - [ ] Não é obrigatório o visitante entrar de carro


### BD (Larissa e João)
- [ ]  Models --> MER
- [ ]  Funções de registro
- [ ]  Não deletar os usuários, moradores, visitantes e registro
   - [ ] Desativa-los e armazenar os registros em algum lugar


#### Tarefas segundárias
  - [ ] Diferenciar se está a pé ou em um veículo



- [X]  CRUD de funcionários
- [X]  CRUD de apartamentos
- [X]  CRUD de moradores 
- [X]  CRUD de visitantes
- [X]  CRUD de Carro
   - [X] Diferenciar carro de morador e de visitante
- [X]  CRUD de Moto
- [X]  Acompanhamento pela placa do veículo e documento do visitante;
- [X]  Registrar a entrada do visitante com um morador

### Front-end  (Tiago, Vitor e Pedro)
   - [ ]  Arrumar os campos dos forms em todos os CRUDs 
   - [X]  Tela de admin do veículo para terminar.
   - [ ]  Consulta da situação do estacionamento de visitantes
   - [ ]  Tela Alerta de visita (com carro) com 3 dias de estadia (portaria)
   - [ ]  Tela de Alerta de visita (com carro) com mais de 4 dias de estadia (administração)
   - [ ]  Mostrar o nome dos usuários quando estivem logados
   - [ ]  Arrumar os links do Header de acordo com o usuário
   - [X]  Home Síndico
      - [ ] Arrumar

#### Tarefas segundárias
   - [ ]  Arrumar os campos dos forms em todos os CRUDs 
   - [ ]  Campos de pesquisa dinâmico
        - [ ]  Quando digitar a placa retornar os dados do visitante ou morador
        - [ ]  Quando digitar o nome do morador retornar seus dados
        - [ ]  Demais lugares necessários
   

   - [X]  Tela de login
   - [X]  Redefinição de senha
   - [X]  Home Portaria
   - [X]  Home Adm
   


<details>

<summary> Outros Requistos: </summary>

- Nobreak para os computadores
  
- Requisitos funcionais e não funcionais: o que são, [diferenças e eXemplos](https://querobolsa.com.br/revista/requisitos-funcionais-e-nao-funcionais)

- Requisitos Funcionais e Requisitos Não Funcionais do [Surpreendente ChatGPT](https://giganteconsultoria.com.br/2023/04/09/requisitos-funcionais-e-requisitos-nao-funcionais-do-surpreendente-chatgpt/)


 Requisitos de Produto Final (não oficial)

- Tempo de consulta de cadastro menor ou igual a 10 segundos
- Segurança logout do sistema a cada saída, troca de plantão (a cada 12h), troca de funcionário
- Dificuldade de uso do sistema: nível médio
- Limite de 3 tentativas para inserção da senha

</details>

## 📝 IDLE Pycharm

- PYCHARM – Como instalar e [configurar](https://www.hashtagtreinamentos.com/pycharm-python?gad_source=1&gclid=CjwKCAjw5v2wBhBrEiwAXDDoJfM3oHcCfQ7RzryHcNdJ0cbHfaMopiIaosGDTPNCWg8fv_nKHlYiPBoCSdwQAvD_BwE)
- Instalando Pacote com [Pip install](https://www.treinaweb.com.br/blog/como-instalar-um-pacote-com-pip-e-utiliza-lo-em-seu-projeto)
-  Criando um Ambiente virtual no [Pycharm](https://www.youtube.com/watch?v=n_yRhe37Yt4)

## 📒 Como funciona o Django
### Padrão da arquitetura MVT (Model View Template)

- Model: modelo e estrutura do BD
- View (back): Lógica da aplicação, como as coisas vão funcionar
- Template (Front): Telas da aplicação, arquivos html/css/javascript

### Documentação
- Framework Utilizado [Django](https://www.djangoproject.com)
- Instruções para configuração do [ambiente de desenvolvimento](https://github.com/treinaweb/treinaweb-youtube-introducao-ao-django/tree/main)


## 🎞️ Cursos Curtos

- [X] TreinaWeb: Iniciando com [Django Framework](https://www.youtube.com/watch?v=rwSHQqQWGnI&list=PLZ5WLsqE1WPGPA0Z0H1XB8P6UwgTHOSaf)

- [X] Dev Aprender: Sistema de Cadastro [Django](https://www.youtube.com/watch?v=-m5ywU8SW9E)

- Hashtag: Criação de sites com [Django](https://pages.hashtagtreinamentos.com/serie-criacaosites-django-python?blog=1n4033rer&video=3dep762tr)

- Jefferson Lobato: Curso de [Django](https://www.youtube.com/watch?v=ZNFVFTqaL60&list=PLLVddSbilcumgeyk0z6ko5U_FYPfbRO2C)

- Pythonando: Guia inicial completo de [Python e Django](https://www.youtube.com/watch?v=YW113aC8TII)

- Pythonando: Curso INTRODUTÓRIO COMPLETO de DJANGO I Live de Aquecimento [#04 - PYSTACK WEEK 10.0](https://www.youtube.com/watch?v=w5So_Ih7r9M&list=TLPQMjEwNDIwMjSAOgkjVR5oOQ&indeX=5)

- Pythonando: Curso INTRODUTÓRIO COMPLETO [de Python](https://www.youtube.com/watch?v=y8l_fbmJbqY&list=TLPQMjEwNDIwMjSAOgkjVR5oOQ&indeX=6&pp=gAQBiAQB)
	
- Pythonando: Aplicação de uma [oficina Django](https://www.youtube.com/watch?v=pNlHlhWDpV0&list=TLPQMjEwNDIwMjSAOgkjVR5oOQ&indeX=7&pp=gAQBiAQB)

- Pythonando: Personalizando as [migrações](https://www.youtube.com/watch?v=reAwhiFo4XM)


## 🔍 Referências

- Como é a estrutura de pastas de um projeto [Django](https://www.youtube.com/watch?v=PHZjZODh9gU)

- Como Sair do Zero em Django no Python [Passo a Passo Primeiro Site](https://www.youtube.com/watch?v=DNGI5aD9MJs)

- Minicurso [Python](https://pages.hashtagtreinamentos.com/minicurso-python-automacao-obrigado?blog=1n4033rer&video=3dep762tr)

-------------------------------------
- Flask ou Django no Python - [Qual o Melhor e Quando Usar?](https://www.youtube.com/watch?v=Bf12XA4PP_k)

- Primeira webpage usando [Django](https://www.youtube.com/watch?v=ao8pCrRqKOs)

- O que é Django - Desenvolvimento [Web em Python](https://www.youtube.com/watch?v=1SgIkOczqFY&list=TLPQMTcwNDIwMjS4sHECBwSLVA&indeX=2)

- Estrutura Básica de um [Projeto em Django](https://www.youtube.com/watch?v=-nTJz0dA7As)

- Sua aplicação Django [no ar](https://www.youtube.com/watch?v=ZBstiRvHX7w)

Esta API simula o funcionamento de um caixa eletrônico. Ela recebe um valor de saque desejado e retorna a quantidade de cédulas de cada valor necessárias para compor esse saque, utilizando a menor quantidade de cédulas possível. As cédulas consideradas são: 100, 50, 20, 10, 5 e 2.

FERRAMENTAS NECESSÁRIAS

Foi desenvolvido utilizando as lingugane typescript, python, html juntamente com css através do framework Visual studio. Para a execução do mesmo é necessário a instalação das seguintes linguagens na máquina local:
  .TYPESCRIPT
  Abra o terminal do Visual Studio e cole a seguitne mensagem: 'npm install -g typescript' em seguida inicialize o mesmo digitando 'tsc --init'
  .PYTHON
  Faça o download na página  python.org e instala em sua máquina.
  Será necessário uma ferramenta chamada flask que é basicamente um miniframework para desenvolviemnto web em Python, que será necessário para criar um servidor na máquina local para que possamos fazer as requisições de API. E para instalar basta abrir o terminal no Visual studio e digitar 'pip install Flask', em seguida instale o CORS digitando 'pip install flask-cors' isso permitirá que seja possível realizar a requisição da API de diferentes rotas caso necessário.
  
EXECUÇÃO E TESTES DO PROJETO 

  O projeto foi desenvolvido utilizando typescript(front-end) para a interação com a interface e python(back-end) para manipulção dos dados, e para alteração no código de typescript é necessário executar o comando 'tsc atm-root/script.ts' para que o mesmo possa ser compilado em javascript e o navegador possa reconhecer e interpretar o mesmo como na imagem abaixo: 
  
  ![image](https://github.com/lucaslima520/desafio-atm/assets/70073731/1210267a-4a21-43d8-9d92-86648b2a5a55) - IMAGEM
  
  Na chamada da do endpoint no código de javascript foi passado a url completa 'http://localhost:5000/api/saque' ao invés de '/api/saque', isso porque ao utilizar o liverserver, o mesmo utiliza de um host diferente e acaba gerando o erro 405 (method allowed) diferentemte do postman que já executava a resquest normalmente. Deste forma inserindo a url de requisição no código o browser consegue intrpretar sem nenhuma divergência. 

  ![image](https://github.com/lucaslima520/desafio-atm/assets/70073731/fd720bc3-a709-4573-8a8d-e22a3c905293) - IMAGEM

  .EXTENSÃO LIVESERVER
  Faça o download nas extensões disponíveis do Visual Studio
  .POSTMAN
  Baixe e instale em sua máquina a partir do site https://www.postman.com/downloads/.

PRIMEIRA FORMA DE EXECUÇÃO DO PROJETO - LIVESERVER
  1. Após a instalação do flask será necessário executar o seguinte comando para inicialializarmos o servidor através do terminal do Visual Studio: 'python atm-root/app.py' (caso esteja nas mesmas pastas deste repositório, caso contrário incremente as demias no comando).
  2. Abro o arquivo index ou execute o liverserver a partir do Visual Studio.
  3. Digite o valor de interesse na aba texto disponível e em seguida em calcular, conforme a imagem abaixo:
  4. 
     ![image](https://github.com/lucaslima520/desafio-atm/assets/70073731/18ebae66-184c-4f72-beb7-ea6a0be163f3) - IMAGEM DE TESTE
     
OS RESULTADOS ESTÃO SITUDADOS NO ALERTA APÓS O CLIKC NO BOTÃO 'CALCULAR', TAMBÉM NO CONSOLE DO PRÓPIRO BROWSER ATRAVÉS DA TECLA 'F12' NA ABA 'CONSOLE'.

SEGUNDA FORMA DE EXECUÇÃO DO PROJETO
  1.Caso queira somente realizar a requisição da API basta abrir o postman, selecionar o método POST, inserir a seguinte URL: 'http://localhost:5000/api/saque', em headers: Key 'Content-type' Value 'application/json', já no corpo da requisição escolha o formato JSON e insira seguinte código com valor desejado conforme a imagem abaixo: 
{
    "valor": 100,
}
Clique em 'send' para envio da resição!

![image](https://github.com/lucaslima520/desafio-atm/assets/70073731/e7dcdfba-b9b2-4624-ad74-2fac40af7529) - IMAGEM DE TESTE



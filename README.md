# Stone Trial

As dependências do projeto são:

* matplotlib
* scrapy
* jupyter
* sqlalchemy
* sqlite3

Os CNPJs que serão buscados estão no arquivo `cnpj.txt`, um por linha.

Para executar o crawler, o comando a ser executado é `scrapy crawl cnpj` .
O scrapy buscará os CNPJs na lista com triplo paralelismo, e quando receber da receitaws uma resposta `429`, irá pausar suas atividades por 1 minuto afim de esperar a renovação de acesso.

As informações obtidas serão armazenadas no banco de dados `stone_trial.db`.

As análises estão no notebook `Analise.ipynb`, tanto o código quanto os resultados, e podem ser executadas novamente usando o `jupyter`. 
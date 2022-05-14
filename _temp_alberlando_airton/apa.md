# Você comete este erro no Left Join?

![Imagem de capa do artigo](https://media-exp1.licdn.com/dms/image/C4D12AQG4ox7yv7p6EQ/article-cover_image-shrink_423_752/0/1651578328606?e=2147483647&v=beta&t=ZK8wOw_90WeE1xBBqlyhK_iFUYo9tZ1536HyvMVMUQc)


Imagina que está chegando o dia das crianças e que sua empresa irá promover uma confraternização entre **todos os funcionários e também** oferecer um espaço de brincadeiras **para os filhos** daqueles. Então, você recebe como missão entregar a relação de todos os funcionários e seus respectivos filhos menores de 18 anos.

Vamos supor que temos as seguintes tabelas:

[![Exibição das duas tabelas usadas](https://media-exp1.licdn.com/dms/image/C4D12AQEf8ioRWKt2Zg/article-inline_image-shrink_1500_2232/0/1651581016945?e=2147483647&v=beta&t=IBjlCbKlhJfJbuXyqhAK_gAr_r-f9uXJx0AGvBmd6QY)](https://dbfiddle.uk/?rdbms=sqlserver_2016&fiddle=70d84946a39ee6ae487e93fa4ec7fbf2)

Você começa a fazer a consulta SQL e sabe que nem todos os funcionários possuem filhos. Assim, você usará o _left join e monta a seguinte query:_

SELECT
  F.nome  func\_nome
  ,D.nome depend\_nome
  ,D.idade depend\_idade

FROM FUNCIONARIO F

LEFT JOIN DEPENDENTE
  ON D.func\_id = F.id

WHERE  D.idade < 18

Por incrível que parece, já vi muitas consultas com este tipo de erro. Se você não percebeu o erro, vejamos o retorno da query:

[![tabela de funcionários](https://media-exp1.licdn.com/dms/image/C4D12AQFX8h7E-5HrgQ/article-inline_image-shrink_1500_2232/0/1651582362950?e=2147483647&v=beta&t=gw7GcXNksafjuNB0Mes4Yq-T4nzmAvDNWFlSzifFW4U)](https://dbfiddle.uk/?rdbms=sqlserver_2016&fiddle=70d84946a39ee6ae487e93fa4ec7fbf2)

Como percebido, temos o funcionário _José Bonifácio_ na lista e o _Pe. José de Anchieta,_ não. O resultado esperado seria:

[![tabela de dependentes](https://media-exp1.licdn.com/dms/image/C4D12AQFv_3WyLbzzLw/article-inline_image-shrink_1500_2232/0/1651582381903?e=2147483647&v=beta&t=secJjHusk3oUMmXeKdq5PxgGvYtaL2cYW754qBGcKZY)](https://dbfiddle.uk/?rdbms=sqlserver_2016&fiddle=70d84946a39ee6ae487e93fa4ec7fbf2)

Por que o erro acontece? Porque quando levamos algum campo **idade** (que pertence à tabela do _LEFT JOIN_) para a cláusula _WHERE_, o SGBD passa a fazer um INNER JOIN. Vejamos o plano de execução gerado para esta consulta:

![plano de execução da consulta](https://media-exp1.licdn.com/dms/image/C4D12AQF67eKAciJdAA/article-inline_image-shrink_1500_2232/0/1651583202846?e=2147483647&v=beta&t=nobJsh05_sZTYfdvbki-tgAxxVvuCPtXQxPIPTZZz3A)

Grifado em amarelo está como o BD "monta" a consulta. Ela usou um _INNER JOIN_! Assim, a consulta certa seria:

SELECT
  F.nome   AS 'func\_nome'
  ,D.nome  AS 'depend\_nome'
  ,D.idade AS 'depend\_idade'

FROM FUNCIONARIO F

LEFT JOIN DEPENDENTE D
  ON D.func\_id = F.id
     AND D.idade < 18

Que gera o seguinte plano de execução:

![Não foi fornecido texto alternativo para esta imagem](https://media-exp1.licdn.com/dms/image/C4D12AQE-bxE9WpWTyg/article-inline_image-shrink_1500_2232/0/1651583434146?e=2147483647&v=beta&t=a7DS4UDrIn1p8U66XaWyhBwYsEzNASkdkGjiAs7xQZQ)

Concluindo, refaço a pergunta: Você comete este erro no _Left Join_?
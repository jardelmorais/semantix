# Desafio Spark

### Qual o objetivo do comando CACHE em Spark?
É uma operação lazy, ou seja, não é executada quando chamada, apenas armazena o RDD criado para uma futura operação de ação.
Seria como criar uma view ou procedure no banco, ela não retorna dados a não ser que seja chamada. Consegue ser mais rápida que um select por já estar na memória e evitar o parse
	
### O mesmo código implementado em Spark é normalmente mais rápido que a implementação equivalente em MapReduce. Por que?
  Um dos motivos pode ser porque o spark trabalha sobe um gerenciador de recursos (yarn/mesos) que segrega em containers cada execução, conseguindo paralelizar ou iterar várias vezes sem uma interferir na outra, diferente do mapreduce que faz processos em batch de unico processamento.
  Os RDD´s que implementam estruturas de dados em memória, possibilitando a interação dos algorítimos várias vezes (compartilhado).

### Qual é a função do Spark Context?
Coração da aplicação spark, ela conecta o Spark ao programa que está sendo desenvolvido 
É pra ele que uma app passa as configs necessárias para alocação de recursos (memoria, cpu, etc) 
Criar RDD´s/Jobs/variáveis broadcast 

### Explique com suas palavras o que é Resilient Distributed Datasets (RDD)
Conjunto de objetos distribuidos no cluster, são como tabelas do banco de dados relacionais.

### GroupByKey é menos eficiente que o reduceByKey em grandes datasets. Por que?. 
O GroupByKey precisa juntar todos os dados e enviar ao executor, causando em grandes datasets, alocação de muita memória e eventualmente até uso de disco, o que vai diminuir consideravelmente a performance.
O reduceByKey consegue executar operações separadamente nas partições pela chave passada, levando para os executores apenas para o resultado final.

### Explique o que o código escala abaixo faz:
val textFile = sc.textFile( "hdfs://..." )                                  
> Importa um arquivo via spark context guardando em um RDD chamado textFile

val counts = textFile . flatMap ( line => line. split ( " " ))  
> Splita" o arquivo usando o separador ""

. map ( word => ( word , 1 ))                                             
> faz o mapeamento chave x valor, coloca o resultado em linhas ou tuplas e dá o valor 1 para cada (para somar no final)

. reduceByKey ( _ + _ )                                                       
> Soma o resultado pelas chaves

counts . saveAsTextFile ( "hdfs://..." )                                             
> Salva o resultado no arquivo no endereço passado

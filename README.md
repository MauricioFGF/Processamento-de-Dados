# Processamento e Análise de Dados :minidisc:

O objetivo principal deste projeto  é processar os dados dos candidatos e seus bens declarados á Justiça Eleitoral para o pleito de 2014.

#### Candidatos 

- O Documento **"candidatos.txt"** armazena a lista de todos os candidatos de 2014, juntamente com os dados relevantes para a participação dos mesmos.
- O  Documento **"candidatos.py"** processa todos os dados dos candidatos, incluindo seus bens e os atribuindo para o candidato correspondente. No final é emitida a lista de todos os candidatos, podendo ter variâncias de acordo com as preferencias de pesquisa do usuário. 

#### Bens

- O Documento **"bens.txt"** guarda as informações dos bens dos candidatos de 2014.
- O Documento **"bens.py"** processa e armazena os dados dos bens dos candidatos e os armazena para a analise e distribuição dos bens dos candidatos.		

<hr>

O Documento **"lista.py"**  manipula os dados para serem emitidos para o usuário de acordo com as preferencias escolhida, ex: Ordem alfabética dos candidatos.

O Documento **"controle.py"**  realiza o carregamento dos dados dos candidatos e dos bens atribuídos a eles. Também consegue manipular os dados para remover candidatos ou bens e emite a quantidade de bens dos candidatos baseado no critério selecionado. ex: Quantidade de bens dos candidatos por estado. 

O Documento **"comparacao.py"** Realiza a comparação de dados e emite qual o maior ou o menor de acordo com o critério escolhido.
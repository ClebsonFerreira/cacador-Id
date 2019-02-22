# Caçador 
O Caçador e um coletor de tags html que não possui id dentro de um diretorio 

Obs. Hoje só execulta em projetos ionic v1 que contém a pasta www dentro da raiz 

EX: 
  
        <button id="login" type="submit" class="btn btn-success">Entrar</button>
        <button  type="submit" class="btn btn-success">Novo</button>
 
    E selecionado a segunda opção do arquivo e coloca em um arquivo de log.txt dentro da raiz do projeto 

    ##############-INICIO-##################
    Arquivo: {index.html} , Contém {1} tags sem id 
    <button  type="submit" class="btn btn-success">Novo</button>
    #####################-FIM-#########################


# INSTALAÇÃO

    git clone https://github.com/ClebsonFerreira/cacador-Id.git

    cd cacador-Id 

    pip install -r requirements.txt

    python index.py

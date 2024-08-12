from .decorators import set_client

@set_client
def get_resumo_documento(client, num_doc:str)->list:

    dados_doc = client(
        'consultarDocumento', 
        id_unidade='', 
        protocolo_documento=num_doc,
        sin_retornar_andamento_geracao='N', 
        sin_retornar_assinaturas='N',
        sin_retornar_publicacao='N', 
        sin_retornar_campos='N', 
        sin_retornar_blocos='N', 
        array_return=False
    )


    return dados_doc
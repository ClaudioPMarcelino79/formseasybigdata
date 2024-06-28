import streamlit as st
import yagmail

# Função para enviar o e-mail
def send_email(subject, body, to_email):
    try:
       
        email_user = st.secrets.email_felipe.email_user
        email_password = st.secrets.email_felipe.email_password
        smtp_server = st.secrets.email_felipe.smtp_server
        smtp_port = st.secrets.email_felipe.smtp_port

        if not email_user or not email_password or not smtp_server or not smtp_port:
            st.error("Variáveis de ambiente para e-mail não estão definidas corretamente.")
            return

        yag = yagmail.SMTP(
            user=email_user,
            password=email_password,
            host=smtp_server,
            port=smtp_port,
            smtp_ssl=True
        )
        yag.send(to=to_email, subject=subject, contents=body)
        st.success('Formulário enviado com sucesso!')
    except yagmail.YagAddressError:
        st.error("Endereço de e-mail inválido.")
    except yagmail.YagConnectionClosed:
        st.error("Conexão com o servidor SMTP foi fechada.")
    except yagmail.YagInvalidEmailAddress:
        st.error("Endereço de e-mail inválido.")
    except Exception as e:
        st.error(f'Erro ao enviar o formulário: {str(e)}')

# Título do formulário
st.title('Forms Easy Bigdata')

# Adicionar imagem ao formulário
st.image("logo.png", use_column_width=True)

# Seção de informações pessoais
st.header('Informações Pessoais')
nome = st.text_input('Qual é o seu nome completo?')
email = st.text_input('Qual é o seu e-mail?')
telefone = st.text_input('Qual é o seu número de telefone?')

# Seção de informações sobre a empresa
st.header('Informações sobre a Empresa')
nome_empresa = st.text_input('Qual é o nome da sua empresa?')
setor_empresa = st.text_input('Em qual setor a sua empresa atua?')
num_funcionarios = st.radio('Quantos funcionários a sua empresa possui?', 
                            ['Menos de 50', '50-200', '200-500', 'Mais de 500'])

# Seção de informações sobre dados (opcional)
st.header('Informações sobre DADOS (opcional)')
desafios_dados = st.multiselect('Quais são os principais desafios que a sua empresa enfrenta atualmente em relação a dados?',
                                ['Gestão de dados', 'Análise de dados', 'Integração de dados', 'Segurança de dados', 'Outro (especificar)'])
if 'Outro (especificar)' in desafios_dados:
    outro_desafio = st.text_input('Especifique outro desafio:')

objetivos_big_data = st.multiselect('Quais são os principais objetivos da sua empresa ao investir em soluções de big data?',
                                    ['Melhorar a tomada de decisão', 'Aumentar a eficiência operacional', 'Personalizar a experiência do cliente', 'Outros (especificar)'])
if 'Outros (especificar)' in objetivos_big_data:
    outro_objetivo = st.text_input('Especifique outro objetivo:')

ferramentas_big_data = st.text_input('Quais ferramentas ou tecnologias de big data a sua empresa já utiliza, se houver?')

volume_dados = st.radio('Qual é o volume aproximado de dados que a sua empresa lida mensalmente?',
                        ['Menos de 1 TB', '1-50 TB', '50-150 TB', '150-300 TB', '300-500 TB', 'Mais de 500 TB'])

# Seção de informações sobre o projeto (opcional)
st.header('Informações sobre o Projeto (opcional)')
orcamento_projeto = st.radio('Qual é o orçamento estimado que a sua empresa tem para projetos de big data?',
                             ['Até R$50.000', 'R$50.001 - R$150.000', 'R$150.001 - R$300.000', 'R$300.001 - R$500.000', 'R$500.001 - R$1.000.000', 'Acima de R$1.000.000'])

prazo_projeto = st.text_input('Existe um prazo desejado para iniciar o projeto?')

# Seção de agendamento
st.header('Agendamento')
consulta_inicial = st.radio('Está interessado em agendar uma consulta inicial? Realizar uma PoC (Prova de Conceito) ou um MVP (Minimo Produto Viável).', ['Sim', 'Não'])
preferencia_contato = st.radio('Qual a sua preferência para o contato?', ['E-mail', 'Telefone', 'Video Chamada (meet)'])
data_hora_contato = st.text_input('Data e hora preferida para contato (informe 3 opções):')

# Seção de informações adicionais
st.header('Informações Adicionais')
informacoes_adicionais = st.text_area('Há algo mais que você gostaria de compartilhar sobre as suas necessidades ou expectativas?')

# Seção de consentimento para contato
st.header('Consentimento para Contato')
consentimento = st.radio('Você concorda em ser contatado por nós para futuras comunicações?', ['Sim', 'Não'])

# Botão para enviar
if st.button('Enviar'):
    # Construir corpo do e-mail
    email_body = f"""
    Informações Pessoais:
    Nome: {nome}
    E-mail: {email}
    Telefone: {telefone}

    Informações sobre a Empresa:
    Nome da Empresa: {nome_empresa}
    Setor: {setor_empresa}
    Número de Funcionários: {num_funcionarios}

    Informações sobre DADOS (opcional):
    Desafios: {', '.join(desafios_dados)}
    Outro Desafio: {outro_desafio if 'Outro (especificar)' in desafios_dados else 'N/A'}
    Objetivos: {', '.join(objetivos_big_data)}
    Outro Objetivo: {outro_objetivo if 'Outros (especificar)' in objetivos_big_data else 'N/A'}
    Ferramentas/tecnologias: {ferramentas_big_data}
    Volume de Dados: {volume_dados}

    Informações sobre o Projeto (opcional):
    Orçamento: {orcamento_projeto}
    Prazo: {prazo_projeto}

    Agendamento:
    Consulta Inicial: {consulta_inicial}
    Preferência de Contato: {preferencia_contato}
    Data e Hora para Contato: {data_hora_contato}

    Informações Adicionais: {informacoes_adicionais}

    Consentimento para Contato: {consentimento}
    """

    # Enviar e-mail
    to_emails = ['claudio.marcelino@easybigdata.com.br', 'felipe.silvestre@easybigdata.com.br']
    send_email('Resposta do Formulário de Coleta de Informações', email_body, to_emails)
    #send_email('Resposta do Formulário de Coleta de Informações', email_body, 'claudio.marcelino@easybigdata.com.br', 'felipe.silvestre@easybigdata.com.br)

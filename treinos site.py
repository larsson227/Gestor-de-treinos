import streamlit as st

# Configuração da página
st.set_page_config(page_title="Gestor de Treinos", layout="centered")

st.title("🏃 Registro de Treinos")

# Inicializa as listas no "estado da sessão" para não perder os dados ao recarregar a página
if "registados" not in st.session_state:
    st.session_state.registados = []
if "agendados" not in st.session_state:
    st.session_state.agendados = []

# Menu lateral para navegação
menu = st.sidebar.selectbox("Menu", ["Registar Treino", "Ver Registos", "Agendar Treino", "Ver Agenda"])

if menu == "Registar Treino":
    st.subheader("Novo Registro")
    nome_kms = st.text_input("Digite o nome do treino e os kms (ex: Corrida 5km)")
    if st.button("Salvar Treino"):
        if nome_kms:
            st.session_state.registados.append(nome_kms)
            st.success("Treino registado com sucesso!")
        else:
            st.error("Por favor, digite algo.")

elif menu == "Ver Registos":
    st.subheader("Histórico de Treinos")
    if st.session_state.registados:
        for t in st.session_state.registados:
            st.write(f"✅ {t}")
            st.divider()
    else:
        st.info("Nenhum treino registado ainda.")

elif menu == "Agendar Treino":
    st.subheader("Agendamento")
    data_kms = st.text_input("Digite a data e os kms (ex: 20/05 - 10km)")
    if st.button("Agendar"):
        if data_kms:
            st.session_state.agendados.append(data_kms)
            st.success("Treino agendado!")
        else:
            st.error("Preencha os dados do agendamento.")

elif menu == "Ver Agenda":
    st.subheader("Próximos Treinos")
    if st.session_state.agendados:
        for a in st.session_state.agendados:
            st.write(f"📅 {a}")
            st.divider()
    else:
        st.info("Agenda vazia.")

# Botão para limpar (equivalente ao menu 5)
if st.sidebar.button("Limpar Tudo"):
    st.session_state.registados = []
    st.session_state.agendados = []
    st.rerun()
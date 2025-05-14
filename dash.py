import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st 

df = pd.read_csv('fifa_players.csv')

st.title("Analise de jogadores fifa")




def main():
    st.subheader("Tabela de jogadores")
    st.write(df)
    col1,col2 =st.columns(2)
    col3,col4 = st.columns(2)
    with col1:
        dados_para_Gdispersao = df.groupby('nationality')[['overall_rating','potential']].mean()
        st.subheader("overall médio x potencial médio por País")
        st.scatter_chart(data=dados_para_Gdispersao)
    
    with col2:
        st.subheader("relação da média entre potencial e overall por idade")
        dados_de_linha = df.groupby('age')[['overall_rating','potential']].mean()
        st.line_chart(data=dados_de_linha)
    
    with col3:
        st.subheader('Média das caracteristicas por posição')
        dados_de_barra = df.groupby('national_team_position')[['crossing','finishing','heading_accuracy','short_passing','volleys','dribbling','curve','freekick_accuracy','long_passing','ball_control','acceleration','sprint_speed','agility','reactions','balance','shot_power','jumping','stamina','strength','long_shots','aggression','interceptions','positioning','vision','penalties','composure','marking','standing_tackle','sliding_tackle']].mean()
        st.bar_chart(data=dados_de_barra)
        
    with col4:
        paises_overall = df['nationality'].value_counts().nlargest(10)
        fig,graf = plt.subplots()
        graf.pie(paises_overall,labels=paises_overall.index,autopct='%1.1f%%', startangle=90)
        graf.axis('equal')
        st.subheader('Top 10 países com mais jogadores')
        st.pyplot(fig)

def dashFiltrado(filtro):
    df_filtrado = df[df['nationality']==filtro]
    st.subheader("Tabela de jogadores")
    st.write(df_filtrado)
    
    col1,col2 = st.columns(2)
    col3,col4 = st.columns(2)
    
    with col1:
        st.subheader("overall x potencial")
        dispersao = df_filtrado.groupby('name')[['overall_rating','potential']].max()
        st.scatter_chart(data=dispersao)
        
    with col2:
        st.subheader("relação da média entre potencial e overall por idade")
        linha = df_filtrado.groupby('age')[['overall_rating','potential']].mean()
        st.line_chart(data=linha)
    
    with col3:
        jogadores = df_filtrado[['name', 'overall_rating']].sort_values(by='overall_rating', ascending=False).head(10)
        st.subheader("Top 10 overall do país")
        st.bar_chart(data=jogadores.set_index('name'))
        
    with col4:
        jogadores_p = df_filtrado[['name', 'potential']].sort_values(by='potential', ascending=False).head(10)
        st.subheader("Top 10 potenciais do país")
        st.bar_chart(data=jogadores_p.set_index('name'))
    
paises = sorted(df['nationality'].unique())
with st.sidebar:
    opcao = st.selectbox("Escolha um pais para analizar:",paises)
    botaoAplicar = st.button(label="Aplicar filtro")
    st.write("Clique no botão para voltar para a análise geral:")
    botao = st.button(label="análise geral")
        
#parte onde tudo é chamado

if botaoAplicar:
    dashFiltrado(opcao)
elif botao:
    main()
else:
    main()

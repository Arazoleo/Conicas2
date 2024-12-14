import streamlit as st
import plotly.graph_objects as go
import numpy as np

def Elipse_Composer(eixo, a, b, center=(0, 0), angle=0, resolution=1000):
    if eixo == 'y':  
        a, b = b, a

    t = np.linspace(0, 2 * np.pi, resolution)
    x = center[0] + a * np.cos(t) * np.cos(angle) - b * np.sin(t) * np.sin(angle)
    y = center[1] + a * np.cos(t) * np.sin(angle) + b * np.sin(t) * np.cos(angle)

    fig = go.Figure()

    
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Elipse'))

   
    vertices_horizontal = [(center[0] + a * np.cos(angle), center[1] + a * np.sin(angle)),
                           (center[0] - a * np.cos(angle), center[1] - a * np.sin(angle))]
    fig.add_trace(go.Scatter(x=[v[0] for v in vertices_horizontal],
                             y=[v[1] for v in vertices_horizontal],
                             mode='markers',
                             marker=dict(color='red'),
                             name='Vértices do Eixo Maior'))

    vertices_vertical = [(center[0] - b * np.sin(angle), center[1] + b * np.cos(angle)),
                         (center[0] + b * np.sin(angle), center[1] - b * np.cos(angle))]
    fig.add_trace(go.Scatter(x=[v[0] for v in vertices_vertical],
                             y=[v[1] for v in vertices_vertical],
                             mode='markers',
                             marker=dict(color='blue'),
                             name='Vértices do Eixo Menor'))

    
    c = np.sqrt(abs(a**2 - b**2))
    if eixo == 'y':
        foco1 = (center[0], center[1] + c)
        foco2 = (center[0], center[1] - c)
        fig.add_trace(go.Scatter(x=[foco1[0]], y=[foco1[1]],
                                 mode='markers', marker=dict(color='green'), name='Foco 1'))
        fig.add_trace(go.Scatter(x=[foco2[0]], y=[foco2[1]],
                                 mode='markers', marker=dict(color='yellow'), name='Foco 2'))
        title = 'Elipse com Eixo Maior na Vertical'
    else:
        foco1 = (center[0] + c, center[1])
        foco2 = (center[0] - c, center[1])
        fig.add_trace(go.Scatter(x=[foco1[0]], y=[foco1[1]],
                                 mode='markers', marker=dict(color='green'), name='Foco 1'))
        fig.add_trace(go.Scatter(x=[foco2[0]], y=[foco2[1]],
                                 mode='markers', marker=dict(color='yellow'), name='Foco 2'))
        title = 'Elipse com Eixo Maior na Horizontal'

    fig.update_layout(
        title=title,
        xaxis_title='X',
        yaxis_title='Y',
        xaxis=dict(scaleanchor="y", scaleratio=1),
        yaxis=dict(scaleanchor="x", scaleratio=1),
        showlegend=True
    )

    return fig


def main():
    st.title("Composição de Elipses")
    st.write("Insira os parâmetros abaixo para gerar a elipse:")


    eixo = st.radio("Escolha o eixo maior:", options=['x', 'y'], index=0)
    a = st.number_input("Valor do eixo maior (a):", min_value=0.1, value=5.0, step=0.1)
    b = st.number_input("Valor do eixo menor (b):", min_value=0.1, value=3.0, step=0.1)
    if a < b:
        st.error("O valor do eixo maior (a) deve ser maior que o eixo menor (b).")

    x = st.number_input("Coordenada X do centro:", value=0.0, step=0.1)
    y = st.number_input("Coordenada Y do centro:", value=0.0, step=0.1)
    center = (x, y)

    angle_deg = st.slider("Ângulo de rotação (em graus):", min_value=0, max_value=360, value=0)
    angle_rad = np.radians(angle_deg)

    resolution = st.slider("Resolução (número de pontos):", min_value=100, max_value=5000, value=1000, step=100)

    
    if st.button("Gerar Elipse"):
        fig = Elipse_Composer(eixo, a, b, center=center, angle=angle_rad, resolution=resolution)
        st.plotly_chart(fig)

if __name__ == '__main__':
    main()

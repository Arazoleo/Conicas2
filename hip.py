import streamlit as st
import numpy as np
import plotly.graph_objects as go

def construct_hyperbola(a, b, x0, y0):
    c = np.sqrt(a**2 + b**2)

    fig = go.Figure()

    if a > b:  
        x = np.linspace(x0 - 10 * a, x0 + 10 * a, 400)
        y_positive = []
        y_negative = []

        for x_val in x:
            if (x_val - x0)**2 / a**2 - 1 >= 0:
                y_val = b * np.sqrt((x_val - x0)**2 / a**2 - 1)
                y_positive.append(y_val + y0)
                y_negative.append(-y_val + y0)
            else:
                y_positive.append(np.nan)
                y_negative.append(np.nan)

        y_positive = np.array(y_positive)
        y_negative = np.array(y_negative)

        
        asymptote_y1 = y0 + (b / a) * (x - x0)
        asymptote_y2 = y0 - (b / a) * (x - x0)

       
        fig.add_trace(go.Scatter(x=x, y=y_positive, mode='lines', name='Hipérbole Superior', line=dict(color='blue')))
        fig.add_trace(go.Scatter(x=x, y=y_negative, mode='lines', name='Hipérbole Inferior', line=dict(color='blue')))
        fig.add_trace(go.Scatter(x=x, y=asymptote_y1, mode='lines', name='Assíntota 1', line=dict(color='red', dash='dash')))
        fig.add_trace(go.Scatter(x=x, y=asymptote_y2, mode='lines', name='Assíntota 2', line=dict(color='red', dash='dash')))
        
        
        fig.add_trace(go.Scatter(x=[x0 + a, x0 - a], y=[y0, y0], mode='markers', name='Vértices', marker=dict(color='green', size=10)))
        
        fig.add_trace(go.Scatter(x=[x0 + c, x0 - c], y=[y0, y0], mode='markers', name='Focos', marker=dict(color='red', size=10)))

    else:  
        y = np.linspace(y0 - 10 * b, y0 + 10 * b, 400)
        x_positive = []
        x_negative = []

        for y_val in y:
            if (y_val - y0)**2 / b**2 - 1 >= 0:
                x_val = a * np.sqrt((y_val - y0)**2 / b**2 - 1)
                x_positive.append(x_val + x0)
                x_negative.append(-x_val + x0)
            else:
                x_positive.append(np.nan)
                x_negative.append(np.nan)

        x_positive = np.array(x_positive)
        x_negative = np.array(x_negative)

        # Assíntotas
        asymptote_x1 = x0 + (a / b) * (y - y0)
        asymptote_x2 = x0 - (a / b) * (y - y0)

        # Adicionando os gráficos
        fig.add_trace(go.Scatter(x=x_positive, y=y, mode='lines', name='Hipérbole Direita', line=dict(color='blue')))
        fig.add_trace(go.Scatter(x=x_negative, y=y, mode='lines', name='Hipérbole Esquerda', line=dict(color='blue')))
        fig.add_trace(go.Scatter(x=asymptote_x1, y=y, mode='lines', name='Assíntota 1', line=dict(color='red', dash='dash')))
        fig.add_trace(go.Scatter(x=asymptote_x2, y=y, mode='lines', name='Assíntota 2', line=dict(color='red', dash='dash')))
        
        
        fig.add_trace(go.Scatter(x=[x0, x0], y=[y0 + b, y0 - b], mode='markers', name='Vértices', marker=dict(color='green', size=10)))
        
     
        fig.add_trace(go.Scatter(x=[x0, x0], y=[y0 + c, y0 - c], mode='markers', name='Focos', marker=dict(color='red', size=10)))


    fig.update_layout(
        title="Gráfico Interativo da Hipérbole com Assíntotas, Vértices e Focos",
        xaxis_title="x",
        yaxis_title="y",
        showlegend=True,
        xaxis=dict(showgrid=True, zeroline=True),
        yaxis=dict(showgrid=True, zeroline=True),
        width=800,
        height=800
    )

    return fig


st.title("Hipérbole com Elementos")
st.write("""
Este aplicativo permite visualizar gráficos de hipérboles com assíntotas, vértices e focos. 
Você pode ajustar os parâmetros e explorar a geometria.
""")


a_input = st.text_input("Valor de a (semi-eixo real)", "5")
b_input = st.text_input("Valor de b (semi-eixo imaginário)", "3")


try:
    a = float(a_input)
    b = float(b_input)

    if a <= 0 or b <= 0:
        st.error("Os valores de 'a' e 'b' devem ser positivos e maiores que zero.")
        a = b = 0  
except ValueError:
    st.error("Por favor, insira números válidos para 'a' e 'b'.")
    a = b = 0  


x0 = st.number_input("Coordenada x do centro", value=0.0, step=0.1)
y0 = st.number_input("Coordenada y do centro", value=0.0, step=0.1)

# Gerar o gráfico
if a != 0 and b != 0:
    fig = construct_hyperbola(a, b, x0, y0)
    st.plotly_chart(fig)

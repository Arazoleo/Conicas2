import streamlit as st
import numpy as np
import plotly.graph_objects as go

def parabola_horizontal(a, p, h, k):
    
    x = np.linspace(h - 10, h + 10, 400)
    argumento = 4 * a * p * (x - h)

    
    y = np.where(argumento >= 0, np.sqrt(argumento) + k, np.nan)
    y_neg = np.where(argumento >= 0, -np.sqrt(argumento) + k, np.nan)

    foco = (h + p, k) if a > 0 else (h - p, k)
    diretriz = h - p if a > 0 else h + p

    
    fig = go.Figure()

    
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='y² = 4ap(x-h) (positivo)'))
    fig.add_trace(go.Scatter(x=x, y=y_neg, mode='lines', name='y² = 4ap(x-h) (negativo)'))

   
    fig.add_trace(go.Scatter(x=[h], y=[k], mode='markers+text',
                             text=[f'Vértice ({h}, {k})'], textposition='bottom center',
                             marker=dict(color='red', size=8), name='Vértice'))

    
    fig.add_trace(go.Scatter(x=[foco[0]], y=[foco[1]], mode='markers+text',
                             text=[f'Foco ({foco[0]:.2f}, {foco[1]:.2f})'], textposition='top center',
                             marker=dict(color='yellow', size=8), name='Foco'))

    
    fig.add_shape(type="line", x0=diretriz, y0=min(y_neg[np.isfinite(y_neg)]), x1=diretriz, y1=max(y[np.isfinite(y)]),
                  line=dict(color='green', dash='dash'), name='Diretriz')


    fig.update_layout(title=f'Parábola Horizontal: y² = 4ap(x - h)',
                      xaxis_title='x', yaxis_title='y',
                      xaxis=dict(showgrid=True, zeroline=True),
                      yaxis=dict(showgrid=True, zeroline=True),
                      showlegend=True,
                      height=600, width=800)
    return fig

def parabola_vertical(a, p, h, k):
   
    y = np.linspace(k - 10, k + 10, 400)
    argumento = 4 * a * p * (y - k)

   
    x = np.where(argumento >= 0, np.sqrt(argumento) + h, np.nan)
    x_neg = np.where(argumento >= 0, -np.sqrt(argumento) + h, np.nan)

   
    foco = (h, k + p) if a > 0 else (h, k - p)
    diretriz = k - p if a > 0 else k + p

    
    fig = go.Figure()

    
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='x² = 4ap(y-k) (positivo)'))
    fig.add_trace(go.Scatter(x=x_neg, y=y, mode='lines', name='x² = 4ap(y-k) (negativo)'))

    
    fig.add_trace(go.Scatter(x=[h], y=[k], mode='markers+text',
                             text=[f'Vértice ({h}, {k})'], textposition='bottom center',
                             marker=dict(color='blue', size=8), name='Vértice'))

    
    fig.add_trace(go.Scatter(x=[foco[0]], y=[foco[1]], mode='markers+text',
                             text=[f'Foco ({foco[0]:.2f}, {foco[1]:.2f})'], textposition='top center',
                             marker=dict(color='yellow', size=8), name='Foco'))

  
    fig.add_shape(type="line", x0=min(x_neg[np.isfinite(x_neg)]), y0=diretriz, x1=max(x[np.isfinite(x)]), y1=diretriz,
                  line=dict(color='green', dash='dash'), name='Diretriz')


    fig.update_layout(title=f'Parábola Vertical: x² = 4ap(y - k)',
                      xaxis_title='x', yaxis_title='y',
                      xaxis=dict(showgrid=True, zeroline=True),
                      yaxis=dict(showgrid=True, zeroline=True),
                      showlegend=True,
                      height=600, width=800)
    return fig

def main():
    st.title("Gráfico de Parábolas Canônicas")
    st.sidebar.title("Configurações da Parábola")

   
    a = st.sidebar.number_input("Valor de 'a' (orientação e abertura)", value=1.0, step=0.1)
    p = st.sidebar.number_input("Valor de 'p' (distância do vértice ao foco)", value=1.0, step=0.1)
    h = st.sidebar.number_input("Valor de 'h' (x do vértice)", value=0.0, step=0.1)
    k = st.sidebar.number_input("Valor de 'k' (y do vértice)", value=0.0, step=0.1)
    op = st.sidebar.radio("Escolha o tipo de parábola:", ["Parábola Horizontal (y² = 4ap(x - h))", "Parábola Vertical (x² = 4ap(y - k))"])

    
    if p <= 0:
        st.error("Erro: O valor de 'p' deve ser positivo para gerar um gráfico válido.")
    else:
     
        if op == "Parábola Horizontal (y² = 4ap(x - h))":
            fig = parabola_horizontal(a, p, h, k)
            st.plotly_chart(fig)
        elif op == "Parábola Vertical (x² = 4ap(y - k))":
            fig = parabola_vertical(a, p, h, k)
            st.plotly_chart(fig)

if __name__ == "__main__":
    main()

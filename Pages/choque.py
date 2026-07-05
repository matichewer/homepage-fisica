import streamlit as st
import pandas as pd
from PIL import Image
from io import BytesIO
import requests

# Link golf : https://drive.google.com/file/d/1HGXU91fEMXKLz2u2nuIkRMgstaB32laE/view?usp=drive_link
def app():
    st.markdown("# **CHOQUE**")

    st.markdown("### Dos pelotas, una de **tenis** y una de **basquet** chocan")

    texto = """
            Durante este experimento, medimos las masas de ambas pelotas, 
            así como sus velocidades iniciales y finales. 
            Estos datos nos permitieron calcular la cantidad de movimiento (momentum) 
            antes y después del choque, y determinar si hubo pérdida de energía, calculando 
            la energía cinética antes y después del impacto.\n
           Los resultados obtenidos confirmaron que, por un lado, la cantidad de movimiento
           se conserva antes y después del choque, cumpliendo con el principio de conservación del momento lineal. 
           Por otro lado, el choque resultó ser inelástico, ya que se observó
           una pérdida de parte de la energía cinética, que se disipa en forma de calor, sonido u otras formas de energía no recuperables.

       """
    st.markdown(texto)

    # Link:
    # https://drive.google.com/file/d/1LeyBvFRo9xSo2VaN3w5FjhJd9ot86fbs/view?usp=drive_link
    # id video = 1LeyBvFRo9xSo2VaN3w5FjhJd9ot86fbs

    video_url = 'https://drive.google.com/file/d/1d71bNGU2dXCSSL5MStzrTC8oh8mZ_RK-/preview'

    # Insertar el video usando HTML
    st.markdown(f"""
            <div style="text-align: center;">
                 <iframe src="{video_url}" width="640" height="480" allow="autoplay"></iframe>
             </div>
            """, unsafe_allow_html=True)

    st.write("\n\n")

    texto2="""
        Para el análisis, se elige un sistema de referencia positivo hacia la derecha 
        y se aplica el principio de conservación de la cantidad de movimiento.\n
        Esto significa que la cantidad de movimiento total de los dos cuerpos 
        (en nuestro caso, la pelota de tenis y la pelota de básquet) antes del
        choque debe ser igual a la cantidad de movimiento total después del choque.\n
        Matemáticamente, esto se expresa como:
        
    """
    st.markdown(texto2)
    latex_ec=r"""
        \mathbf{P_{f}} \ = \mathbf{P_{0}}
    """
    st.latex(latex_ec)

    texto3="""
    También se plantea la conservación de la energía cinética.\n
    La energía cinética total que tienen los dos cuerpos antes del
    choque debe ser igual a la energía cinética total que tienen
    los dos cuerpos después del choque. Esto se expresa mediante la siguiente ecuación:\n
    """
    st.markdown(texto3)
    latex_ec2=r"""
        \mathbf{E_{f}} = \mathbf{E_{0}}
    """
    st.latex(latex_ec2)
    st.write("\n \n Ecuaciones a utilizar: \n")
    st.markdown("- Conservacion de cantidad de movimiento: ")
    latex_ec3=r"""
        \mathbf{P_{0}} \ = \mathbf{P_{f}} \Rightarrow \mathbf{m_{a}} \ast \mathbf{V_{A0}} + \mathbf{m_{b}} \ast \mathbf{V_{B0}} = \mathbf{m_{a}} \ast \mathbf{V_{Af}} + \mathbf{m_{b}} \ast \mathbf{V_{Bf}}
    """
    st.latex(latex_ec3)
    latex_ec4=r"""
        \mathbf{E_{f}} =  \mathbf{E_{0}} \Rightarrow \frac{1}{2} \mathbf{m_{1}} \ast \mathbf{V^2_{0}} + \frac{1}{2} \mathbf{m_{2}} \ast \mathbf{V^2_{0}}   = \mathbf{E_{0}} \Rightarrow \frac{1}{2} \mathbf{m_{1}} \ast \mathbf{V^2_{f}} + \frac{1}{2} \mathbf{m_{2}} \ast \mathbf{V^2_{f}} 
    """
    st.markdown("- Conservacion de la energia cinética: ")
    st.latex(latex_ec4)

    st.markdown("## Materiales y métodos")

    texto3="""
    Para este experimento, grabamos un video en una cancha de básquet. \n
    Utilizamos un trípode, un celular, una pelota de tenis, una pelota de básquet y dos personas.\n
    Tomamos las medidas correspondientes en el **Sistema Internacional (SI)** o **MKS:** **metro (m)**, **kilogramo (kg)** y **segundo (s)**. \n
    Usamos una balanza para pesar ambas pelotas antes de grabar el experimento, obteniendo los siguientes datos:
    -   Masa de la pelota de tenis: 0.06kg
    -   Masa de la pelota de basquet: 0.62kg\n
    Para obtener las velocidades iniciales y finales de ambas pelotas en ambos ejes, nos basamos en las siguientes tablas:\n
    """
    st.markdown(texto3)

    #LINK IMAGEN
    #https://drive.google.com/file/d/1NNb_r7RRBTmM03E33TQR-mp8uAGIaz1Y/view?usp=drive_link
    #https://drive.google.com/file/d/1tD4ouCGRkGXl0OtOQ_XJcGbUrihmE_mP/view?usp=drive_link
    grafico='1NNb_r7RRBTmM03E33TQR-mp8uAGIaz1Y'
    grafico_2='1tD4ouCGRkGXl0OtOQ_XJcGbUrihmE_mP'
    def get_image_from_drive(file_id):
        url = f"https://drive.google.com/uc?export=download&id={file_id}"
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        return img
    # Obtener y mostrar la imagen en Streamlit
    imagen_1 = get_image_from_drive(grafico)
    st.image(imagen_1, caption="Grafico 1")

    texto4="""
    A partir del video y del trackeo en Python, obtuvimos la posición en X e Y en píxeles, así como el tiempo. 
    Las últimas dos columnas corresponden a la conversión de píxeles a metros, considerando que un píxel equivale a 0.00491 m.\n
    """
    st.write(texto4)
    st.write("\n")
    image_2=get_image_from_drive(grafico_2)
    st.image(image_2,caption="Grafico 2")

    st.write("\n")

import streamlit as st
import pandas as pd
from PIL import Image
from io import BytesIO
import requests
def app():
    st.markdown("# DINAMICA")

    st.write("\n\n")

    texto = """

    Para el estudio de dinámica, realizamos un experimento en el cual grabamos un video donde se lanza una pelota de básquet al aro. En dinámica, utilizamos tres conceptos fundamentales: fuerza, masa y aceleración.
    En este experimento, calcularemos la fuerza ejercida en el tiro al aro.

    ## **Introducción**

    Hasta ahora, hemos definido magnitudes que nos permitieron describir el movimiento de un cuerpo puntual (CP) respecto a un sistema de referencia (SR). Ahora, nos enfocaremos en estudiar la dinámica.
    Comenzaremos explicando los tres conceptos básicos del estudio de dinámica.
    
    Una **fuerza** es una magnitud física que causa un cambio en el movimiento o la forma de un objeto. Cuando la fuerza empieza a actuar, el cuerpo que estaba quieto comienza a moverse. Si no permitimos que el cuerpo se mueva, la fuerza actuará deformándolo o rompiéndolo.
    
    La **masa** es una cantidad que indica cuán difícil es acelerar o frenar un cuerpo. También se puede entender la masa como una medida de la tendencia de los cuerpos a mantener su estado de movimiento, lo que en la vida diaria se suele llamar inercia.
    
    La **aceleración** es una cantidad que nos dice qué tan rápido está aumentando o disminuyendo la velocidad de un cuerpo. Como sabemos de cinemática, si un objeto tiene una aceleración de , eso significa que su velocidad aumenta en  por cada segundo que pasa. Por ejemplo, si al principio su velocidad es cero, después de un segundo será de , después de dos segundos será de , y así sucesivamente.
    """

    # Mostrar los textos en Streamlit
    st.markdown(texto)

    # Texto con las leyes de Newton resaltadas y formateadas
    texto_laws = """
    Ahora bien, explorando las causas de los cambios en el estado del cuerpo puntual (CP), tenemos las tres leyes de Newton. Estas leyes son principios físicos que resultan de hechos experimentales. 

    ### **Primera Ley de Newton: Ley de inercia**
    Un cuerpo puntual permanece en reposo o continúa en movimiento rectilíneo y uniforme si sobre él no actúan fuerzas desequilibradas.

    ### **Segunda Ley de Newton**
    La aceleración de un cuerpo puntual es proporcional a la fuerza resultante que se ejerce sobre él y tiene la misma dirección y sentido de dicha fuerza.

    ### **Tercera Ley de Newton: Principio de acción y reacción**
    Las fuerzas de acción y reacción entre cuerpos en contacto son de igual intensidad y colineales, pero tienen sentidos opuestos. La validez de estas leyes ha sido verificada mediante numerosas mediciones físicas de gran precisión.

    Las dos primeras leyes de Newton son válidas para mediciones efectuadas en un sistema de referencia absoluto, pero deben corregirse levemente cuando se realizan respecto a un sistema de referencia acelerado, como la superficie terrestre. La segunda ley de Newton constituye la base de la mayoría de los análisis en mecánica. Aplicada a un punto material de masa \\(m\\), sometido a una fuerza resultante \\(F\\), puede enunciarse en la forma:

    """
    texto_lawx2= """Donde \\(a\\) es la aceleración medida en un sistema de referencia no acelerado. La primera ley de Newton es consecuencia de la segunda, ya que no habrá aceleración si la fuerza es nula, y en tal caso la partícula debe estar en reposo o moviéndose a velocidad constante. La tercera ley constituye el principio de acción y reacción.
    """

    # Mostrar el texto en Streamlit con Markdown
    st.markdown(texto_laws, unsafe_allow_html=True)
    st.latex(r""" F = ma  """)
    st.markdown(texto_lawx2)
    st.markdown("## Video analizado")

    # Enlace embebido de Google Drive tiro del chipi
    video_url = 'https://drive.google.com/file/d/1t6dzRm44syZZ8PSQqG2OK0KDNAIkGoCl/preview'

    # Insertar el video usando HTML
    st.markdown(f"""
            <div style="text-align: center;">
                 <iframe src="{video_url}" width="640" height="480" allow="autoplay"></iframe>
             </div>
            """, unsafe_allow_html=True)

    st.markdown("## Materiales y Métodos")
    texto_material="""
        Tomando las medidas correspondientes en el **Sistema Internacional (SI)** o **MKS**: \n
        - **metro (m)**
        - **kilogramo (kg)** 
        - **segundo (s)** \n
        Utilizamos una balanza para obtener la masa de la pelota de básquet, que resultó ser **0.62kg.**
        Obtuvimos la aceleración en el eje X  mediante cálculos en Python, y con esta información podemos calcular 
        la fuerza resultante en el eje x.\n
        Teniendo en cuenta 

    """
    st.markdown(texto_material)

    delta_eq = r"""
    \Delta \mathbf{X} \; \Delta \mathbf{Y} \; \mathbf{F_x}
    """
    st.latex(delta_eq)
    st.write("\n")
    texto_sig="""
        Podemos calcular mediante:
    """

    delta_emec=r"""
        \Delta E_{\text{MEC}}
    """
    st.latex(delta_emec)

    texto_sig2="""
        Y poder obtener:
    """
    texto_fy=r"""
        \mathbf{F_y}
    """
    st.write(texto_sig2)

    st.latex(texto_fy)

    fuerzas_eq = r"""
    \|\mathbf{F}\| = \sqrt{F_x^2 + F_y^2}
    """
    st.latex(fuerzas_eq)

    st.markdown("### Resultados obtenidos:")
    st.markdown("Para mayor detalle de los resultados ir al **Anexo**")

    #LINK IMAGEN
    #
    # Función para obtener la imagen desde Google Drive
    # imagen_url_d ='https://drive.google.com/file/d/1WJhPSfvwQmrlvZUSJvIaDtP6yBKyPU9H/view?usp=drive_link'
    # imagen_url_d2='https://drive.google.com/file/d/1TkV8BqeZM3ePUMLlCOx2W_90ILnrySA6/view?usp=drive_link'
    id_din='1WJhPSfvwQmrlvZUSJvIaDtP6yBKyPU9H'
    id_din2='1TkV8BqeZM3ePUMLlCOx2W_90ILnrySA6'
    def get_image_from_drive(file_id):
        url = f"https://drive.google.com/uc?export=download&id={file_id}"
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        return img

    # ID de la imagen en Google Drive
    file_id = id_din

    # Obtener y mostrar la imagen en Streamlit
    image = get_image_from_drive(file_id)
    st.image(image, caption="Resultado")

    st.write("\n\n")
    file_id2= id_din2
    image2=get_image_from_drive(file_id2)
    st.image(image2,caption="Resultado")
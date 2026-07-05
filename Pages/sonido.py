import streamlit as st
import pandas as pd
from PIL import Image
from io import BytesIO
import requests

def app():
    st.markdown("# **AUDIO**")

    texto="""
    En este experimento, medimos la masa de la pelota de golf, la altura desde la cual se 
    dejó caer la pelota, y utilizamos el audio del video para obtener los tiempos en los
    que la pelota choca con el suelo de cemento.\n Estos datos nos permitieron calcular el
    coeficiente de restitución, que mide el grado de conservación de la energía cinética.\n
    Los resultados obtenidos confirman que en cada choque la pelota pierde altura debido
    a la pérdida de energía, lo cual se refleja en la disminución de la velocidad
    antes y después del choque.\n
    """
    st.markdown(texto)
    #LINK AUDIO:
    #   https://drive.google.com/file/d/1CczDtTo53xOFARmVvCf5P49mQDQipNFF/view?usp=drive_link
    #LINK VIDEO:
    #   https://drive.google.com/file/d/1HGXU91fEMXKLz2u2nuIkRMgstaB32laE/view?usp=drive_link

    video_url='https://drive.google.com/file/d/1_pEC_OYsoi90BOTCzkWUeKNimO8ay_I-/preview'

    # Insertar el video usando HTML
    st.markdown(f"""
             <div style="text-align: center;">
                  <iframe src="{video_url}" width="640" height="480" allow="autoplay"></iframe>
              </div>
             """, unsafe_allow_html=True)


    audio_file = '1CczDtTo53xOFARmVvCf5P49mQDQipNFF'

    # Construir la URL de descarga directa
    url = f"https://drive.google.com/uc?export=download&id={audio_file}"

    url2 = 'https://github.com/Chicago-Fisicos/proyecto-fisica/blob/main/src/audios/videos-y-audios/output_with_audio.mp4?raw=true'

    # Mostrar el reproductor de audio en Streamlit
    st.audio(url2)

    texto2= """
        En un choque elástico, no se pierde energía. En estos choques, la energía cinética total se conserva.
        El coeficiente de restitución está directamente relacionado con el estudio de choques, 
        ya que proporciona una medida cuantitativa de cómo se comportan los cuerpos antes y 
        después del choque.\n
        Al calcular el coeficiente de restitución, podemos determinar cuánta energía cinética se conserva y cuánta se disipa en formas no mecánicas, como el calor o la deformación.
        Esto nos permite clasificar el choque según su elasticidad.\n
    """
    st.markdown(texto2)

    st.markdown("## Materiales y métodos")

    texto3="""
    Para este experimento, grabamos un video en un suelo de cemento.
    Utilizamos un celular, un micrófono, una pelota de golf y una referencia 
    métrica desde la cual lanzamos la pelota para obtener la altura.\n
    Tomamos las medidas correspondientes en el **Sistema Internacional (SI)** o **MKS:** **metro (m)*,
    **kilogramo (kg)** y **segundo (s).**\n
    Pesamos la pelota de golf con una balanza.\n 
    La referencia métrica fue un cartón con dimensiones de 0.3 m x 0.3 m.\n
    Desde una altura de 0.3 m sobre el suelo, lanzamos la pelota de golf y grabamos el video.
    En cuanto al audio, en formato **.wav**, primero lo pasamos por un ecualizador para eliminar 
    el ruido de fondo, dejando solo los rebotes de la pelota.\n
    Utilizando Python y librerías externas: 
    - **“numpy”** para transformar el audio en un arreglo de enteros. 
    - **scipy.signal.find_peaks** para encontrar los “picos” de sonido en el arreglo
    cuánto más alto era un número, mayor era el pico, que interpretamos como
    el choque de la pelota con el suelo, guardándolo en un archivo formato .csv. \n
    Con los datos obtenidos, calculamos el coeficiente de restitución para cada rebote y
    luego promediamos esos valores para obtener el valor promedio.\n
    A continuación, se muestra la tabla de sonido con los picos mencionados anteriormente:
    """
    st.markdown(texto3)
    # Grafico de sonido:
    # https://github.com/Chicago-Fisicos/proyecto-fisica/blob/main/src/audios/graficos/grafico_picos.png

    graf_audio=' https://github.com/Chicago-Fisicos/proyecto-fisica/blob/main/src/audios/graficos/grafico_picos.png?raw=true'
    # Solicitar la imagen desde la URL
    response = requests.get(graf_audio)
    img = Image.open(BytesIO(response.content))

    # Mostrar la imagen en Streamlit
    st.image(img, caption='Picos sonido', use_column_width=True)

    st.markdown("## Calculos y resultados: \n")

    texto_cyr="""
        Dividimos los cálculos en dos partes: \n
        El primer rebote desde que soltamos la pelota desde nuestra altura de referencia, y 
        los rebotes sucesivos hasta que la pelota se detiene.\n
        Nos basaremos en los siguientes conceptos:
    """

    st.markdown(texto_cyr)
    # Descripciones
    st.write("Ccr = coeficiente de restitución")
    st.write("V = velocidad antes del impacto")
    st.write("V' = velocidad después del impacto")

    # Fórmula
    st.latex(r"C_{cr} = -\frac{V'_{\text{pelota}} - V'_{\text{suelo}}}{V_{\text{pelota}} - V_{\text{suelo}}}")
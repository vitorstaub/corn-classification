from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai
from os import getenv
from dotenv import load_dotenv
import PIL.Image
from utils.training import *

def load_gemini() -> None:
    load_dotenv(override=True)
    genai.configure(api_key=getenv("API_KEY"))
    
MODEL_NAME = "gemini-1.5-pro-latest"

GENERATION_CONFIG = {
  "temperature": 0.5  ,
}
    
def setup_model() -> genai.GenerativeModel:
  return genai.GenerativeModel(
      model_name='gemini-1.0-pro-vision-latest',
      generation_config=GENERATION_CONFIG,
)

def load_steamlit_header() -> None:
    st.set_page_config(
        page_title="Corn Classification",
        page_icon="🌽",
        layout="centered",
        initial_sidebar_state="collapsed"
    )

    st.markdown('### Classificação de doenças foliares na cultura do milho 🌽')
    st.markdown('Atualmente podemos identificar as seguintes doenças:')
    st.markdown('* Mancha Branca')
    st.markdown('* Ferrugem Comum')
    st.markdown('* Cercosporiose (Cercospora zeae-maydis)')
    st.markdown('[**Saiba mais sobre as doenças**](https://www.embrapa.br/agencia-de-informacao-tecnologica/cultivos/milho/producao/pragas-e-doencas/doencas/doencas-foliares)')

    st.divider()
    st.markdown('Envie uma imagem de uma folha de milho para ser analizada')
    st.markdown('🔽🔽🔽')
    
def role_to_streamlit(role):
  if role == "model":
    return "assistant"
  else:
    return role
    
def main() -> None:
  load_gemini()
  model = setup_model()
  input_image = ''

  # Page setup.    
  load_steamlit_header()

  # Accept user's next message, add to context, resubmit context to Gemini and show the received response.
  if (uploaded_file := st.file_uploader("Envie uma imagem", type=["png", "jpg"])) is not None:
    # Display uploaded image
    input_image = PIL.Image.open(uploaded_file)
    st.image(input_image, caption="Imagem enviada", use_column_width='auto')
       
    image_paths = [
      './utils/content/img0-cescosporiose.png',
      './utils/content/img1-mancha-branca.jpg',
      './utils/content/img2-ferrugem.jpg',
      './utils/content/img3-cescosporiose.png',
      './utils/content/img4-ferrugem.png',
      './utils/content/img5-mancha-branca.png',
      './utils/content/img6-not.jpg',
      './utils/content/img7-not.jpg'
  ]

    img = [PIL.Image.open(path) for path in image_paths]
    
    prompt_parts = [
      "Você é um modelo de reconhecimento de doenças do milho, com base nos exemplos. o usuário vai mandar uma imagem e você irá retornar o tipo de doença analisando os detalhes da imagem. O output só pode ser de doenças mostradas nos exemplos que são: Cercosporiose do milho, Mancha branca, Ferrugem Comum.",
      "input: Qual a doença dessa folha de milho?",
      img[0],
      "output: Cercosporiose (Cercospora zeae-maydis):\n\nSintomas: \n\nOs sintomas caracterizam-se por manchas de coloração cinza, predominantemente retangulares, com as lesões desenvolvendo-se paralelas às nervuras. Com o desenvolvimento dos sintomas da doença, pode ocorrer necrose de todo o tecido foliar. Em situações de ataques mais severos, as plantas tornam-se mais predispostas às infecções por patógenos no colmo, resultando em maior incidência de acamamento de plantas.",
      "input: Qual a doença dessa folha de milho?",
      img[1],
      "output: Mancha branca:\n\nAs lesões da mancha branca são, inicialmente, circulares, aquosas e verde claras (anasarcas). Posteriormente, passam a necróticas, de cor palha, circulares a elípticas, com diâmetro variando de 0,3 cm a 1 cm. Geralmente, são encontradas dispersas no limbo foliar, mas iniciam-se na ponta da folha progredindo para a base, podendo coalescer. Em geral, os sintomas aparecem inicialmente nas folhas inferiores, progredindo rapidamente para as superiores, sendo mais severos após o pendoamento. Sob condições de ataque severo, os sintomas da doença podem ser observados também na palha da espiga. Em condições de campo, os sintomas não ocorrem, normalmente, em plântulas de milho.",
      "input: Qual a doença dessa folha de milho?",
      img[2],
      "output: Ferrugem Comum:\n\nA ferrugem comum caracteriza-se pela formação de pústulas em toda a parte aérea da planta, mas com maior abundância nas folhas. As pústulas ocorrem em ambas as superfícies da folha, sendo esta uma das características que a diferencia da ferrugem polissora, cujas pústulas predominam na superfície superior da folha. As pústulas da ferrugem comum apresentam formato circular a alongado e coloração castanho clara a escuro, que se acentua à medida em que as pústulas amadurecem e se rompem, liberando os uredósporos, que são os esporos típicos do patógeno. Sob condições ambientais favoráveis, as pústulas podem coalescer, formando grandes áreas necróticas nas folhas.",
      "input: Qual a doença dessa folha de milho?",
      img[3],
      "output: Cercosporiose (Cercospora zeae-maydis):\n\nSintomas: \n\nOs sintomas caracterizam-se por manchas de coloração cinza, predominantemente retangulares, com as lesões desenvolvendo-se paralelas às nervuras. Com o desenvolvimento dos sintomas da doença, pode ocorrer necrose de todo o tecido foliar. Em situações de ataques mais severos, as plantas tornam-se mais predispostas às infecções por patógenos no colmo, resultando em maior incidência de acamamento de plantas.",
      "input: Qual a doença dessa folha de milho?",
      img[4],
      "output: Ferrugem Comum:\n\nA ferrugem comum caracteriza-se pela formação de pústulas em toda a parte aérea da planta, mas com maior abundância nas folhas. As pústulas ocorrem em ambas as superfícies da folha, sendo esta uma das características que a diferencia da ferrugem polissora, cujas pústulas predominam na superfície superior da folha. As pústulas da ferrugem comum apresentam formato circular a alongado e coloração castanho clara a escuro, que se acentua à medida em que as pústulas amadurecem e se rompem, liberando os uredósporos, que são os esporos típicos do patógeno. Sob condições ambientais favoráveis, as pústulas podem coalescer, formando grandes áreas necróticas nas folhas.",
      "input: Qual a doença dessa folha de milho?",
      img[5],
      "output: Mancha branca:\n\nAs lesões da mancha branca são, inicialmente, circulares, aquosas e verde claras (anasarcas). Posteriormente, passam a necróticas, de cor palha, circulares a elípticas, com diâmetro variando de 0,3 cm a 1 cm. Geralmente, são encontradas dispersas no limbo foliar, mas iniciam-se na ponta da folha progredindo para a base, podendo coalescer. Em geral, os sintomas aparecem inicialmente nas folhas inferiores, progredindo rapidamente para as superiores, sendo mais severos após o pendoamento. Sob condições de ataque severo, os sintomas da doença podem ser observados também na palha da espiga. Em condições de campo, os sintomas não ocorrem, normalmente, em plântulas de milho.",
      "input: Qual a doença dessa folha de milho?",
      img[6],
      "output: Folha de milho saudavel",
      "input: Qual a doença dessa folha de milho?",
      img[7],
      "output: Folha de milho saudavel",
      "input: Qual a doença dessa folha de milho?",
      input_image,
      "output: ",
  ]

    # Make prediction with the model
    response = model.generate_content(prompt_parts)
    st.markdown(response.text)

if __name__ == "__main__":
    main()
import gradio as gr
from rembg import remove

def segment(image):
     return remove(image)
     
demo = gr.Interface(fn=segment, inputs = gr.Image(label="Input Image", interactive=True), outputs = gr.Image(label="Result Image"), description = "  ", theme = gr.themes.Base(primary_hue="teal",secondary_hue="teal",neutral_hue="slate"))
demo.launch(show_api=False)
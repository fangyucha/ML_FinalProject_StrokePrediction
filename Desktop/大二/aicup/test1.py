import gradio as gr
#輸入文書處理程式
def greet(name):
    return "Hello " + name + "!"
#介面建立函數
#fn設定處理常式，inputs設定輸入介面元件，outputs設定輸出介面元件
#fn,inputs,outputs都是必填函數
demo = gr.Interface(fn=greet, inputs="text", outputs="text")
demo.launch()
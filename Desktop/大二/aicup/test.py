import openai
import gradio as gr
import gradio as component
#openai.api_key = ""
#openai.api_key = ""
openai.api_key = "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"

messages = [
	{"role": "system", "content": "Counting his current word count and warn  if it is less that 500 words."},
	{"role": "system", "content": "Using traditional chinese to warning and response."},
	# {"role": "system", "content": "Giving some feedback on user content."},
]

def chatbot(input):
	if input:
		messages.append({"role": "user", "content": input})
		chat = openai.ChatCompletion.create(
			model="gpt-3.5-turbo", messages=messages
		)

		reply = chat.choices[0].message.content
		messages.append({"role": "assistant", "content": reply})

		return reply

input = gr.Textbox(lines=7, label="Chat with AI")
output = gr.Textbox(label="Reply")

gr.Interface(fn=chatbot, inputs=input, outputs=output, title="報告檢核系統", description="請在此輸入要檢測的報告段落", theme="compact").launch(share=True)
#compact

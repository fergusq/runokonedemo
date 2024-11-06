import datetime
from typing import Callable, Any

import rich, rich.console, rich.panel, rich.markdown, rich.live, rich.text, rich.prompt
console = rich.console.Console()

from llama_cpp import Llama

llm = Llama(
	model_path="./Ahma-3B-Instruct.Q6_K.gguf",
	chat_format="oma"
)

def generate(prompt: str):
	while True:
		#try:
			with console.status("Odotetaan palvelinta..."):
				stream: Any = llm(
					prompt,
					stop=["Käyttäjä:", "\n\n"],
					stream=True,
					repeat_penalty=1.18,
					max_tokens=400
				)
			
				yield "ok"
			break
			
	for chunk in stream:
		yield chunk["choices"][0].get("text") or ""



def add_newlines(line: str):
	lines = []
	while len(line) >= 32:
		left = line
		right = ""
		while len(left) >= 32 and " " in left:
			i = left.rindex(" ")
			right = left[i:] + right
			left = left[:i]

		if right == "":
			break

		lines.append(left)
		line = right

	return "\n".join(lines + [line])


def printer_print(text: str, **kwargs):
	for line in text.splitlines():
		line = add_newlines(line)
		print(line, **kwargs)


def printer_print_columns(text1: str, text2: str, **kwargs):
	spaces = " "*(31-len(text1)-len(text2))
	printer_print(f"{text1}{spaces}{text2}", **kwargs)

PROMPT = """Käyttäjä: Kirjoita ylevä runo aiheesta {}. Tiivistä runo yhteen säkeistöön.\n\nTekoäly: Tässä on runosi:\n\n"""
NAME_LEFT = "Järjestön nimi"
NAME_RIGHT = "Tapahtuman nimi"

n = 1
while True:
	import os, traceback
	os.system("clear")

	console.rule("Tekoälyn runot")
	user_input = rich.prompt.Prompt.ask("Anna runolle aihe tai kirjoitusohjeet")
	generation = ""
	text = rich.text.Text()
	panel = rich.panel.Panel.fit(text)
	generator = generate(PROMPT.format(user_input))
	next(generator)
	try:
		with rich.live.Live(panel, refresh_per_second=8):
			for token in generator:
				if generation == "":
					token = token.lstrip()
				generation += token
				text.append(token)

	except:
		traceback.print_exc()
		console.print("[bold red]\\[Virhe generoinnin aikana]")

	if rich.prompt.Confirm.ask("Tulostetaanko runo?"):
		with open("/tmp/tulostin", "w") as f:
			today = datetime.date.today()
			printer_print_columns(NAME_LEFT, NAME_RIGHT, file=f)
			printer_print_columns("Runo nro", str(n), file=f)
			printer_print_columns("Päivämäärä", f"{today.day}.{today.month}.{today.year}", file=f)
			printer_print("\n", file=f)

			printer_print(user_input, file=f)
			printer_print("\n", file=f)
			printer_print(generation, file=f)
			printer_print("\n", file=f)

	rich.prompt.Prompt.ask("Paina enteriä jatkaaksesi")
	n += 1

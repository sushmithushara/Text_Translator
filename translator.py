from translate import Translator
translator= Translator(to_lang="ja")
try:
	with open('./sample_translator.txt',mode ='r',encoding ='utf-8') as my_file:
		text = my_file.read()
		translation = translator.translate(text)
		print(translation)
except FileNotFoundError as e:
		print("Your file is not found")
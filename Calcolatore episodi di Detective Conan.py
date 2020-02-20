Numero = input("Inserisci il numero dell'episodio: ")
NumeroEp = str(Numero)
url = input("Inserusci l'URL dell'episodio (Wstream): ")
Titolo = input("Inserisci il titolo dell'episodio: ")
Codice = "if($msg == "+NumeroEp+")\n\n\n\n\n{  $menua = '[[{\"text\": \" Wstream \", \"url\": "+url+"\"\}\]\]';\n\n\n\n\n  $mess = \""+Titolo+"\";\n  itastiera($chatID, $mess, $menua,$ticket);\n}\n{"
print(Codice)

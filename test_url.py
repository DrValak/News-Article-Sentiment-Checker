import requests 
from bs4 import BeautifulSoup

url = "https://www.rtp.pt/noticias/mundo/guerra-no-medio-oriente-a-evolucao-do-conflito-entre-israel-e-irao_e1663864" 
response = requests.get(url) # Check if the URL is reachable
soup = BeautifulSoup(response.text, 'html.parser') # Parse the HTML content

for script in soup(["script", "style", "nav", "footer", "header"]): # Remove all script and style elements
    script.decompose()

paragraphs = soup.find_all('p') # Find all paragraph elements
clean_text = ' '.join([p.get_text() for p in paragraphs]) # Join all paragraph texts into a single string

# Portuguese stop words and positive/negative words
stop_words = ["de", "a", "o", "e", "do", "da", "em", "para", "com", "que", "é", "um", "uma", "os", "as", "no", "na", "por", "mais", "foi", "como", "são", "ao", "dos", "das"]
positive_words = ["bom", "ótimo", "excelente", "sucesso", "vitória", "feliz", "positivo", "melhor", "crescimento", "ganhar", "paz", "acordo", "progresso", "esperança", "solução"]
negative_words = ["mau", "péssimo", "terrível", "fracasso", "derrota", "triste", "negativo", "pior", "crise", "perder", "guerra", "conflito", "ataque", "violência", "morte", "destruição"]

words = clean_text.split()
filter_words = [word for word in words if word.lower() not in stop_words]

positive_counter = 0
negative_counter = 0

for words in filter_words: # Count positive and negative words 
    if words.lower() in positive_words:
        positive_counter += 1
    elif words.lower() in negative_words:
        negative_counter += 1

print(f'Positive words: {positive_counter}')
print(f'Negative words: {negative_counter}')

if positive_counter > negative_counter:
    print("The article has a more POSITIVE tone")
elif negative_counter > positive_counter:
    print("The article has a more NEGATIVE tone")
else:
    print("The article has a NEUTRAL tone")
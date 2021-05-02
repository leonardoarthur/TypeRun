import requests
import random
import time

url = 'https://www.mit.edu/~ecprice/wordlist.10000'

resposta = requests.get(url)
palavras = resposta.content.splitlines()

palavras = [palavra.decode('utf-8') for palavra in palavras]

random_palavras = random.sample(palavras, 10)

pontos = 0
tic = time.perf_counter()
for palavras in random_palavras:
  print(palavras)
  entrada = input()
  if entrada == palavras:
    pontos = pontos + 1

toc = time.perf_counter()
print('Sua pontuação foi', pontos)
print('Seu tempo foi', toc - tic)
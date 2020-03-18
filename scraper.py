#import bibliotek
import requests
from bs4 import BeautifulSoup 
# def adres strony z opiniami
url = "https://www.ceneo.pl/76891701#tab=reviews"

# pobieranie kodu HTMl strony z adresu URL
page_response = requests.get(url)
page_tree = BeautifulSoup(page_response.text,"html.parser")

# wybranie z kodu strony fragmentów odpowiadajacych poszczegolnym opiniom
opinions = page_tree.select("li.review-box")

for opinion in opinions:
    opinion_id = opinion["data-entry-id"]
    # print(opinion_id)
    author = opinion.select('div.reviever-name-line').pop().string.strip()
    try:
        recomendation = opinion.select('div.product-reviever-summary').pop().string.strip()
    except IndexError:
        recomendation = None
    stars = opinion.select('span.review-score-count').pop().string.strip()
    try:
        purchased = opinion.select('div.product-review-pz').pop().string.strip()
    except IndexError:
        purchased = None
    useful = opinion.select('button.vote-yes').pop()['data-total-vote'] 
    useless = opinion.select('button.vote-no').pop()['data-total-vote'] 
    content = opinion.select('p.product-review-body').pop().get_text().strip()
    try:
        cons = opinion.select['div.cons-cell > ul'].pop().get_text().strip()
    except IndexError:
        cons = None
    try:
        pros = opinion.select['div.pros-cell > ul'].pop().get_text().strip()
    except IndexError:
        cons = None
    date = opinion.select('span.reviev-time > time')
    review_date = date.pop(0)["datetime"]
    try:
        purchase_date = date.pop(0)["datetime"]
    except IndexError:
        purchase_date = None
    # print(opinion_id, author, recomendation, stars, content, pros, cons, useful, useless, purchased, purchase_date, review_date)
import bs4
import requests

def getAmazonPrice(productUrl):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    }    
    res = requests.get(productUrl, headers=headers)
    res.raise_for_status()


    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#priceblock_ourprice')
    print(elems)
    return elems[0].text.strip()


price = getAmazonPrice('https://www.amazon.com/dp/B075RNKT6G/?coliid=IS7YSA96E6FF7&colid=8P5TOKF8CR5&psc=1&ref_=lv_ov_lig_dp_it')
print('The price is ' + price)
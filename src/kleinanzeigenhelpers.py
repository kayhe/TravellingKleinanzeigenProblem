import mechanicalsoup

def get_listings_page(keywords, postcode, radius=0):
    browser = mechanicalsoup.StatefulBrowser()
    browser.open("https://www.ebay-kleinanzeigen.de")
    browser.select_form('form[id="site-search-form"]')
    browser['keywords'] = keywords
    browser['locationStr'] = postcode
    browser['radius'] = str(radius)
    
    res = browser.submit_selected()
    return res

def extract_items(page):
    items = [] 
    for item in page.soup.find_all('article'):
        title = item.a.text
        url = 'https://www.ebay-kleinanzeigen.de' + item.a.attrs['href']
        price = item.strong.text
        items.append({'title' : title, 'url' : url, 'price' : price})

    return items

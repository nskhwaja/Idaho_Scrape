# Import Libraries
import bs4 
import requests

def import_pharmacists(pharma_lname):
    if pharma_lname == 'L': #specifing the variable to filter to
        page = requests.get('https://idbop.mylicense.com/verification/SearchResults.aspx')
    elif pharma_lname == 'l': #if the last name came out lowercae
        page = requests.get('https://idbop.mylicense.com/verification/SearchResults.aspx')
    else:
        logger.error("Invalid Pharma_LName: " + pharma_lname)
        return None #if a null is returned

    # html parse
    soup = bs4.BeautifulSoup(page.content, 'html.parser')

    # Grab only table elements
    all_soup = soup.find_all('table')

    # Get table elements
    for element in all_soup:        
        listing = str(element)

        if 'https://idbop.mylicense.com/verification/SearchResults.aspx' in listing:   

            # Stuff the results in a pandas df
            data = pd.read_html(listing)

    return data

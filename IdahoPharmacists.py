# Import Libraries
import bs4 
import requests

def import_pharmacists(pharma_lname):
    if pharma_lname == 'L':
        page = requests.get('https://idbop.mylicense.com/verification/SearchResults.aspx')
    elif pharma_lname == 'l':
        page = requests.get('https://idbop.mylicense.com/verification/SearchResults.aspx')
    else:
        logger.error("Invalid Pharma_LName: " + pharma_lname)
        return None

    # Parse the HTML Page
    soup = bs4.BeautifulSoup(page.content, 'html.parser')

    # Grab only table elements
    all_soup = soup.find_all('table')

    # Get what you want from table elements!
    for element in all_soup:        
        listing = str(element)

        if 'https://idbop.mylicense.com/verification/SearchResults.aspx' in listing:   

            # Stuff the results in a pandas data frame (if your not using these you should)
            data = pd.read_html(listing)

    return data

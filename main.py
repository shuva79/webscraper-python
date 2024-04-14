from bs4 import BeautifulSoup 

# This is not the actual program, I am just practicing this
# Program that pulls actual website data is in the other python file

# with open reads files and the 'r' is the read mode and stored in html_file
with open('home.html', 'r') as html_file:
    content = html_file.read()
    
    # BeautifulSoup pulls the data from the file home.html stored in content
    # 'lxml' is used for parsing data according to our use case
    soup = BeautifulSoup(content, 'lxml')

    # find_all lists all the occurrences that we require
    # Alternatively, if we only need the first occurrence of the data, use find instead

    # The '_' is used alone with class because class is already built into python and
    # we need to pull all the data which is included in the 'numeric' class 
    price = soup.find_all('div', class_ = "numeric") 

    # Price being an array, we are parsing the data and showing it in a more readable format
    
    for prices in price:
        share_price = prices.td.text

        print(f'Share price: {share_price}')

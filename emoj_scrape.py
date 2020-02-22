from bs4 import BeautifulSoup as soup
from requests import get

url = 'https://unicode.org/emoji/charts/full-emoji-list.html'

def get_data(url_source):
    response = get(url_source)
    html_soup = soup(response.text, 'html.parser')
    
    #Get the fields container 
    code_containers = html_soup.table.find_all("td",class_ = 'code')
    name_containers = html_soup.table.find_all("td",class_ = 'name')
    #rchars_container = html_soup.table.find_all("td",class_ = 'rchars')   
    
    #Create a dictionary to hold the data
    emoj_dict = dict()
    
    #Propagate the emoj data to dictionary
    for emoj in range(len(code_containers)):
        #Get fields' data
        emoj_name = name_containers[emoj].text
        emoj_code = code_containers[emoj].text
        #emoj_rchars = rchars_container[emoj].text
        emoj_dict[emoj_code] = emoj_name
    #Done creating the dictionary
    

#import the pandas library and aliasing as pd
import pandas as pd

#convert dictionary to dataframe
data = emoj_dict
df = pd.DataFrame(list(data.items()), columns=['Emoj Code', 'Emoj Name'])
df.to_csv (r'D:\kingsoft\emoj_dataframe.csv', index = None, header=True) #Don't forget to add '.csv' at the end of the path


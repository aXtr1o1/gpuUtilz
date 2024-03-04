import pprint
from colorama import Fore, Style
from tqdm import tqdm
from tabulate import tabulate
from bs4 import BeautifulSoup
import requests

webpage = requests.get('https://en.wikipedia.org/wiki/CUDA')

cuda_table = BeautifulSoup(webpage.text,'html.parser')
table_contents = cuda_table.find_all("table",class_="wikitable")
if len(table_contents) > 2:
    print("/////\n\n")
    pprint.pprint(table_contents[1])
    print("\n\n/////")







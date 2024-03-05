from pprint import pprint
from colorama import Fore, Style
from tqdm import tqdm
from tabulate import tabulate
from bs4 import BeautifulSoup
import requests
import csv

webpage = requests.get('https://en.wikipedia.org/wiki/CUDA')

cuda_table = BeautifulSoup(webpage.text,'html.parser')
table_contents = cuda_table.find_all("table",class_="wikitable")

compute_compatibility = table_contents[1]
Nvidia_GPU_BoardProducts = table_contents[2]

pprint(compute_compatibility)
print("\n\n\n\n\n")
pprint(Nvidia_GPU_BoardProducts)
print(type(cuda_table))
print(type(table_contents))

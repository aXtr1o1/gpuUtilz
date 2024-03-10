from pprint import pprint
from lxml import etree
from colorama import Fore, Style
from tqdm import tqdm
from tabulate import tabulate
from bs4 import BeautifulSoup
import requests
import csv

wiki_webpage = requests.get('https://en.wikipedia.org/wiki/CUDA')
cudnn_archive = requests.get("https://developer.nvidia.com/rdp/cudnn-archive")

cudnn_list = BeautifulSoup(cudnn_archive.text,'html.parser')
list_contents = cudnn_list.find("div",class_="panel-group")
a_tag_list = [a.get_text(strip=True) for a in list_contents.find_all('a')]
print(a_tag_list)


cuda_table = BeautifulSoup(wiki_webpage.text,'html.parser')
table_contents = cuda_table.find_all("table",class_="wikitable")

compute_compatibility = table_contents[1]
Nvidia_GPU_BoardProducts = table_contents[2]

text=""
table=Nvidia_GPU_BoardProducts.find_all('tr')
table=table[1:]
key= [x.find('td').text.strip() for x in table if x.find('td')]
val=[]
for x in table:
    if x.find('td'):
        row_vals = []
        for td in x.find_all('td'):
            row_vals.append(td.text.strip())
        val.append(row_vals[1:])


with open('Cuda_version.txt','w') as f:
    f.write("\tCuda Version Bruh\t")
    for i in range(len(key)):
        text=str(key[i])+"\t:\t"+str(val[i])+"\n"
        f.write(text)
print("Success")

# print(val)
# pprint(compute_compatibility)
# print("\n\n\n\n\n")
# pprint(Nvidia_GPU_BoardProducts)
# print(type(cuda_table))
# print(type(table_contents))

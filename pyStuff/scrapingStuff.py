from colorama import Fore, Style
from tqdm import tqdm
from pprint import pprint
from tabulate import tabulate
from bs4 import BeautifulSoup
import requests
import csv

cudnn_archive = requests.get("https://developer.nvidia.com/rdp/cudnn-archive")

cudnn_list = BeautifulSoup(cudnn_archive.text,'html.parser')
list_contents = cudnn_list.find("div",class_="panel-group")
a_tag_list = [a.get_text(strip=True) for a in list_contents.find_all('a') if a.get_text(strip=True).startswith("Download") ]

#Prettyfying the raw scraped ugly data#
cudnn_archive_list =[]
for item in a_tag_list:
    cudnn_text = str(item)+"\t"+'\n'
    cudnn_archive_list.append(cudnn_text)
cudnn_contents = [x.split("for") for x in cudnn_archive_list]
cudnn_contents = [[sublist.replace('\n','').replace('\t','') for sublist in megalist] for megalist in cudnn_contents]

#Adding the Waterwashed data in a CSV file#
with open("CSV_Files/cuDNN_CUDA_Version_Compatibility.csv",'w') as cudnn_csv:
    header = ['cuDNN Version','CUDA Version']
    data = csv.writer(cudnn_csv)
    data.writerow(header)
    data.writerows(cudnn_contents)

# CUDA Version Scraping From WikiPedia
wiki_webpage = requests.get('https://en.wikipedia.org/wiki/CUDA')
cuda_table = BeautifulSoup(wiki_webpage.text,'html.parser')
table_contents = cuda_table.find_all("table",class_="wikitable")
compute_compatibility = table_contents[1]

#Scraping RAW data from Wikipedia Table 
table_rows = compute_compatibility.find_all('tr')
i=0
header_row = [table_rows[i + index].text.strip() for index, _ in enumerate(table_rows)]

#Prettifying the Compute Compatibility Table
compatibility_list = []
for i in range(len(header_row)):
    compatibility_list.append(header_row[i].strip().split('\n'))
compatibility_list = [[item.split('[')[0] for item in sublist] for sublist in compatibility_list]
for i in compatibility_list:
    elements_to_add = 13 - len(i)
    i.extend(['']*elements_to_add)

#Adding the Scraped out compatibility data in a CSV file
with open("CSV_Files/CUDA_Compute_Compatibility-CUDA SDK support vs Microarchitechture.csv",'w') as compat_csv:
    compat_data = csv.writer(compat_csv)
    compat_data.writerow([compute_compatibility.find('caption').text])
    compat_data.writerows(compatibility_list)

# Nvidia GPU BoardProducts From Wikipedia
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


# Prettyfying the RAW Scrapped Data Nvidia Board Compatibility      
Board_compt = []
for i in range(len(key)):
        value=[x for x in val[i] if x !='']
        value = [x.replace('\xa0K1','').replace('\xa0TX1','').replace('\xa0','') if '\xa0K1' in x or '\xa0TX1' in x or '\xa0' in x  else x   for x in value]
        text=[key[i],value]
        Board_compt.append(text)

# Writing Down the Scrapped Data into a CSV File
with open('CSV_Files/Nvidia_GPU_Board_Compatibility.csv','w') as bcomp:
    bcomp_data = csv.writer(bcomp)
    bcomp_data.writerow(['Compute Capability (version)','Nvidia GPU Board'])
    bcomp_data.writerows(Board_compt)



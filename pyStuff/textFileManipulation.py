from pprint import pprint
with open("Cuda_Version.txt",'r') as cudafile:
    contents = cudafile.readlines()

# print('\n\n\n\n\n')

with open("CUDNN_Version.txt",'r') as cudnnFile:
    cdncontents = cudnnFile.readlines()
    # print(cdncontents)

for i in range(len(contents)):
    print(contents[i],'\n')
print('\n')
pprint(cdncontents)

print('\n\n')
print(type(contents))
print(type(cdncontents))
print('\n')
print(len(contents))
print(len(cdncontents))
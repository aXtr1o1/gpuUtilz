with open("Cuda_Version.txt",'r') as cudafile:
    contents = cudafile.readlines()
    # print(contents,'\n')

# print('\n\n\n\n\n')

with open("CUDNN_Version.txt",'r') as cudnnFile:
    cdncontents = cudnnFile.readlines()
    # print(cdncontents)
print(type(contents))
print(list(cudnnFile))


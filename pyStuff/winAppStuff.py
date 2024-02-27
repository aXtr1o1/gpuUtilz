from colorama import Fore, Style
from tabulate import tabulate
from tqdm import tqdm
import GPUtil

GPUs = GPUtil.getGPUs()
GPUlist = []
for i in tqdm(GPUs, desc = "Flowin' throuogh the GPUs Yo!", colour = 'red'):
    gpuId = i.id
    gpuName = i.name
    gpuLoad = f"{i.load*100}%"
    gpuFreeMemory = f"{i.memoryFree}MB"
    gpuUsedMemory = f"{i.memoryUsed}MB"
    gpuTotalMemory = f"{i.memoryTotal}MB"
    gpuTemperature = f"{i.temperature} °C"
    gpuUUid = i.uuid
    GPUlist.append((
        gpuId, gpuName, gpuLoad, gpuFreeMemory, gpuUsedMemory,
        gpuTotalMemory, gpuTemperature, gpuUUid
    ))

print(Fore.BLUE+Style.BRIGHT+"\n\nGPUstuff Yo !"+Fore.RESET)
print(tabulate(GPUlist, headers=("id", "name", "load", "free memory", "used memory", "total memory",
                                   "temperature", "uuid")))
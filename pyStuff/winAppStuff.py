import kivy 
import GPUtil
kivy.require("2.3.0")
from tqdm import tqdm
from kivy.app import App 
from kivy.uix.label import Label
import tabulate
from colorama import Fore, Style

class Labapp(App):
    def build(self):
        Gpus=GPUtil.getGPUs()
        if Gpus:
            Gpu_list=[]
            for i in tqdm(Gpus, desc="Flowin' through the GPUs Yo!", colour='red'):
                gpuId = i.id
                gpuName = i.name
                gpuLoad = f"{i.load*100}%"
                gpuFreeMemory = f"{i.memoryFree}MB"
                gpuUsedMemory = f"{i.memoryUsed}MB"
                gpuTotalMemory = f"{i.memoryTotal}MB"
                gpuTemperature = f"{i.temperature} °C"
                gpuUUid = i.uuid
                Gpu_list.append((
                    gpuId, gpuName, gpuLoad, gpuFreeMemory, gpuUsedMemory,
                    gpuTotalMemory, gpuTemperature, gpuUUid
                ))
            output = f"{Fore.BLUE+Style.BRIGHT}\n\nGPUstuff Yo !{Fore.RESET}\n"
            output += tabulate(Gpu_list, headers=("id", "name", "load", "free memory", "used memory", "total memory",
                                              "temperature", "uuid"))
            
            lab=Label(text=output,color="red")
            return lab
        else:
            lab=Label(text="No Details About GPU  404 Error",color="red")
            return lab

label=Labapp()
label.run()
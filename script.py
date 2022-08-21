from functions import area,pc
from pyodide import create_proxy

def calc(event):
    input1 = document.getElementById('Iterable').value
    input1 = input1.split(",")
    input2 = document.getElementById('Length').value
    
    pyscript.write("result",pc(input1,int(input2)))
        

proxy = create_proxy(calc)
btn = document.getElementById('clacB')
btn.addEventListener("click",proxy)
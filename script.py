from xml.dom.minidom import Document
from functions import area,pc
from pyodide import create_proxy

def calc(event):
    # get inputs
    input1 = document.getElementById('Iterable').value
    input1 = input1.split(",")
    input2 = document.getElementById('Length').value
    # get run time div
    div_runtime = document.getElementById('on_runtime')

    try:
        input2 = int(input2)
        if not(input2>0):
            # input error
            raise ValueError("Input Error")
        # result
        pyscript.write("result",pc(input1,input2))

        # show run time div
        div_runtime.style.display = "block"

    except ValueError:
        # input error
        pyscript.write("result","Input Error")
        # hide run time div
        div_runtime.style.display = "none"


        
proxy = create_proxy(calc)
btn = document.getElementById('clacB')
btn.addEventListener("click",proxy)
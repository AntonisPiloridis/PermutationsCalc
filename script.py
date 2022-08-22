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

    except MemoryError:
        # memory error
        pyscript.write("result","Memory Error")
        # hide run time div
        div_runtime.style.display = "none"

    except Exception as e:
        # other error
        pyscript.write("result",e)
        # hide run time div
        div_runtime.style.display = "none"


def reset(event):
    pyscript.write("result","")
    div_runtime = document.getElementById('on_runtime')
    div_runtime.style.display = "none"


        
proxy = create_proxy(calc)
btn = document.getElementById('clacB')
btn.addEventListener("click",proxy)

proxy2 = create_proxy(reset)
btn2 = document.getElementById('clB')
btn2.addEventListener("click",proxy2)

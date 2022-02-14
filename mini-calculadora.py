from cProfile import label
from ctypes import alignment
import tkinter as tk
from unittest import result

frame = tk.Tk();
frame.title("exemplo viadao kk");
frame.geometry('400x200');

lbl1 = tk.Label(frame, text="digite o primeiro número: ");
lbl1.pack();
inputtt = tk.Text(frame, height=1, width=20); 
inputtt.pack();

lbl3 = tk.Label(frame, text="digite o segundo número: ");
lbl3.pack();
inputtt2 = tk.Text(frame, height=1, width=20);
inputtt2.pack();


lbl2 = tk.Label(frame, text="");
lbl4 = tk.Label(frame, text="");
lbl5 = tk.Label(frame, text="");
lbl6 = tk.Label(frame, text="");

def mostrandoInput():
    inp = inputtt.get(1.0, "end-1c");
    inp2 = inputtt2.get(1.0, "end-1c");
    resultado1 = int(inp) + int(inp2);
    lbl2.config(text="a soma de: "+str(inp)+" + "+str(inp2)+" é: "+str(resultado1));
    resultado2 = int(inp) - int(inp2);
    lbl4.config(text="a subtração de: "+str(inp)+" - "+str(inp2)+" é: "+str(resultado2));
    resultado3 = int(inp) / int(inp2);
    lbl5.config(text="a divisão entre: "+str(inp)+" / "+str(inp2)+" é: "+str(resultado3));
    resultado4 = int(inp) * int(inp2);
    lbl6.config(text="a multiplicação entre: "+str(inp)+" * "+str(inp2)+" é: "+str(resultado4));


buttonnn = tk.Button(frame, text="let's go", command=mostrandoInput);

inputtt.pack();
buttonnn.pack();
lbl2.pack();
lbl4.pack();
lbl5.pack();
lbl6.pack();
frame.mainloop();
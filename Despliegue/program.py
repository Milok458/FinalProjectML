import tkinter as tk
import math
from tkinter import messagebox
from joblib import load
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier

model = load('NeuralNet.joblib')

sc = load('Scaler.joblib')


def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()


def predict():

    try:
        vmag = float(entry1.get())
        plx = float(entry2.get())
        bv = float(entry3.get())
    except ValueError:
        messagebox.showinfo("Error", "All inputs must be float numbers!")
    else:
        amag = vmag + (5 * (math.log(plx, 10) + 1))

        data = [[vmag, plx, bv, amag]]

        data = sc.transform(data)

        pred = model.predict(data)

        label5 = tk.Label(root, text='Your star is of class ' + str(pred[0]))
        label5.config(font=('helvetica', 10))
        canvas1.create_window(200, 260, window=label5)


root = tk.Tk()

root.title('Star Classification')

canvas1 = tk.Canvas(root, width=400, height=400, relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='Enter variables for prediction')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='Vmag:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 75, window=label2)

entry1 = tk.Entry(root)
canvas1.create_window(200, 100, window=entry1)

label3 = tk.Label(root, text='Plx:')
label3.config(font=('helvetica', 10))
canvas1.create_window(200, 125, window=label3)

entry2 = tk.Entry(root)
canvas1.create_window(200, 150, window=entry2)

label4 = tk.Label(root, text='B-V:')
label4.config(font=('helvetica', 10))
canvas1.create_window(200, 175, window=label4)

entry3 = tk.Entry(root)
canvas1.create_window(200, 200, window=entry3)

button1 = tk.Button(text='Predict', bg='red', fg='white',
                    font=('helvetica', 9, 'bold'), command=predict)
canvas1.create_window(200, 310, window=button1)

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()

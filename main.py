from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import time
import timeit


def partition(array, low, high, speed):
    pivot = array[high]

    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:

            i = i + 1
            drawData(array)
            time.sleep(speed)
            (array[i], array[j]) = (array[j], array[i])

    drawData(array)
    time.sleep(speed)

    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1

def quickSort(array, low, high, speed):
    if low < high:

        pi = partition(array, low, high, speed)

        quickSort(array, low, pi - 1, speed)

        quickSort(array, pi + 1, high, speed)

    drawData(array)



def mergeSort(data, left, right, speed):
    if left < right:
        m = (left + right) // 2
        mergeSort(data, left, m, speed)
        mergeSort(data, m + 1, right, speed)

        j = m + 1
        if data[m] <= data[m + 1]:
            return

        while left <= m and j <= right:

            if data[left] <= data[j]:
                left += 1
            else:
                drawData(data)
                time.sleep(speed)

                temp = data[j]
                i = j
                while i != left:
                    data[i] = data[i - 1]

                    drawData(data)
                    time.sleep(speed)

                    i -= 1

                data[left] = temp
                drawData(data)

                time.sleep(speed)
                left += 1
                m += 1
                j += 1




def bubbleSort(data, speed):
    n = len(data)

    for i in range(n):
        for j in range(0, n - i - 1):

            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

                drawData(data)
                time.sleep(speed)

    drawData(data)

def drawData(data):
    canvas.delete('all')
    c_height = 300
    c_width = 600
    x_width = c_width / (len(data) + 1)
    offset = 30
    spacing = 10
    for i, height, in enumerate(data):
        x0 = i * x_width + offset + spacing
        y0 = c_height - height

        x1 = (i +1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill ='red')
        canvas.create_text(x0 + 2, y0, anchor=SW, text = str(data[i]))
        root.update_idletasks()

def Generate():
    if len(size.get()) == 0:
        messagebox.showerror("Błąd", "Podaj rozmiar")
    else:
        datasize = int(size.get())
        global data
        data = [random.randint(0,100) for i in range(datasize)]
        drawData(data)
def Start():
    if len(size.get()) == 0:
        messagebox.showerror("Błąd", "Podaj rozmiar")
    elif len(Speed.get()) == 0:
        messagebox.showerror("Błąd", "Podaj prędkość")
    try: data
    except NameError:
        messagebox.showerror("Błąd", "Brak danych")
    else:
        if selectedAlgorithm.get() == 'Bubble Sort':
            starttime = timeit.default_timer()
            bubbleSort(data[:], float(Speed.get()))
            stoptime = timeit.default_timer()
            Time.set(str(stoptime - starttime))
        elif selectedAlgorithm.get() == 'Merge Sort':
            starttime = timeit.default_timer()
            mergeSort(data[:], 0, len(data) - 1, float(Speed.get()))
            stoptime = timeit.default_timer()
            Time.set(str(stoptime - starttime))

        elif selectedAlgorithm.get() == 'Quick Sort':
            starttime = timeit.default_timer()
            quickSort(data[:], 0, len(data) - 1, float(Speed.get()))
            stoptime = timeit.default_timer()
            Time.set(str(stoptime - starttime))

def Reset():
    try:
        data
    except NameError:
        messagebox.showerror("Błąd", "Brak danych")
    else:
        drawData(data)

root = Tk()
root.title("Algorithm Visualizer")

root.maxsize(900, 600)
root.config(bg="black")

selectedAlgorithm = StringVar()
speedCount = StringVar()
Time = StringVar()

UI_frame = Frame(root, width = 600, height = 200, bg = 'grey')
UI_frame.grid(row = 0, column = 0, padx = 10, pady = 5)

canvas = Canvas(root, width= 600, height= 300, bg = 'white')
canvas.grid(row =1, column = 0, padx =10, pady = 5)

Label(UI_frame, text= 'Algorytm', bg= 'grey').grid(row=0, column = 0, padx = 10, pady = 5, sticky = W)
menu = ttk.Combobox(UI_frame, textvariable= selectedAlgorithm, values=['Bubble Sort',
                                                                    'Merge Sort', 'Quick Sort'])
menu.grid(row = 0, column = 1)
menu.current(0)

Button(UI_frame, text = 'Generuj', bg= 'white', command= Generate).grid(row = 0, column = 2, padx = 10,
                                                                        pady = 5)

Label(UI_frame, text = 'Rozmiar', bg = 'grey').grid(row = 1, column = 0, padx = 10, pady = 5)
size = Entry(UI_frame)
size.grid(row = 1, column = 1, padx = 10, pady = 5, sticky = W)


Button(UI_frame, text = 'Rozpocznij', bg = 'white', command= Start).grid(row = 0, column = 3, padx = 10,
                                                                         pady = 5)

Label(UI_frame, text = 'Prędkość: ', bg = 'grey').grid(row = 1, column = 2, padx = 10,
                                                                    pady = 5)
Speed = Entry(UI_frame, textvariable=speedCount)
Speed.grid(row = 1, column = 3, padx = 5, pady =5, sticky = W)

Label(UI_frame, text = 'Przybliżony czas', bg = 'grey').grid(row = 1, column = 4, padx = 5, pady =10)
estTime = Entry(UI_frame, textvariable=Time, state= DISABLED)
estTime.grid(row = 1, column = 5, padx = 5, pady = 5, sticky = W)

Button(UI_frame, text = 'Resetuj', bg = 'white', command = Reset).grid(row = 0, column = 4 , padx = 10,
                                                                       pady = 5)

root.mainloop()


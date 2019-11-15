import PIL.ImageGrab
import requests,webbrowser
import tkinter as tk
import json
X1 = 0
X2 =0
Y1 = 0
Y2 = 0
def screenshot_search():
    with open('config.json', 'r') as f:
        config = json.load(f)
    im = PIL.ImageGrab.grab(bbox=(config['X1'],config['Y1'],config['X2'],config['Y2']))
    im.save('q.png')
    filePath = 'q.png'
    searchUrl = 'http://www.google.co.in/searchbyimage/upload'
    multipart = {'encoded_image': (filePath, open(filePath, 'rb')), 'image_content': ''}
    response = requests.post(searchUrl, files=multipart, allow_redirects=False)
    fetchUrl = response.headers['Location']
    webbrowser.open(fetchUrl)


def exit_():
    exit()

win = tk.Tk()
win.geometry('190x150')
win.title('FLipkart')

def get_x1_y1():
    global X1,Y1
    X1, Y1 = win.winfo_pointerxy()
    print("X1 :" + str(X1))
    print("Y1:" +str(Y1))

def get_x2_y2():
    global X2,Y2
    X2,Y2 = win.winfo_pointerxy()
    print("X2 :" + str(X2))
    print("Y2:" +str(Y2))



def save_cord():
    global X1,X2,Y1,Y2
    config = {'X1': X1, 'X2': X2,'Y1':Y1,'Y2':Y2}

    with open('config.json', 'w') as f:
        json.dump(config, f)
    exit()

text = tk.Text(win, height=2)
text.pack()
text.insert(tk.END, "Flipkart Gamezone")

openBtn = tk.Button(win, text='Search', command=screenshot_search,bg="green")
openBtn.pack(expand=tk.FALSE, fill=tk.X, side=tk.TOP)

openBtn = tk.Button(win, text='Exit', command=exit_,bg="red")
openBtn.pack(expand=tk.FALSE, fill=tk.X, side=tk.RIGHT)

openBtn = tk.Button(win, text='X1-Y1',command =get_x1_y1,bg="blue")
openBtn.pack(expand=tk.FALSE, fill=tk.X, side=tk.LEFT)

openBtn = tk.Button(win, text='X2-Y2',command =get_x2_y2,bg="blue")
openBtn.pack(expand=tk.FALSE, fill=tk.X, side=tk.LEFT)


openBtn = tk.Button(win, text='Save ',command =save_cord,bg="green")
openBtn.pack(expand=tk.FALSE, fill=tk.X, side=tk.LEFT)
win.mainloop()
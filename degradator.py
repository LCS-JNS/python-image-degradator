import os
from PIL import Image
from tkinter import Tk, filedialog
from tkinter import ttk
import tkinter as tk
from pathlib import Path

QUALITY = 100
EXIT = False
LEVEL = 'Soft'

def selectImage():
    root = Tk()
    root.withdraw()
    
    file = filedialog.askopenfilename(
        title="Select image",
        filetypes=[("Images", "*.jpg *.jpeg")]
    )
    
    return file

def selectDegradationLevel():
    
    def confirm():
        global QUALITY
        global LEVEL
        LEVEL = combo.get()
        if LEVEL == "Soft":
            QUALITY = 40
        elif LEVEL == "Medium":
            QUALITY = 20
        elif LEVEL == "Hard":
            QUALITY = 10
        elif LEVEL == "Extreme":
            QUALITY = 5
        else:
            return
        root.quit()
        root.destroy()
    
    def cancel():
        global EXIT
        EXIT = True
        root.quit()
        root.destroy()
    
    root = tk.Tk()
    root.title("Degradation")
    root.geometry("450x150")
    root.resizable(False, False)
    
    # Centralize window
    root.update_idletasks()
    x = (root.winfo_screenwidth() // 2) - (450 // 2)
    y = (root.winfo_screenheight() // 2) - (150 // 2)
    root.geometry(f"450x150+{x}+{y}")
    
    label = tk.Label(root, text="Select degradation level:", font=("Arial", 11))
    label.pack(pady=15)
    
    options = [
        "Soft",
        "Medium",
        "Hard",
        "Extreme"
    ]

    combo = ttk.Combobox(root, values=options, state="readonly", width=40, font=("Arial", 10))

    combo.pack(pady=10)
    
    buttonsFrame = tk.Frame(root)
    buttonsFrame.pack(pady=15)
    
    btn_ok = tk.Button(buttonsFrame, text="OK", command=confirm, width=10, font=("Arial", 10))
    btn_ok.pack(side=tk.LEFT, padx=5)
    
    btnCancel = tk.Button(buttonsFrame, text="Cancel", command=cancel, width=10, font=("Arial", 10))
    btnCancel.pack(side=tk.LEFT, padx=5)
    
    root.mainloop()
    
    return

def degradateImage(imagePath):
    diretorio = os.path.dirname(imagePath)
    fileName = os.path.basename(imagePath)
    noExtentionFileName, extention = os.path.splitext(fileName)
    
    name = f"{noExtentionFileName}_degradated_{LEVEL.lower()}_{extention}"
    finalPath = os.path.join(diretorio, name)
    finalFile = Path(finalPath)
    
    if finalFile.exists():
        os.remove(finalPath)
    
    img = Image.open(imagePath)
    img.save(finalPath, quality=QUALITY)
    
    return finalPath

def main():    
    imagePath = selectImage()
    
    if not imagePath:
        return
    
    selectDegradationLevel()
    
    if EXIT:
        return
    
    path = degradateImage(imagePath)     
    image = Image.open(path)
    image.show()

if __name__ == "__main__":
    main()
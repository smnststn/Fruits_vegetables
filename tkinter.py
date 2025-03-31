import tkinter as tk
from tkinter import filedialog
import requests
from PIL import Image, ImageTk
from io import BytesIO

# Function to upload image and get prediction
def upload_image():
    file_path = filedialog.askopenfilename(title="Select an image")
    if file_path:
        image = Image.open(file_path)
        image.thumbnail((250, 250))  # Resize for display
        img_display = ImageTk.PhotoImage(image)
        label.config(image=img_display)
        label.image = img_display  # Keep reference to avoid garbage collection

        # Make a POST request to the Flask backend
        files = {'file': open(file_path, 'rb')}
        response = requests.post("http://127.0.0.1:5000/predict", files=files)
        if response.status_code == 200:
            prediction = response.json().get('prediction')
            prediction_label.config(text=f"Predicted: {prediction}")
        else:
            prediction_label.config(text="Error in prediction")

# Function to upload an image from URL
def upload_url():
    url = url_entry.get()
    if url:
        response = requests.post("http://127.0.0.1:5000/predict_url", json={"url": url})
        if response.status_code == 200:
            prediction = response.json().get('prediction')
            prediction_label.config(text=f"Predicted: {prediction}")
        else:
            prediction_label.config(text="Error in prediction")

# GUI setup
root = tk.Tk()
root.title("Fruit/Vegetable Prediction")

upload_button = tk.Button(root, text="Upload Image", command=upload_image)
upload_button.pack()

url_entry = tk.Entry(root)
url_entry.pack()

url_button = tk.Button(root, text="Upload Image from URL", command=upload_url)
url_button.pack()

label = tk.Label(root)
label.pack()

prediction_label = tk.Label(root)
prediction_label.pack()

root.mainloop()

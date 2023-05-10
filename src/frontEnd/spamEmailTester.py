import tkinter as tk
import pickle
import numpy
from sklearn.feature_extraction.text import TfidfVectorizer

def getSpam(input):
    # Predicting

        model_path = "models/trained_spam_email_dataset_model"
        vectorizer_path = "models/vectorizer_for_spam_email"
        with open(model_path,'rb') as f:
            model = pickle.load(f)
        with open(vectorizer_path,'rb') as f:
            vectorizer = pickle.load(f)
        # input = numpy.array(array).reshape(1,-1)
        # prediction = model.predict(input)
        features = vectorizer.transform([input])
        prediction = model.predict(features)
        return prediction

def run_gui():
    def check_spam():
        # Get input from the text area
        input_text = text_input.get("1.0", tk.END).strip()
        output_text = "Checking..."
        # Do some processing on the input
        spamResult = getSpam(input_text)
        if isinstance(spamResult, (list, tuple)):
            spamResult = spamResult[0]

        if spamResult==0:
            output_text = "Legitimate!"
        elif spamResult==1:
            output_text = "Spam :("
        else:
            output_text = spamResult

        # Update the output label with the result
        output_label.config(text=output_text)

    # Create the main window
    window = tk.Tk()
    window.title("Spam email Checker")

    #Vars
    backgroundColor = "#f7c1a3"
    my_font = ("Cascadia Code", 20)
    my_font_small = ("Cascadia Code", 16)
    my_font_tiny = ("Cascadia Code", 11)

    window.configure(bg=backgroundColor)

    # Create the Header label
    header_label = tk.Label(window,bg=backgroundColor,font=my_font, text="Input your email below and press the run button")
    desc_label = tk.Label(window,bg=backgroundColor,font=my_font_small, text="Should be email body")
    
    # Create the input text area
    text_input = tk.Text(window,height=10,width=80,padx=20, pady=20,font=my_font_tiny)

    # Create the run button
    run_button = tk.Button(window,height=2,width=8, text="Run", command=check_spam)
    
    # Create the output label
    output_label = tk.Label(window,bg=backgroundColor,font=my_font, text="")

    header_label.pack(pady=8,padx=40)
    desc_label.pack(pady=4)
    text_input.pack(pady=20,padx=20)
    run_button.pack(pady=8)
    output_label.pack()

    # Start the main event loop
    window.mainloop()

    
run_gui()
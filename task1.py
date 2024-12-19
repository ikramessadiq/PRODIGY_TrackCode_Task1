import tkinter as tk
from tkinter import messagebox
import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression


data_train = pd.read_csv("train.csv")
data_test = pd.read_csv("test.csv")


features = ['GrLivArea', 'TotRmsAbvGrd', 'FullBath']  
X_train = data_train[features] 
y_train = data_train['SalePrice'] 


model = LinearRegression()
model.fit(X_train, y_train)


def predict_price():
    try:
        
        gr_liv_area = float(entry_gr_liv_area.get())
        tot_rms_abv_grd = int(entry_tot_rms_abv_grd.get())
        full_bath = int(entry_full_bath.get())

        
        features_input = [[gr_liv_area, tot_rms_abv_grd, full_bath]]
        
        
        predicted_price = model.predict(features_input)[0]
        
        
        messagebox.showinfo("Price Estimate", f"The estimated price is: {predicted_price:.2f} $")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid values ​​for the characteristics.")


root = tk.Tk()
root.title("House Price Estimate")


tk.Label(root, text="Living area (in square feet):").grid(row=0, column=0, padx=10, pady=10)
entry_gr_liv_area = tk.Entry(root)
entry_gr_liv_area.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Total number of rooms above ground:").grid(row=1, column=0, padx=10, pady=10)
entry_tot_rms_abv_grd = tk.Entry(root)
entry_tot_rms_abv_grd.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Number of full bathrooms:").grid(row=2, column=0, padx=10, pady=10)
entry_full_bath = tk.Entry(root)
entry_full_bath.grid(row=2, column=1, padx=10, pady=10)


predict_button = tk.Button(root, text="Estimate the price", command=predict_price)
predict_button.grid(row=3, column=0, columnspan=2, pady=20)


root.mainloop()

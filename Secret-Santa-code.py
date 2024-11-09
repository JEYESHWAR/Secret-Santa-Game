import datetime
from inspect import _empty
import os
from queue import Full
import random
import tkinter as tk
from tkinter import filedialog
import csv
from tkinter import messagebox
current_year = datetime.datetime.now().year


def shuffle_the_array(in_array):
    random.shuffle(in_array)
    return in_array


def map_array(arr1,arr2):
    final_arr = []
    for i in range(0,len(arr1),1):
        # Comparring the Mail Id of both the Array arr1 --> Emp name and Mail arr2 --> Secret Emp Name and Mail
        if(arr1[i][1] != arr2[i][1]):
            result = arr1[i] + arr2[i]
            final_arr.append(result)
        else:
            shuffle_the_array(arr2)
            map_array(arr1,arr2)
    
    return final_arr


def open_file():
    # Open file dialog to select a CSV file
    file_path = filedialog.askopenfilename(
        title="Select a CSV file",
        filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")]
    )
    
    if file_path:
        file_name = os.path.basename(file_path)
        new_filename = file_name.split("-")
        new_filename.pop()
        resultFilename = '-'.join(map(str, new_filename))
        final_filename = resultFilename + "-" + str(current_year)
        file_location = os.path.dirname(file_path)
        empName_and_empEmail = []
        serectEmpname_and_mail = []
        
        # Read and print CSV file content
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            csvreader = csv.reader(csvfile)
            for index, row in enumerate(csvreader):
                if(index == 0):
                    header_for_csv = row
                else:
                    # Check if any of the required fields are empty (columns 0 to 3)
                    empty_field_found = False 
                    empty_field_index = -1  # Store index of the first empty field

                    # Looping the column with column count of header_for_csv
                    for i in range(len(header_for_csv)):  
                        if row[i] == "":
                            empty_field_found = True # if Empty found assign it to True
                            empty_field_index = i
                            break

                    if empty_field_found:
                        # Error message to show which column is empty
                        column_names = ["Emp Name", "Emp Email", "Secret Emp Name", "Secret Emp Email"] # to idenfiy the which column contains empty field in it.
                        messagebox.showerror("Error", f"The data is mishandled. The field '{column_names[empty_field_index]}' is empty in row {index+1}. Kindly check the CSV file and execute the tool again.")
                        break

                    else: # No Empty Data means appaend the data to the array
                        empName_and_empEmail.append([row[0], row[1]])  # Getting Emp name and Emp mail
                        serectEmpname_and_mail.append([row[2], row[3]])  # Getting Secret Emp Name and Secret Emp Mail

    
    
    #  Validating both the array need to be in same len so that we can able to avoid emp vaccant in the csv data
    if(empty_field_found == False):
        # intital Shuffle
        shuffle_the_array(serectEmpname_and_mail)
        
        # Mapping the Array
        final_array_out = map_array(empName_and_empEmail,serectEmpname_and_mail)

        if(len(final_array_out) != 0):
            # Open a new CSV file for writing
            file_path = os.path.join(file_location, final_filename +'.csv')
            with open(file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                # Write the header (optional)
                writer.writerow(header_for_csv)
                
                for row in final_array_out:
                    # Write the Datas from the excel
                    writer.writerow(row)
            
            messagebox.showinfo("Success", f"Output CSV file is generated in the respective path:\n\n {file_path}") 
        else:
             messagebox.showwarning("Warning", "No data found") 
 
    root.quit()
    



# Create the main window
root = tk.Tk()
root.title("Secret Santa Game")
root.geometry("300x100")

# Create a button to open the file dialog
open_button = tk.Button(root, text="Select the CSV file", command=open_file)
open_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()

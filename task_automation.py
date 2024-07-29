import os
import shutil
import pandas as pd
import numpy as np
import psutil

def organize_files_by_extension(path):
    list_files = os.listdir(path)
    for file in list_files:
        name, extension = os.path.splitext(file)
        extension = extension[1:]

        if os.path.exists(os.path.join(path, extension)):
            shutil.move(os.path.join(path, file), os.path.join(path, extension, file))
        else:
            os.makedirs(os.path.join(path, extension))
            shutil.move(os.path.join(path, file), os.path.join(path, extension, file))
    print("Files organized by extension successfully.")

def read_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        print("Data loaded successfully.")
        return df
    except Exception as e:
        print(f"Error reading the CSV file: {e}")
        return None

def write_csv(data, file_path):
    try:
        data.to_csv(file_path, index=False)
        print(f"Data saved to {file_path}.")
    except Exception as e:
        print(f"Error writing to the CSV file: {e}")

def clean_data(df):
    duplicates_before = df.duplicated().sum()
    print(f"Duplicates before removal: {duplicates_before}")

    df = df.drop_duplicates()
    nulls_before = df.isnull().sum()
    print("\nNull values before handling:")
    print(nulls_before)

    df = df.dropna(how='any')
    df = df.interpolate()
    nulls_after = df.isnull().sum()
    print("\nNull values after interpolation:")
    print(nulls_after)
    
    duplicates_after = df.duplicated().sum()
    print(f"\nDuplicates after removal: {duplicates_after}")

    return df

def process_data(input_file, output_file):
    data = read_csv(input_file)
    
    if data is not None:
        print("\nData before cleaning:")
        print(data)

        cleaned_data = clean_data(data)
        
        print("\nData after cleaning:")
        print(cleaned_data)

        write_csv(cleaned_data, output_file)
        
        print(f"\nData cleaning completed. Cleaned data saved to {output_file}")

def display_system_info():
    memory_info = psutil.virtual_memory()
    print(f"Total Memory: {memory_info.total / (1024 ** 3):.2f} GB")
    print(f"Used Memory: {memory_info.used / (1024 ** 3):.2f} GB")
    print(f"Free Memory: {memory_info.free / (1024 ** 3):.2f} GB")
    print('\n')
    
    disk_info = psutil.disk_usage('c:\\')
    print(f"Total Disk Space: {disk_info.total / (1024 ** 3):.2f} GB")
    print(f"Used Disk Space: {disk_info.used / (1024 ** 3):.2f} GB")
    print(f"Free Disk Space: {disk_info.free / (1024 ** 3):.2f} GB")
    print('\n')
    
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        try:
            print(f"PID: {proc.info['pid']}, Name: {proc.info['name']}, User: {proc.info['username']}")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

def menu():
    print("Menu:")
    print("1. Organize Files by Extension")
    print("2. Process CSV Data")
    print("3. Display System Information")
    print("4. Exit")

def main():
    while True:
        menu()
        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            path = input("Enter the path to organize files: ")
            organize_files_by_extension(path)
        elif choice == '2':
            input_file = input("Enter the path of the input CSV file: ")
            output_file = input("Enter the path of the output CSV file: ")
            process_data(input_file, output_file)
        elif choice == '3':
            display_system_info()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

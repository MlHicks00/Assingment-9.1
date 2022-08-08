# import the os library
import os

def main():

  # User input
  directory = input("Enter the directory to save your file: ")
  file_name = input("Enter the file name: ")
  user_name = input("Enter your name: ")
  address = input("Enter your address: ")
  phone_number = input("Enter your phone number: ")
 
      
  if os.path.isdir(directory):
  
  #writing and creating the file entered by user
    with open(directory, "w") as written_file:
      written_file.write(file_name + "," +user_name + "," + address + "," + phone_number)

    #make sure to close the file
      written_file.close()
  
    #display the file contents to the user for validation purposes
    print("The file contents are: ")

    #reading written file
    with open(directory,"r") as written_file:
    
    #display the file contents to the user for validation purposes
    print("The file contents are: ")
    
    #displaying the file written
      data = written_file.read()
      print(data)
   
      # close the file
      written_file.close()
  else: 
    print("Error, Directory does not exist")

main()

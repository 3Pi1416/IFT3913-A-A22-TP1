# IFT3913-A-A22-TP1
Hugo Carrier: 20197563

Maggie Robert: 20182443

///////////////////////////////////////
you can execute each programme invidualy by executing their binary in command line (changing the command with the binary example : main.exe -> jls path == jls.exe path)
///////////////////////////////////////
Execution of the main:
start main by executing the binary main. 

jls:
Print and create a csv of :
•	Path of file
•	Package’s name
•	Class’s name 
command: jsl path_folder [optional]root
path_folder: folder where to start the execution of jsl
root: optional, if not mention, is equal to path_folder, use to change the name of the java package by giving a root different from the path ;
example  path_folder = x\y\z, root =x -> java name would be y.z.[*]

nvloc:
Print number of nonempty line in file.
command: nvloc file
file : path of java file 

lscec:
Print :
•	Path of file
•	Package’s name
•	Class’s name 
•	lscec

command lscec path_folder csv_file
lscec path_folder csv_file
	path_folder: folder where to start the execution of jsl
	csv_file: file where jsl data is.

Egon:
Print and create a csv of:
•	Path of file
•	Package’s name
•	Class’s name 
•	nvloc
•	Lscec
Of the class that are superior of the threshold in both nvloc and lscec compared to the other classes
Command : egon  path_folder threshold [optional]add_to_name_output
path_folder: folder where to start the execution of jsl
threshold: threshold for a data to be in the upper echelon for the nvloc and  Lscec values.

Exit: to exit



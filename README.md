# IFT3913-A-A22-TP1
Hugo Carrier: 20197563

Maggie Robert: 20182443

///////////////////////////////////////
you can execute each programme individually by executing their binary in command line (changing the command with the binary example : main.exe -> jls path == jls.exe path)
///////////////////////////////////////
Execution of the main:
start main by executing the binary main. 

jls:
Prints and creates a csv of :
•	Path of Java file
•	Package of file
•	Class name of file
command: jsl path_folder [optional]root
path_folder: folder where to start the execution of the program
root: optional; if not specified it will be equal to the path_folder. Use it to change the name of the java package by giving a root that is different from the path ;
example  path_folder = x\y\z, root =x -> java name would be y.z.[*]

nvloc:
Prints the number of nonempty lines in a file.
command: nvloc file
file : path of java file 

lscec:
Prints and creates a csv of :
•	Path of Java file
•	Package of file
•	Class name of file
•	lscec score of file

command lscec path_folder csv_file
lscec path_folder csv_file
	path_folder: folder where to start the execution of the program
	csv_file: file where jsl-format data is.

Egon:
Prints and creates a csv with the following data of the classes that have both nvloc and lscec scores in the top {threshold}% of all the classes in the provided folder:
•	Path of Java file
•	Package of file
•	Class name of file
•	lscec score of file
•	nvoloc score of file
Command : egon  path_folder threshold [optional]add_to_name_output
path_folder: folder where to start the execution of the program
threshold: the percentage threshold for the nvloc and lcsec scores of the output classes.

Exit: to exit



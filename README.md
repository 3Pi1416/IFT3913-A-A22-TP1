IFT3913-A-A22-TP1
Hugo Carrier: 20197563

Maggie Robert: 20182443

Link to Github repository: https://github.com/3Pi1416/IFT3913-A-A22-TP1

///////////////////////////////////////
option A. !only in the repo, to big to be put in the 20 mb zip! You can execute each program individually by choosing your corresponding OS folder and executing the respective binary in the command line with the appropriate arguments. 
option B. You can execute the main and call each method by name in it. 
///////////////////////////////////////
N.B. one and only one space between input
///////////////////////////////////////

jls:
Prints and creates a csv of :
•	Path of Java file
•	Package of file
•	Class name of file

command: jls path_folder [optional]root
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

command: lscec path_folder csv_file
	path_folder: folder where to start the execution of the program
	csv_file: file where jsl-format data is.

Egon:
Prints and creates a csv with the following data of the classes that have both nvloc and lscec scores in the top {threshold}% of all the classes in the provided folder:
•	Path of Java file
•	Package of file
•	Class name of file
•	lscec score of file
•	nvoloc score of file

Command : egon path_folder threshold [optional]add_to_name_output
path_folder: folder where to start the execution of the program
threshold: the percentage threshold for the nvloc and lcsec scores of the output classes.



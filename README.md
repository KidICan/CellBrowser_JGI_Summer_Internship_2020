## This repository includes all the files that we might need for our test.
 
## This reposotory has the following Folders

 
### arabidopsis_singlecelldata_for_cellbrowerser:

-This folder contains all the cell data files that we need to run the cell browerser builder. 

## cells:

This folder contains the output files of both the arabadopsis cell data and the
 sample data.
	-Arabodopsis output data:
		-OutputFiles
	-Sample output data:
		-sample 

### mini/mini:

-This folder contains all the cell data files that are needed to run the cell broweser builder
on the sample data

# HOW TO RUN cbBuild

Once you have installed the cell browser viewer from the following website
https://cellbrowser.readthedocs.io/installation.html and have python installed on your computer
running the cell browerser is quite simple. 

## STEP 1: THE WORKING DIRECTORY

Make sure that in your terminal, your working directory is the directory that contains all the 
cell data files

## STEP 2: THE CELLBROWERSER.CONFIG FILE
The most important part for this process is to have the cellbrowser.config in the same directory 
as your cell data files. 
If you do not have the cellbrowers.config file in the correct working directory
addig is very simple. Simply run the comand cbBuild --init. This will coppy the sample cellbrower.config file
to your working directory for you. If you would like other things that you can add to the cbBuild comand 
simple run cbBuild by itself to see all of your options.
Once you have your cellbroweser.config file run the follwoing comand: nano cellbrowser.config. 
This will let you edit the cellbrowser.config file to work for your data. Once here edit the file under the fields
specified in the .config file and save it.


## STEP 3: RUNNING cbBuild
To run the the command you must have the follwing field to the comand:

cbBuild -o ~/public_html/cells/ -p 8888

These are the arguments for this command
}cbBuild (The base command)
}-o (Telling the comand to output the files)
} ~/public_html/cells/ (the directory where you want your output files to be sent)
}-p (Telling that you want to publish this build)
}8888 (The port were you will host the cell broweser)


If all of these steps were done correclty the comand should start to process the
input files and tell you to riderect your browser to your local host port :8888
Look at the bottom of the terminal output for your local host number.
 
 
 


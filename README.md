# AO3_Fandom_Scrape
Python scripts for scraping data from the AO3 (archiveofourown.org).

Have not yet explored Github enough to know how to package for installation via command prompt. So for now

SETUP
1.  Fully install Python 3 from https://www.python.org
2.  Use Command Prompt and the following string (without quotations) to install other components needed: "pip install beautifulsoup4 requests openpyxl pandas"
3.  Choose a location to save all the python, text, and output files. Download the files to that location. If you are scraping pairings, you will also need to create a .txt file in that location with all your pairings saved, one per line, in the way they appear on AO3 (more below)
4.  In Command Prompt, cd C:\Enter\Folder\Location (e.g. C:\Users\Zephyr\AO3_Python) will take you to the location so you can run the files without needing to type in the full location string. (Note: if you use the python files regularly and want a short-cut, how to do this will be shown near the bottom of the   readme)
5.  Choose the script (single or combination, described below) you want to run and call the file by typing: python example_script.py into the command prompt.
6.  Some scripts just run without anymore input, others require you to type into the command prompt. This is indicated below. 
7.  The scripts with work together use a set series of file names to call the next step so if you are doing multiple batches of scraping, make sure to rename       the generated files (url.txt, results.xlsx etc.) to something else before running more scripts. I have no yet tested whether subsequent runs will correctly     append. Once I have, I'll update this Read Me.


PAIRINGS.TXT FILE
To run the scripts which search for pairing numbers, you will need to create a .txt file that has each of the pairings you want to generate a URL about, with each pairing on its own line. I have included a .txt file with the top 100 F/F pairings of 2022 as an example [Remember to not place this .txt into your working folder unless you want to use it].

With this file, the pairing names must look how they do on AO3 or it will not scrape the page. One common thing I find is that people do not know how to write the | symbol that is used to separate when a character has two used names e.g. Evil Queen| Regina Mills/Emma Swan so sometimes will us the letters lowercase L or uppercase i which then do not work for generating the URL. So copy the pairings exactly as they are from AO3.



COMBO 1: NUMBER OF WORKS FOR A LIST OF PAIRINGS (ALL-TIME)
This will use a "pairings.txt" file to scrape the number of works for each pairing on AO3, without a date restriction, and output a file showing the pairing name and the number of works to a .xlsx

Once you have created your pairings.txt file, and navigated your Command Prompt to the correct location, type: python full_pairing_script.py
Various messages should indicate that it is processing (e.g. no Error messages)
Once complete, a .xslx file will have been created with the pairings and work numbers.

Note - I need to work out how to remove an unwanted space from the works (numbers) column. Until done, select that column, use Ctrl + H, put a space in the "Find" box and leave the "Replace" box blank of anything, then 'Replace All'

full_pairing_script.py will run the following files:
    gen_pair.py
    num_pp.py
    striptext.py



STANDALONE 1: FIND FIRST 300 CHARACTER, RELATIONSHIP, AND FREEFORM TAGS IN A FANDOM PAGE
This pulls the information from the page that you get if you click the Underlined name of the Fandom at the top of that fandom's works page. It can also be reached through https://archiveofourown.org/tags/Fandom Name e.g. https://archiveofourown.org/tags/Supergirl

It will take the three categories (characters, relationships, freeform) and write them into a .xlsx file.
I am working on adding the feature to the file so that it will automatically delimit based on the comma that separates each section, but until I have done that you can do the following in Excel: High data to be separated, go to Data tab at top, choose 'Text to columns', select the 'Delimited' radio button then next, uncheck default option (usually 'Tab') and check 'Comma'. Press finish.
    
To run this, once you have navigated Command Prompt to your files via cd as described at the beginning, type: python Pull_biggest_tags_fandom.py
You will be asked to input your fandom tag. Again, this needs to be exactly as it appears on AO3.

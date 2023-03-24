# AO3_Fandom_Scrape
## Python scripts for scraping data from the AO3 (archiveofourown.org).

This is very much a work in progress as I am still learning Python; some bits of coding are slightly cobbled together and may be less efficient than they could be, I've left some print() components in that could be improved but were added in to confirm the code worked, and there are some changes I have to make to improve use. I do not have a timeline for this as this is just a bit of fun. I have tested quite thoroughly, but errors always have a way of happening even with the best testing. 

### Note on AO3's TOS for Web-scraping
Per their post: 'Selective data dump for fan statisticians' on the 21st March 2021
"We hope to one day be able to provide regular, automatic dumps of this data, but for now, our focus is on other projects. In the meantime, there are a number of tools available to scrape publicly available data, or you're welcome to build your own. (If you're planning to scrape the Archive, we do ask that you include a delay between requests to reduce load on our servers, and avoid scraping on weekends, which are our busiest time. We'd also appreciate it if you could set your scraper's user agent string to include the word "bot.")"

I have a delay of 6 (the lowest they ask for is 5) in the script that does the actual scraping (num_pp.py) but I tend to alter it myself to a higher number (10 seconds or more) if I'm leaving it to run. The location is marked with a comment so you can alter it easily. Please do not lower it below 5; not only does it put pressure on the servers, it also increases the likelihood of the webpage not loading (the "Retry later" message) and then you won't get the data anyway because those pages will be missed or an error will occur.

------------------

## Setup
I have not yet explored Github enough to know how to package for installation via command prompt. So for now
1.  Fully install Python 3 from https://www.python.org
2.  Use Command Prompt and the following string (without quotations) to install other components needed: "pip install beautifulsoup4 requests openpyxl pandas"
3.  Choose a location to save all the python, text, and output files. Download the files to that location. You will need to create some .txt files that the scripts pull from.
    1. user_agent.txt - AO3 ask (as above) that user agents contain the string 'bot'. A search online of "what is my user agent" can help you find what yours is so you'll paste that into the .txt followed by a semi-colon ; then an identifier of your bot e.g happy.bot. I also add a forward slash and then my e-mail address to adhere to ethical scraping.
    2. login.txt - If you want to be logged into AO3 (to see the stats including Restricted Works) then you'll need to create a login.txt with your username on the top line and your password on the second line.
    3. pairings.txt - If you are scraping multiple pairings, you will also need to create a .txt file in that location with all your pairings saved, one per line, in the way they appear on AO3 (more below)
4.  In Command Prompt, cd C:\Enter\Folder\Location (e.g. C:\Users\Zephyr\AO3_Python) will take you to the location so you can run the files without needing to type in the full location string. (Note: if you use the python files regularly and want a short-cut, how to do this will be shown below.)
5.  Choose the script (single or combination, described below) you want to run and call the file by typing: python example_script.py into the command prompt.
6.  Some scripts just run without anymore input, others require you to type into the command prompt. This is indicated below. 
7.  The scripts with work together use a set series of file names to call the next step so if you are doing multiple batches of scraping, make sure to rename       the generated files (url.txt, results.xlsx etc.) to something else before running more scripts. I have no yet tested whether subsequent runs will correctly     append. Once I have, I'll update this Read Me.

------------------

## Shortcut to File Locations
If you find yourself using the python files regularly and want to skip the step of using cd C:\Enter\Folder\Location each time, then open up a .txt file (in Notepad or equivalent) and type the following in (changing the location path to where your folder is):

@echo off
cd C:\Enter\Folder\Location
cmd

Not save the file as change_dir.bat and in the future, you can double click that and it'll load your Command Prompt up in the directory of where you're keeping your Python files.

------------------

## Pairings.txt File
To run the scripts which search for pairing numbers, you will need to create a .txt file that has each of the pairings you want to generate a URL about, with each pairing on its own line. I have included a .txt file with the top 100 F/F pairings of 2022 as an example [Remember to not place this .txt into your working folder unless you want to use it].

With this file, the pairing names must look how they do on AO3 or it will not scrape the page. One common thing I find is that people do not know how to write the | symbol that is used to separate when a character has two used names e.g. Evil Queen| Regina Mills/Emma Swan so sometimes will us the letters lowercase L or uppercase i which then do not work for generating the URL. So copy the pairings exactly as they are from AO3.

------------------

## COMBO 1: NUMBER OF WORKS FOR A LIST OF PAIRINGS (ALL-TIME)
This will use a "pairings.txt" file to scrape the number of works for each pairing on AO3, without a date restriction, and output a file showing the pairing name and the number of works to a .xlsx

Once you have created your pairings.txt file, and navigated your Command Prompt to the correct location, type: python full_pairing_script.py
Various messages should indicate that it is processing (e.g. no Error messages)
Once complete, a .xslx file will have been created with the pairings and work numbers.

Note - I need to work out how to remove an unwanted space from the works (numbers) column. Until done, select that column, use Ctrl + H, put a space in the "Find" box and leave the "Replace" box blank of anything, then 'Replace All'

full_pairing_script.py will run the following files:
    gen_pair.py
    num_pp.py
    striptext.py

------------------


## COMBO 2: NUMBER OF WORKS FOR A LIST OF PAIRINGS (CHOOSE DATE, ALL + ONE TRUE PAIRING)
This will use a "pairings.txt" file to scrape the number of works for each pairing on AO3, within the dates specified by the user when prompted, and output a file showing the pairing name and the number of works to a .xlsx. The user also has an option to do the process for a single typed in Pairing rather than a list from the .txt

Once you have created your pairings.txt file, and navigated your Command Prompt to the correct location, type: python pairing_choose_date.py
You will be asked if you want to use the pairings.txt file Y/N. Selecting Y will use the file, selecting N will give you the option to type in a single pairing.
Then you will be asked to provide a date range. Take care inputting as I am still to add in a loop to allow re-entry if an incorrect date is provided, so errors will mean starting again.
Various messages should indicate that it is processing (e.g. no Error messages)
Once complete, a .xslx file will have been created with the pairings and work numbers for works tagged with that pairing and works where that is the only pairing tagged (One True Pairing/OTP)

Note - I need to work out how to remove an unwanted space from the works (numbers) column. Until done, select that column, use Ctrl + H, put a space in the "Find" box and leave the "Replace" box blank of anything, then 'Replace All'

fpairing_choose_date.py will run the following files:
    pairing_date_range.py
    num_pp.py
    striptext.py

------------------

## STANDALONE 1: FIND FIRST 300 CHARACTER, RELATIONSHIP, AND FREEFORM TAGS IN A FANDOM PAGE
This pulls the information from the page that you get if you click the Underlined name of the Fandom at the top of that fandom's works page. It can also be reached through https://archiveofourown.org/tags/Fandom Name

It will take the three categories (characters, relationships, freeform) and write them into a .xlsx file.
I am working on adding the feature to the file so that it will automatically delimit based on the comma that separates each section, but until I have done that you can do the following in Excel: High data to be separated, go to Data tab at top, choose 'Text to columns', select the 'Delimited' radio button then next, uncheck default option (usually 'Tab') and check 'Comma'. Press finish.
    
To run this, once you have navigated Command Prompt to your files via cd as described at the beginning, type: python Pull_biggest_tags_fandom.py
You will be asked to input your fandom tag. Again, this needs to be exactly as it appears on AO3.

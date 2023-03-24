import subprocess

#List of scripts to run in order
scripts = ["gen_pair.py", "num_pp.py", "striptext.py"]

#Run each script in the list
for script in scripts:
	subprocess.run(["python", script])
	print("Process 1 Complete")

print("All scripts executed successfully.")

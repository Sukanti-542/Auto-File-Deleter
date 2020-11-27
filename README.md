# Automatic File Deleter

## Delete un-needed files automatically

<br/><br/>
Below are the configurations you need to update for the script to work

```
# Enter directory path from where the files/folders should to be deleted
directory_path = "PATH"  
# Enter the number of days beyond which the files/folders should to be deleted
threshold_days = 30 
```

### Want to execute the script automatically?
<br/>

1. Comment the below code 

```
confirm = input("Do you want to delete these files yes or no: ")
if confirm == "yes":
```
2. Create a batch file with the below code

```
"Path where your Python exe is stored\python.exe" "Path where your Python script is stored\script_name.py"
pause
```
3. Schedule a basic task using Windows Scheduler to run at your choice of time




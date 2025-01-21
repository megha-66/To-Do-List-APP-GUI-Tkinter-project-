## Description 
#### This project uses Tkinter in Python to build a Progress list for a work
> It can be used like a to-do list. 

#### There is a single source code file, which does all the job. 

> Note : You will need Pyinstaller python package to use this application as a desktop app.


## Steps to deploy the application in your desktop :- 
> 1. Open your terminal and type - 

```
pip install pyinstaller
```
> 2. Download the to-do-list.py file and open it in your desktop.
> 3. Install tkinter again from the terminal simply using - 
```
pip install tkinter
```
> 4. Set the base directory `base_dir` by giving a path from desktop to it. 
> 5. Update path1, path2 and path3 for the images. 
>> Note : You need to keep all 3 images under a folder named `images` exactly to use the same variables. 
> 6. To be precise your directory structure should look like - 

```
your_projecr/
├── to-do-list.py
├── images/
│   ├── image1.png
│   ├── image2.png
```
> 7. Run the following command on your terminal - 
```
pyinstaller --onefile --add-data "<path-to-your-image-folder>";images" to-do-list.py
``` 
for Windows. 
>> For Ubuntu or linux-based systems, replace ";" in this command to ":". 
> 8. After the command executes, in the same directory , you will see a `dist` folder, which has the application installed for you. 

###### Congratulations, You did set up the app successfully!

#### All the items/tasks you mention in the list get saved in an items.txt file. 


















 










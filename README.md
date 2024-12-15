## How to use:

1) Open GamePaths.py and add the paths as a string tuple, where the first element is the source directory, and the second element is the backup destiny directory.

    Example: 

    SUPERLIMINAL = (r"C:\Users\supev\AppData\LocalLow\PillowCastle\SuperliminalSteam", 
                   r"D:\Game Saves\Superliminal\SuperliminalSteam")

2) Go to GameBackup.py, and in the 'directories_to_copy' list, add the name of the variable you added earlier GamePaths.py

    Example:

    directories_to_copy = [
        STANLEY_PARABLE,
        WITCHER_3,
        HELLBLADE
    ]

    (This is so you can keep the paths saved in the GamePaths file and simply add/remove them from the directories_to_copy lsit when you no longer wish for the script to act on them.)

3) Open GameBackup.ahk and replace the paths with the ABSOLUTE path to the GameBackup.py file. Modify the keyboard shortcut if you wish, the default is Alt + Numpad3

4) Press Win + R, type 'shell:startup'.

    It will open a folder, everything you put in there will run when you boot your pc.

    Put a SHORTCUT of the GameBackup.ahk file in there.

5) Keep the .ahk file running in the background. Every time you want to back up your files, press Alt + Numpad3 and it will do it automatically for you.

6) Repeat steps 2 and 3 as you wish.

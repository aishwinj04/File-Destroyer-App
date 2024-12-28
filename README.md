# File Destroyer App

## Overview
This is a Python program with a graphical user interface (GUI) that allows users to select files from their system and permanently delete them. The program provides a simple and intuitive interface built using `PyQt6` and helps users securely delete files by overwriting their contents before removing them.

## How the Program Works

1. **File Selection**: The program uses the `QFileDialog` widget from PyQt6 to allow users to select multiple files they wish to delete.
   
2. **File Deletion**: Once files are selected, the program overwrites the contents of each file with empty data and then deletes the file from the file system.
   
3. **User Interface**: The program features a user-friendly GUI with two buttons:
   - **Select Files**: Opens the file dialog to allow users to choose files to delete.
   - **Destroy Files**: Permanently deletes the selected files.

4. **Messages**: After performing the delete action, the program updates the message area to inform the user whether the files were successfully deleted or if no files were selected.

## Features

- Allows selection of multiple files for deletion.
- Overwrites file contents and deletes them permanently.
- Intuitive GUI with feedback messages for the user.
- Simple, one-click file deletion process.
- Cautionary warning to inform users about the irreversible nature of the action.

## Imports Used
- PyQt6 for GUI
- Pathlib 

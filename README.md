🔹 Steps to Load and Use RemoveWriteNodes.py in Nuke
This guide will help you set up and use the RemoveWriteNodes.py script to import Nuke scripts while removing all Write nodes.

🔹 Step 1: Save the Script in the Correct Directory
Open File Explorer (Windows) or Finder (Mac) or use the Terminal (Linux).
Navigate to Nuke's .nuke directory:
Windows: C:\Users\YourUsername\.nuke
macOS/Linux: ~/ .nuke
Save the script as:
Copy
Edit
RemoveWriteNodes.py
🔹 Step 2: Link the Script to Nuke’s Menu
Open Nuke.
In Nuke’s Script Editor, open the menu.py file:
If menu.py doesn’t exist, create one in the .nuke directory.
Add the following line to menu.py:
python
Copy
Edit
import RemoveWriteNodes  # This will load it into Nuke
Save the file and restart Nuke.
🔹 Step 3: Use the Script in Nuke
After restarting Nuke, the script is now available in Nuke’s UI.

Option 1: Using the Menu
Open Nuke.
Go to "Custom Tools" in the top menu bar.
Click "Import & Remove Write Nodes".
Option 2: Using the Shortcut
Open Nuke.
Press Shift+R on your keyboard.
🔹 Step 4: Select a Nuke Script to Import
When prompted, choose the .nk file you want to import.
Click "Open".
🔹 What Happens Next?
✅ All Write nodes will be removed from the imported script.
✅ A cleaned version (_no_write.nk) will be created.
✅ The cleaned script will be added to the current Nuke session.
✅ Imported nodes will be moved to a different location to avoid overlap.
✅ A confirmation message will appear in Nuke.

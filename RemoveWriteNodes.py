import os
import nuke

def remove_write_nodes_from_import(nk_file_path):
    """
    Opens a Nuke script (.nk), removes all Write nodes, saves a cleaned version, 
    and imports it into the current session at a different location.
    """
    try:
        # If user cancels the file selection, exit gracefully
        if not nk_file_path:
            print("User canceled file selection. No script imported.")
            return

        print(f"Processing Nuke script: {nk_file_path}")

        # Read the Nuke script as plain text
        with open(nk_file_path, "r", encoding="utf-8") as file:
            nk_lines = file.readlines()

        # Filter out Write nodes
        new_lines = []
        inside_write_node = False

        for line in nk_lines:
            if line.strip().startswith("Write {"):
                inside_write_node = True  # Start ignoring Write node block
            elif inside_write_node and line.strip() == "}":
                inside_write_node = False  # End of Write node block, skip adding it
                continue
            
            if not inside_write_node:
                new_lines.append(line)  # Keep everything except Write nodes

        # Save the modified script as a new file
        temp_nk_file = nk_file_path.replace(".nk", "_no_write.nk")
        with open(temp_nk_file, "w", encoding="utf-8") as file:
            file.writelines(new_lines)

        # Import the cleaned script into the existing Nuke session (instead of replacing it)
        nuke.nodePaste(temp_nk_file)

        # Move the newly imported nodes to a different location to avoid overlap
        imported_nodes = nuke.selectedNodes()
        if imported_nodes:
            x_offset = 300  # Adjust this value as needed
            y_offset = 200  # Adjust this value as needed
            for node in imported_nodes:
                node.setXpos(node.xpos() + x_offset)
                node.setYpos(node.ypos() + y_offset)

        nuke.message(f"Imported script with Write nodes removed:\n{temp_nk_file}")
        print(f"Imported script without Write nodes: {temp_nk_file}")

    except Exception as e:
        print(f"Error processing Nuke script: {e}")
        nuke.message(f"Error: {e}")

# Add menu item in Nuke
def add_to_nuke_menu():
    """
    Adds this tool to the Nuke menu under 'Custom Tools' for easy access.
    """
    menu_bar = nuke.menu("Nuke")
    custom_menu = menu_bar.addMenu("Custom Tools")
    custom_menu.addCommand(
        "Import & Remove Write Nodes",
        lambda: remove_write_nodes_from_import(nuke.getFilename("Select Nuke Script", "*.nk")),
        "Shift+R"
    )

# Run the menu addition when the script is loaded
add_to_nuke_menu()

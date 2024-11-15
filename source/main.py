import dearpygui.dearpygui as dpg
import validators
import requests
from bs4 import BeautifulSoup

import containers

badges = {
    "Windows": r"![Static Badge](https://img.shields.io/badge/Windows-2f81f7?style=for-the-badge&logo=windows10&logoColor=white)",
    "mac OS": r"![Static Badge](https://img.shields.io/badge/MacOS-f0f0f0?style=for-the-badge&logo=apple&logoColor=black)",
    "SteamOS + Linux": r"![Static Badge](https://img.shields.io/badge/SteamOS%2FLinux-%23272932?style=for-the-badge&logo=steam)"
}


def print_me(sender):
    print(f"Menu Item: {sender}")

def main():
    with dpg.window(tag="primary_window"):
        with dpg.menu_bar():
            with dpg.menu(label="File"):
                dpg.add_menu_item(label="Save", callback=print_me)
                dpg.add_menu_item(label="Save As", callback=print_me)
                dpg.add_separator()
                dpg.add_menu_item(label="Save Output As", callback=print_me)
                dpg.add_menu_item(label="Copy Output", callback=print_me)
                dpg.add_menu_item(label="Import CSV", callback=lambda: dpg.show_item("file_dialog_id"))
                dpg.add_menu_item(label="Import JSON", callback=lambda: dpg.show_item("file_dialog_id"))

            with dpg.menu(label="Settings"):
                dpg.add_menu_item(label="Theme")
                dpg.add_checkbox(label="Auto Clipboard", default_value=True)
                dpg.add_checkbox(label="Sort Alphabetical", default_value=True)
                dpg.add_checkbox(label="Add Images", default_value=True)

            with dpg.menu(label="Tools"):
                dpg.add_menu_item(label="Markdown to CSV", callback=lambda: dpg.show_item("markdown_convert"))
                dpg.add_menu_item(label="Debug Menu", callback=containers.Debug.show_debug_menu)

            dpg.add_menu_item(label="Help", callback=print_me)

        with dpg.group(tag="software_container"):
            dpg.add_button(label="Add Software", callback=containers.SoftwareForum.add_software_forum)


if __name__ == "__main__":
    dpg.create_context()
    
    main()

    dpg.create_viewport(title='Markdown Generator', width=1080, height=720, resizable=True)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("primary_window", True)
    dpg.start_dearpygui()
    dpg.destroy_context()
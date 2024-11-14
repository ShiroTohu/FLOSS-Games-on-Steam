import dearpygui.dearpygui as dpg
import validators
import requests
from bs4 import BeautifulSoup

dpg.create_context()

tags = {
    "windows": r"![Static Badge](https://img.shields.io/badge/Windows-2f81f7?style=for-the-badge&logo=windows10&logoColor=white)",
    "mac": r"![Static Badge](https://img.shields.io/badge/MacOS-f0f0f0?style=for-the-badge&logo=apple&logoColor=black)",
    "steam": r"![Static Badge](https://img.shields.io/badge/SteamOS%2FLinux-%23272932?style=for-the-badge&logo=steam)"
}


class Steam:
    def __init__(self, link):
        self.link = link

    def get_images(self) -> list:
        result = {}

        response = requests.get(self.link)
        soup = BeautifulSoup(response.content, "html.parser")
        stats = soup.find_all('div', {'class': 'screenshot_holder'})

        print(stats)

    @staticmethod
    def validate_url():
        pass


class SoftwareContainer:
    instances = []
    steam_tags = []
    github_tags = []

    @staticmethod
    def add_software_container():
        # Alternative Constructor for creating new instances of the Software Container.
        container = SoftwareContainer()
        container.create()

    def __init__(self, parent="software_container"):
        self.parent = parent
        self.instances.append(self)

        self.tag = dpg.generate_uuid() # generates a unique tag.
        self.steam_tag = dpg.generate_uuid()
        self.github_tag = dpg.generate_uuid()
        self.payload_tag = dpg.generate_uuid()

        self.steam_tags.append(self.steam_tag)
        self.github_tags.append(self.github_tag)

    def create(self):
        # with dpg.drag_payload(parent=self.parent, drag_data=[self.get_steam_value(), self.get_github_value()], payload_type="list"):
        with dpg.group(parent=self.parent, tag=self.tag):
            dpg.add_input_text(label="Steam URL", tag=self.steam_tag, callback=lambda: dpg.set_value(self.payload_tag, dpg.get_value(self.steam_tag)))
            dpg.add_input_text(label="Repository URL", tag=self.github_tag)

            with dpg.group(horizontal=True):
                dpg.add_button(label="- Remove Game", callback=self.remove)
                dpg.add_button(label="+ Add Game", callback=SoftwareContainer.add_software_container)
                dpg.add_button(label="Preview Section Markdown (Debugging)")

            dpg.add_separator()

            with dpg.drag_payload(drag_data=self.get_steam_value(), payload_type="list"):
                dpg.add_text(self.get_steam_value(), tag=self.payload_tag)

    def set_values(self, s, a) -> None :
        dpg.set_value(self.steam_tag, a[0])
        dpg.set_value(self.github_tag, a[1])

    def remove(self):
        if len(self.instances) > 1:
            self.instances.remove(self)
            self.steam_tags.remove(self.steam_tag)
            self.github_tags.remove(self.github_tag)
            dpg.delete_item(self.tag)

    def get_steam_value(self):
        return dpg.get_value(self.steam_tag)

    def get_github_value(self):
        return dpg.get_value(self.github_tag)
    
    @classmethod
    def get_steam_values(cls):
        return dpg.get_values(cls.steam_tags)

    @classmethod
    def get_github_values(cls):
        return dpg.get_values(cls.github_tags)


def print_me(sender):
    print(f"Menu Item: {sender}")


with dpg.window(label="Debug Menu", tag="debug_menu", show=False):
    dpg.add_text(
        "debug menu",
        wrap = 600
    )
    steam = Steam(r"https://store.steampowered.com/app/753640/Outer_Wilds/")
    dpg.add_button(label="debug 1", callback=steam.get_images)


with dpg.window(label="Markdown to CSV", tag="markdown_convert", show=False):
    dpg.add_text(
        "This tool converts the already existing FLOSS markdown into a CSV file that has the columns 'Steam URL' and 'Github URL'. Rarely will this  tool be used, but it is here in case it is needed.",
        wrap = 600
    )
    dpg.add_button(label="Import Markdown", callback=lambda: dpg.show_item("file_dialog_id"))
    dpg.add_file_dialog(
        label="Import Markdown",
        directory_selector=True, show=False, tag="file_dialog_id",
        width=700 ,height=400
    )


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
            dpg.add_menu_item(label="Debug Menu", callback=lambda: dpg.show_item("debug_menu"))

        dpg.add_menu_item(label="Help", callback=print_me)

    with dpg.group(tag="software_container"):
        SoftwareContainer.add_software_container()

    dpg.add_button(label="Generate", callback=SoftwareContainer.get_steam_values)


dpg.create_viewport(title='Markdown Generator', width=800, height=720, resizable=True)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("primary_window", True)
dpg.start_dearpygui()
dpg.destroy_context()
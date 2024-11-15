import dearpygui.dearpygui as dpg

class SoftwareForum:
    def add_software_forum(sender):
        """
        Shows the software forum window.

        Args:
            sender (_type_): The callback sender's tag.
        """
        steam_tag = dpg.generate_uuid()
        github_tag = dpg.generate_uuid()

        with dpg.window(label="Software Forum", show=True):
            dpg.add_text(
                "This is the software forum. Here you can add software that is open source and free to use. This includes games, applications, and other software that is free to use.",
                wrap = 600
            )

            dpg.add_separator()
            dpg.add_text("Required Fields: *")

            dpg.add_input_text(
                label="Steam URL*", 
                tag=steam_tag, 
            )

            dpg.add_input_text(
                label="GitHub URL*", 
                tag=github_tag, 
            )

            dpg.add_text(
                "Images will be fetched from the Steam URL and can be choosen by the user. (By default, the first three images are selected.)",
                wrap = 600
            )
            dpg.add_button(label="Fetch Images")

            dpg.add_separator()

            dpg.add_text("Additional URLS:")
            with dpg.group():
                with dpg.group(horizontal=True):
                    dpg.add_input_text()
                    dpg.add_input_text(width=100)   
                
                dpg.add_button(label="+")        

            dpg.add_separator()  

            dpg.add_button(label="Add Software!")


# class SoftwareForum:
#     instances = []
#     steam_tags = []
#     github_tags = []

#     @staticmethod
#     def show_software_container():
#         # Alternative Constructor for creating new instances of the Software Container.
#         container = SoftwareForum()
#         container.create()

#     def __init__(self, parent="software_container"):
#         self.parent = parent
#         self.instances.append(self)

#         self.tag = dpg.generate_uuid() # generates a unique tag.
#         self.steam_tag = dpg.generate_uuid()
#         self.github_tag = dpg.generate_uuid()
#         self.payload_tag = dpg.generate_uuid()

#         self.steam_tags.append(self.steam_tag)
#         self.github_tags.append(self.github_tag)

#     def create(self):
#         with dpg.group(parent=self.parent, tag=self.tag):
#             dpg.add_input_text(
#                 label="Steam URL*", 
#                 tag=self.steam_tag, 
#                 callback=lambda: dpg.set_value(self.payload_tag, dpg.get_value(self.steam_tag))
#             )
#             dpg.add_input_text(label="Repository URL*", tag=self.github_tag)
#             dpg.add_input_text(label="License URL")

#             with dpg.group(horizontal=True):
#                 dpg.add_button(label="- Remove Game", callback=self.remove)
#                 dpg.add_button(label="+ Add Game", callback=SoftwareForum.add_software_container)
#                 dpg.add_button(label="Preview Section Markdown (Debugging)")

#             dpg.add_separator()

#             with dpg.drag_payload(drag_data=self.get_steam_value(), payload_type="list"):
#                 dpg.add_text(self.get_steam_value(), tag=self.payload_tag)

#     def set_values(self, s, a) -> None :
#         dpg.set_value(self.steam_tag, a[0])
#         dpg.set_value(self.github_tag, a[1])

#     def remove(self):
#         if len(self.instances) > 1:
#             self.instances.remove(self)
#             self.steam_tags.remove(self.steam_tag)
#             self.github_tags.remove(self.github_tag)
#             dpg.delete_item(self.tag)

#     def get_steam_value(self):
#         return dpg.get_value(self.steam_tag)

#     def get_github_value(self):
#         return dpg.get_value(self.github_tag)
    
#     @classmethod
#     def get_steam_values(cls):
#         return dpg.get_values(cls.steam_tags)

#     @classmethod
#     def get_github_values(cls):
#         return dpg.get_values(cls.github_tags)
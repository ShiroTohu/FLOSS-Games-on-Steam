import dearpygui.dearpygui as dpg

from API.steam import Steam

class Debug:
    """Debugging menu for the application.
    """
    def show_debug_menu(sender):
        with dpg.window(label="Debug Menu", tag="debug_menu", show=False):
            dpg.add_text(
                "debug menu",
                wrap = 600
            )
            steam = Steam(r"https://store.steampowered.com/app/753640/Outer_Wilds/")
            dpg.add_button(label="debug 1", callback=steam.get_images)
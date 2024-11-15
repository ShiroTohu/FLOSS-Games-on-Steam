import dearpygui.dearpygui as dpg

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
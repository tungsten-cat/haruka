
import kernel.handlers.json as json_handler
import kernel.handlers.importer as import_handler

class VoiceAssistant:
    def __init__(self):
        pass

    def setup_modules(self, modules_file):
        modules_list = json_handler.get_file_content(modules_file)

        for module in modules_list:
            import_handler.import_module(modules_list[module])

    def setup_commands(self, commands_file):
        pass
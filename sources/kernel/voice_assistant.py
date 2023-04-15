
import handlers.filesystem
import handlers.json
import handlers.importer

class VoiceAssistant:
    def __init__(self):
        pass

    def setup_modules(self, modules_file):
        modules_list = handlers.json.get_file_content(modules_file)

        for module in modules_list:
            handlers.importer.import_module(modules_list[module])
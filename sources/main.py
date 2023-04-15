
import kernel.voice_assistant

VOICE_ASSISTANT = kernel.voice_assistant.VoiceAssistant()

import os

CURRENT_DIR = os.getcwd()

VA_MODULES_LIST = os.path.join(CURRENT_DIR, "sources", "modules.json")
VA_COMMANDS_LIST = os.path.join(CURRENT_DIR, "sources", "commands.json")

if __name__ == "__main__":
    VOICE_ASSISTANT.setup_modules(VA_MODULES_LIST)
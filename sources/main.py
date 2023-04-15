
import kernel.voice_assistant

VOICE_ASSISTANT = kernel.voice_assistant.VoiceAssistant()

# Importing module for working with OS API
import os
# Importing module for working with ENV files
import dotenv

# Looking for ENV configuration file
dotenv_config = dotenv.find_dotenv()
# Loading variables from ENV configuration file
dotenv.load_dotenv(dotenv_config)

# Setting variable for configuring PROJECT_MODE (i.e. DEBUG or RELEASE)
PROJECT_CONFIG = os.environ.get("PROJECT_CONFIG")

CURRENT_DIR = os.getcwd()

VA_COMMANDS_LIST = os.path.join(CURRENT_DIR, "sources", "commands.json")
VA_MODULES_LIST = os.path.join(CURRENT_DIR, "sources", "modules.json")

if PROJECT_CONFIG == "DEBUG":
    print(f"Commands configuration file: {VA_COMMANDS_LIST}")
    print(f"Modules configuration file: {VA_MODULES_LIST}")

if __name__ == "__main__":
    VOICE_ASSISTANT.setup_modules(VA_MODULES_LIST)
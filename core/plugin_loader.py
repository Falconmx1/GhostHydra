import os
import importlib

def load_plugins():
    plugins = {}
    modules_path = "modules"

    for file in os.listdir(modules_path):
        if file.endswith(".py") and not file.startswith("__"):
            name = file[:-3]
            module = importlib.import_module(f"{modules_path}.{name}")

            if hasattr(module, "attack"):
                plugins[name] = module

    return plugins

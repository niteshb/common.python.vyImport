import importlib.util
import os

def vyLoadModuleFromFilePath(filePath, moduleName=None):
    if moduleName == None:
        replacements = [
            ('/', '.'),
            ('\\', '.'),
            ('-', '_'),
            (' ', '_'),
        ]
        filePathSansExt = os.path.splitext(filePath)[0]
        for issue, replacement in replacements:
            filePathSansExt = filePathSansExt.replace(issue, replacement)
        moduleName = filePathSansExt

    spec = importlib.util.spec_from_file_location(moduleName, filePath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

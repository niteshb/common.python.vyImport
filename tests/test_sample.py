from vyImport import vyLoadModuleFromFilePath

module001 = vyLoadModuleFromFilePath('res/001 module.py')
assert(module001.config == 1)
module002 = vyLoadModuleFromFilePath('res/002 module.py')
assert(module002.config == {'test': 'success'})

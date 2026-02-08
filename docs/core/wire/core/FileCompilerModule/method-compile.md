# FileCompilerModule::compile()

Source: `wire/core/FileCompilerModule.php`

The compile method processes the contents of a file

1. If you want to compile the entire contents of the file, override this method and don't parent::compile().
2. If you only want to compile non-PHP sections of the file, implement the compileMarkup() method instead.

@param string $data

@return string|array

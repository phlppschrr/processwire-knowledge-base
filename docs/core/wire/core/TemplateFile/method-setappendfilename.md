# TemplateFile::setAppendFilename()

Source: `wire/core/TemplateFile.php`

Set a file to append to the template file at render time

@param string $filename

@return bool Returns true on success false if file doesn't exist.

@throws WireException if file doesn't exist (unless throwExceptions is disabled)

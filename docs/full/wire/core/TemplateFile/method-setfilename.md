# TemplateFile::setFilename()

Source: `wire/core/TemplateFile.php`

Sets the template file name, replacing whatever was set in the constructor

@param string $filename Full path and filename to the PHP template file

@return bool true on success, false if file doesn't exist

@throws WireException if file doesn't exist (unless throwExceptions is disabled)

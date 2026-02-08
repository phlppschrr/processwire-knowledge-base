# WireFileTools::fileGetContents()

Source: `wire/core/WireFileTools.php`

Get contents of file

This is the same as PHP’s `file_get_contents()` except that the arguments are simpler and
it may be preferable to use this in ProcessWire for future cases where the file system may be
abstracted from the installation.


@param string $filename Full path and filename to read

@param int $offset The offset where the reading starts on the original stream. Negative offsets count from the end of the stream.

@param int $maxlen Maximum length of data read. The default is to read until end of file is reached.

@return bool|string Returns the read data (string) or boolean false on failure.

@since 3.0.167

@see WireFileTools::filePutContents()

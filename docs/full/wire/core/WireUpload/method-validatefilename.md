# WireUpload::validateFilename()

Source: `wire/core/WireUpload.php`

Sanitize/validate a given filename

@param string $value Filename

@param array $extensions Allowed file extensions

@return bool|string Returns boolean false if invalid or string of potentially modified filename if valid

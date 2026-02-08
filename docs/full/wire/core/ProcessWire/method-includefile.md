# ProcessWire::includeFile()

Source: `wire/core/ProcessWire.php`

Include a PHP file, giving it all PW API varibles in scope

File is executed in the directory where it exists.

@param string $file Full path and filename

@param array $data Associative array of any extra data to pass along to include file as locally scoped vars

@return bool True if file existed and was included, false if not.

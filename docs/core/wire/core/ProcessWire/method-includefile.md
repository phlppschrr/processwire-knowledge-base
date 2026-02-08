# $processWire->includeFile($file, array $data = array()): bool

Source: `wire/core/ProcessWire.php`

Include a PHP file, giving it all PW API varibles in scope

File is executed in the directory where it exists.

## Arguments

- string $file Full path and filename
- array $data Associative array of any extra data to pass along to include file as locally scoped vars

## Return value

bool True if file existed and was included, false if not.

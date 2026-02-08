# $fileLog->__construct($path, $identifier = '')

Source: `wire/core/FileLog.php`

Construct the FileLog

## Usage

~~~~~
// basic usage
$result = $fileLog->__construct($path);

// usage with all arguments
$result = $fileLog->__construct($path, $identifier = '');
~~~~~

## Arguments

- `$path` `string` Path where the log will be stored (path should have trailing slash) This may optionally include the filename if you intend to leave the second param blank.
- `$identifier` (optional) `string` Basename for the log file, not including the extension.

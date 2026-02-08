# $sanitizer->filename($value, $beautify = false, $maxLength = 128): string

Source: `wire/core/Sanitizer.php`

Name filter for ProcessWire filenames (basenames only, not paths)

This sanitizes a filename to be consistent with the name format in ProcessWire,
ASCII-alphanumeric (a-z A-Z 0-9), hyphens, underscores and periods. Note that
filenames may contain mixed case (a-z A-Z) so if you require lowercase then
run the return value through a `strtolower()` function.

~~~~~
// outputs: FileName.jpg
echo $sanitizer->filename('©®™FileName.jpg');

// outputs: c_r_tmfilename.jpg
echo strtolower($sanitizer->filename('©®™filename.jpg', Sanitizer::translate));
~~~~~

## Arguments

- string $value Filename to sanitize
- bool|int $beautify Should be true when creating a file's name for the first time. Default is false. You may also specify Sanitizer::translate (or number 2) for the $beautify param, which will make it translate letters based on the InputfieldPageName custom config settings.
- int $maxLength Maximum number of characters allowed in the filename

## Return value

string Sanitized filename

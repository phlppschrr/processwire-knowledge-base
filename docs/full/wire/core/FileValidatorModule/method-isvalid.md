# $fileValidatorModule->isValid($filename): bool|int

Source: `wire/core/FileValidatorModule.php`

Is the given file valid?

FileValidator modules should not implement this method, as it only serves as a front-end to isValid()
for logging purposes.

## Usage

~~~~~
// basic usage
$bool = $fileValidatorModule->isValid($filename);
~~~~~

## Arguments

- `$filename` `string`

## Return value

- `bool|int` Returns TRUE if valid, FALSE if not, or integer 1 if valid as a result of sanitization.

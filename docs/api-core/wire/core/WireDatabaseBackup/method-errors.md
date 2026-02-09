# $wireDatabaseBackup->errors($reset = false): array

Source: `wire/core/WireDatabaseBackup.php`

Return all error messages that occurred

## Usage

~~~~~
// basic usage
$array = $wireDatabaseBackup->errors();

// usage with all arguments
$array = $wireDatabaseBackup->errors($reset = false);
~~~~~

## Arguments

- `$reset` (optional) `bool` Specify true to clear out existing errors or omit just to return error messages

## Return value

- `array`

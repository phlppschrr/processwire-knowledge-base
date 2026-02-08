# $wireFileTools->size($path, $options = array()): int|string

Source: `wire/core/WireFileTools.php`

Get size of file or directory (in bytes)

## Usage

~~~~~
// basic usage
$int = $wireFileTools->size($path);

// usage with all arguments
$int = $wireFileTools->size($path, $options = array());
~~~~~

## Arguments

- `$path` `string` File or directory path
- `$options` (optional) `array|bool` Options array, or boolean true for getString option: - `getString` (bool): Get string that summarizes bytes, kB, MB, etc.? (default=false)

## Return value

- `int|string`

## Since

3.0.214

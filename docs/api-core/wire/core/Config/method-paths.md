# $config->paths($for = ''): null|string|Paths

Source: `wire/core/Config.php`

Get disk path for requested resource or module or get all paths if no argument

## Usage

~~~~~
// basic usage
$config->paths();

// usage with all arguments
$config->paths($for = '');
~~~~~

## Arguments

- `$for` (optional) `string` Predefined ProcessWire paths property or module name

## Return value

- `null|string|Paths`

## Since

3.0.130

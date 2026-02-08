# $wireHttp->downloadCURL($fromURL, $fp, array $options): bool

Source: `wire/core/WireHttp.php`

Download file using CURL

## Usage

~~~~~
// basic usage
$bool = $wireHttp->downloadCURL($fromURL, $fp, $options);

// usage with all arguments
$bool = $wireHttp->downloadCURL($fromURL, $fp, array $options);
~~~~~

## Arguments

- `$fromURL` `string`
- `$fp` `resource` Open file pointer
- `$options` `array`

## Return value

- `bool` True if successful false if not

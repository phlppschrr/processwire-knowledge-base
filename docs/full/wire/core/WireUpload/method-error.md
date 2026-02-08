# $wireUpload->error($text, $flags = 0): Wire|WireUpload

Source: `wire/core/WireUpload.php`

Record an error message

## Usage

~~~~~
// basic usage
$wire = $wireUpload->error($text);

// usage with all arguments
$wire = $wireUpload->error($text, $flags = 0);
~~~~~

## Arguments

- `$text` `array|Wire|string`
- `$flags` (optional) `int`

## Return value

- `Wire|WireUpload`

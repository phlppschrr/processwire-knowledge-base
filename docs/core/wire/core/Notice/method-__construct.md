# $notice->__construct($text, $flags = 0)

Source: `wire/core/Notice.php`

Create the Notice

As of version 3.0.149 the $flags argument can also be specified as a space separated
string or array of flag names. Previous versions only accepted flags integer.

## Usage

~~~~~
// basic usage
$result = $notice->__construct($text);

// usage with all arguments
$result = $notice->__construct($text, $flags = 0);
~~~~~

## Arguments

- `$text` `string` Notification text
- `$flags` (optional) `int|string|array` Flags Flags for Notice

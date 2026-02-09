# $sanitizer->removeNewlines($str, $replacement = ' '): string

Source: `wire/core/Sanitizer.php`

Remove newlines from the given string and return it

## Usage

~~~~~
// basic usage
$string = $sanitizer->removeNewlines($str);

// usage with all arguments
$string = $sanitizer->removeNewlines($str, $replacement = ' ');
~~~~~

## Arguments

- `$str` `string` String to remove newlines from
- `$replacement` (optional) `string` Character to replace newlines with (default=" ")

## Return value

- `string` String without newlines

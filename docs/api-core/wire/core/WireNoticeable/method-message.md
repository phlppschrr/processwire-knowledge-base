# $wireNoticeable->message($text, $flags = 0): $this

Source: `wire/core/Interfaces.php`

Record an informational or 'success' message in the system-wide notices.

This method automatically identifies the message as coming from this class.

## Usage

~~~~~
// basic usage
$result = $wireNoticeable->message($text);

// usage with all arguments
$result = $wireNoticeable->message($text, $flags = 0);
~~~~~

## Arguments

- `$text` `string`
- `$flags` (optional) `int` See Notices::flags

## Return value

- `$this`

# $session->message($text, $flags = 0): $this

Source: `wire/core/Session.php`

Queue a message to appear on the next pageview

## Usage

~~~~~
// basic usage
$result = $session->message($text);

// usage with all arguments
$result = $session->message($text, $flags = 0);
~~~~~

## Arguments

- `$text` `string` Message to queue
- `$flags` (optional) `int` Optional flags, See Notice::flags

## Return value

- `$this`

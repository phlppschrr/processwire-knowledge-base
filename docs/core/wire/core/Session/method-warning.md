# $session->warning($text, $flags = 0): $this

Source: `wire/core/Session.php`

Queue a warning to appear the next pageview

## Usage

~~~~~
// basic usage
$result = $session->warning($text);

// usage with all arguments
$result = $session->warning($text, $flags = 0);
~~~~~

## Arguments

- `$text` `string` Warning to queue
- `$flags` (optional) `int` See Notice::flags

## Return value

- `$this`

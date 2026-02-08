# $session->error($text, $flags = 0): $this

Source: `wire/core/Session.php`

Queue an error to appear on the next pageview

## Usage

~~~~~
// basic usage
$result = $session->error($text);

// usage with all arguments
$result = $session->error($text, $flags = 0);
~~~~~

## Arguments

- `$text` `string` Error to queue
- `$flags` (optional) `int` See Notice::flags

## Return value

- `$this`

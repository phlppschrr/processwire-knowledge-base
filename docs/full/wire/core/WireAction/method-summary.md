# $wireAction->summary($text = null): string

Source: `wire/core/WireAction.php`

Get or set a text summary of what this action did

## Usage

~~~~~
// basic usage
$string = $wireAction->summary();

// usage with all arguments
$string = $wireAction->summary($text = null);
~~~~~

## Arguments

- `$text` (optional) `string|null` Set the summary or omit to only retrieve the summary

## Return value

- `string` Always returns the current summary text or blank string if not set

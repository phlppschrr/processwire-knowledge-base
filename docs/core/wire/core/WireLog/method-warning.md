# $wireLog->warning($text, $flags = 0): Wire|WireLog

Source: `wire/core/WireLog.php`

Record a warning message in the warnings log (warnings.txt)

## Example

~~~~~
// Log an warning message to warnings.txt log
$log->warning("This is a warning");
~~~~~

## Usage

~~~~~
// basic usage
$wire = $wireLog->warning($text);

// usage with all arguments
$wire = $wireLog->warning($text, $flags = 0);
~~~~~

## Arguments

- `$text` `string` Text to save in the log
- `$flags` (optional) `int|bool` Specify boolean true to also display the warning interactively (admin only).

## Return value

- `Wire|WireLog`

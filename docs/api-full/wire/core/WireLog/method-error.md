# $wireLog->error($text, $flags = 0): Wire|WireLog

Source: `wire/core/WireLog.php`

Record an error message in the error log (errors.txt)

Note: Fatal errors should instead always throw a WireException.

## Example

~~~~~
// Log an error message to errors.txt log
$log->error("Login attempt failed");
~~~~~

## Usage

~~~~~
// basic usage
$wire = $wireLog->error($text);

// usage with all arguments
$wire = $wireLog->error($text, $flags = 0);
~~~~~

## Arguments

- `$text` `string` Text to save in the log
- `$flags` (optional) `int|bool` Specify boolean true to also display the error interactively (admin only).

## Return value

- `Wire|WireLog`

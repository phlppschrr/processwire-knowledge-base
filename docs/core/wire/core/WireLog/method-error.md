# $wireLog->error($text, $flags = 0): Wire|WireLog

Source: `wire/core/WireLog.php`

Record an error message in the error log (errors.txt)

Note: Fatal errors should instead always throw a WireException.

~~~~~
// Log an error message to errors.txt log
$log->error("Login attempt failed");
~~~~~

## Arguments

- string $text Text to save in the log
- int|bool $flags Specify boolean true to also display the error interactively (admin only).

## Return value

Wire|WireLog

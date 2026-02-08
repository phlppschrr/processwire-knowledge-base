# $wireLog->warning($text, $flags = 0): Wire|WireLog

Source: `wire/core/WireLog.php`

Record a warning message in the warnings log (warnings.txt)

~~~~~
// Log an warning message to warnings.txt log
$log->warning("This is a warning");
~~~~~

## Arguments

- string $text Text to save in the log
- int|bool $flags Specify boolean true to also display the warning interactively (admin only).

## Return value

Wire|WireLog

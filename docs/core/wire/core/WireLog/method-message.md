# $wireLog->message($text, $flags = 0): Wire|WireLog

Source: `wire/core/WireLog.php`

Record an informational or 'success' message in the message log (messages.txt)

~~~~~
// Log message to messages.txt log
$log->message("User updated profile");
~~~~~

## Arguments

- `$text` `string` Message to log
- `$flags` (optional) `bool|int` Specify boolean true to also have the message displayed interactively (admin only).

## Return value

Wire|WireLog

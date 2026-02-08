# WireLog::message()

Source: `wire/core/WireLog.php`

Record an informational or 'success' message in the message log (messages.txt)

~~~~~
// Log message to messages.txt log
$log->message("User updated profile");
~~~~~

@param string $text Message to log

@param bool|int $flags Specify boolean true to also have the message displayed interactively (admin only).

@return Wire|WireLog

# WireLog::warning()

Source: `wire/core/WireLog.php`

Record a warning message in the warnings log (warnings.txt)

~~~~~
// Log an warning message to warnings.txt log
$log->warning("This is a warning");
~~~~~

@param string $text Text to save in the log

@param int|bool $flags Specify boolean true to also display the warning interactively (admin only).

@return Wire|WireLog

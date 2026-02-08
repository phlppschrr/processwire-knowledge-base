# Wire::___log()

Source: `wire/core/Wire.php`

Log a message for this class

Message is saved to a log file in ProcessWire's logs path to a file with
the same name as the class, converted to hyphenated lowercase. For example,
a class named `MyWidgetData` would have a log named `my-widget-data.txt`.

~~~~~
$this->log("This message will be logged");
~~~~~


@param string $str Text to log, or omit to return the `$log` API variable.

@param array $options Optional extras to include:
 - `url` (string): URL to record the with the log entry (default=auto-detect)
 - `name` (string): Name of log to use (default=auto-detect)
 - `user` (User|string|null): User instance, user name, or null to log for current User. (default=null)

@return WireLog

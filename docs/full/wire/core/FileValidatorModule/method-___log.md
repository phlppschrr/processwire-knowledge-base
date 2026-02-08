# $fileValidatorModule->___log($str = '', array $options = array()): WireLog|null

Source: `wire/core/FileValidatorModule.php`

Log a message for this class

Message is saved to a log file in ProcessWire's logs path to a file with
the same name as the class, converted to hyphenated lowercase.

## Arguments

- string $str Text to log, or omit to just return the name of the log
- array $options Optional extras to include: - url (string): URL to record the with the log entry (default=auto-detect) - name (string): Name of log to use (default=auto-detect)

## Return value

WireLog|null

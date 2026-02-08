# $fileLog->isValidLine($line, array $options, &$stopNow): bool

Source: `wire/core/FileLog.php`

Returns whether the given log line is valid to be considered a log entry

## Usage

~~~~~
// basic usage
$bool = $fileLog->isValidLine($line, $options, $stopNow);

// usage with all arguments
$bool = $fileLog->isValidLine($line, array $options, &$stopNow);
~~~~~

## Arguments

- $line
- `$options` `array`
- `$stopNow` `bool` Populates this with true when it can determine no more lines are necessary.

## Return value

- `bool` Returns boolean true if valid, false if not.

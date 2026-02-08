# $wire->log($str = '', array $options = array()): WireLog

Source: `wire/core/Wire.php`

Log a message for this class

Message is saved to a log file in ProcessWire's logs path to a file with
the same name as the class, converted to hyphenated lowercase. For example,
a class named `MyWidgetData` would have a log named `my-widget-data.txt`.

## Example

~~~~~
$this->log("This message will be logged");
~~~~~

## Usage

~~~~~
// basic usage
$wireLog = $wire->log();

// usage with all arguments
$wireLog = $wire->log($str = '', array $options = array());
~~~~~

## Hookable

- Hookable method name: `log`
- Implementation: `___log`
- Hook with: `$wire->log()`

## Arguments

- `$str` (optional) `string` Text to log, or omit to return the `$log` API variable.
- `$options` (optional) `array` Optional extras to include: - `url` (string): URL to record the with the log entry (default=auto-detect) - `name` (string): Name of log to use (default=auto-detect) - `user` (User|string|null): User instance, user name, or null to log for current User. (default=null)

## Return value

- `WireLog`

# $wireLog->___save($name, $text, $options = array()): bool

Source: `wire/core/WireLog.php`

Save text to a named log

- If the log doesn't currently exist, it will be created.
- The log filename is `/site/assets/logs/[name].txt`
- Logs can be viewed in the admin at Setup > Logs

## Example

~~~~~
// Save text searches to custom log file (search.txt):
$log->save("search", "User searched for: $phrase");
~~~~~

## Usage

~~~~~
// basic usage
$bool = $wireLog->___save($name, $text);

// usage with all arguments
$bool = $wireLog->___save($name, $text, $options = array());
~~~~~

## Arguments

- `$name` `string` Name of log to save to (word consisting of only `[-._a-z0-9]` and no extension)
- `$text` `string` Text to save to the log
- `$options` (optional) `array` Options to modify default behavior: - `showUser` (bool): Include the username in the log entry? (default=true) - `showURL` (bool): Include the current URL in the log entry? (default=true) - `user` (User|string|null): User instance, user name, or null to use current User. (default=null) - `url` (bool): URL to record with the log entry (default=auto determine) - `delimiter` (string): Log entry delimiter (default="\t" aka tab)

## Return value

- `bool` Whether it was written or not (generally always going to be true)

## Exceptions

- `WireException`

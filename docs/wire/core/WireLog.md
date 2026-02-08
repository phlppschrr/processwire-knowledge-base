# WireLog

Source: `wire/core/WireLog.php`

ProcessWire Log

WireLog represents the ProcessWire $log API variable.
It is an API-friendly interface to the FileLog class.

Enables creation of logs, logging of events, and management of logs.

ProcessWire 3.x, Copyright 2023 by Ryan Cramer
https://processwire.com


@todo option to disable logs by name

## other

@method bool save($name, $text, $options = array())

## message()

Record an informational or 'success' message in the message log (messages.txt)

~~~~~
// Log message to messages.txt log
$log->message("User updated profile");
~~~~~

@param string $text Message to log

@param bool|int $flags Specify boolean true to also have the message displayed interactively (admin only).

@return Wire|WireLog

## error()

Record an error message in the error log (errors.txt)

Note: Fatal errors should instead always throw a WireException.

~~~~~
// Log an error message to errors.txt log
$log->error("Login attempt failed");
~~~~~

@param string $text Text to save in the log

@param int|bool $flags Specify boolean true to also display the error interactively (admin only).

@return Wire|WireLog

## warning()

Record a warning message in the warnings log (warnings.txt)

~~~~~
// Log an warning message to warnings.txt log
$log->warning("This is a warning");
~~~~~

@param string $text Text to save in the log

@param int|bool $flags Specify boolean true to also display the warning interactively (admin only).

@return Wire|WireLog

## ___save()

Save text to a named log

- If the log doesn't currently exist, it will be created.
- The log filename is `/site/assets/logs/[name].txt`
- Logs can be viewed in the admin at Setup > Logs

~~~~~
// Save text searches to custom log file (search.txt):
$log->save("search", "User searched for: $phrase");
~~~~~

@param string $name Name of log to save to (word consisting of only `[-._a-z0-9]` and no extension)

@param string $text Text to save to the log

@param array $options Options to modify default behavior:
  - `showUser` (bool): Include the username in the log entry? (default=true)
  - `showURL` (bool): Include the current URL in the log entry? (default=true)
  - `user` (User|string|null): User instance, user name, or null to use current User. (default=null)
  - `url` (bool): URL to record with the log entry (default=auto determine)
  - `delimiter` (string): Log entry delimiter (default="\t" aka tab)

@return bool Whether it was written or not (generally always going to be true)

@throws WireException

## getLogs()

Return array of all logs, sorted by name

Each item in returned array is an associative array that includes the following:

	- `name` (string): Name of log file, excluding extension.
	- `file` (string): Full path and filename of log file.
	- `size` (int): Size in bytes
	- `modified` (int): Last modified date (unix timestamp)


@param bool $sortNewest Sort by newest to oldest rather than by name? (default=false) Added 3.0.143

@return array Indexed by log name

## getFilename()

Get the full filename (including path) for the given log name


@param string $name Name of log (not including extension)

@return string Filename to log file

@throws WireException If given invalid log name

## exists()

Does given log name exist?

@param string $name

@return bool

@since 3.0.176

## getLines()

Return the given number of entries from the end of log file

This method is pagination aware.


@param string $name Name of log

@param array $options Specify any of the following:
	- `limit` (integer): Specify number of lines (default=100)
	- `text` (string): Text to find.
	- `dateFrom` (int|string): Oldest date to match entries.
	- `dateTo` (int|string): Newest date to match entries.
	- `reverse` (bool): Reverse order (default=true)
	- `pageNum` (int): Pagination number 1 or above (default=0 which means auto-detect)

@return array

@see WireLog::getEntries()

## getEntries()

Return given number of entries from end of log file, with each entry as an associative array of components

This is effectively the same as the `getLines()` method except that each entry is an associative
array rather than a single line (string). This method is pagination aware.


@param string $name Name of log file (excluding extension)

@param array $options Optional options to modify default behavior:
	- `limit` (integer): Specify number of lines (default=100)
	- `text` (string): Text to find.
	- `dateFrom` (int|string): Oldest date to match entries.
	- `dateTo` (int|string): Newest date to match entries.
	- `reverse` (bool): Reverse order (default=true)
	- `pageNum` (int): Pagination number 1 or above (default=0 which means auto-detect)

@return array Returns an array of associative arrays, each with the following components:
 - `date` (string): ISO-8601 date string
 - `user` (string): user name or boolean false if unknown
 - `url` (string): full URL or boolean false if unknown
 - `text` (string): text of the log entry

@see WireLog::getLines()

## getTotalEntries()

Get the total number of entries present in the given log


@param string $name Name of log, not including path or extension

@return int Total number of entries

## delete()

Delete a log file


@param string $name Name of log, excluding path and extension.

@return bool True on success, false on failure.

## deleteAll()

Delete all log files

@param bool $throw Throw WireException if any delete fails? (default=false)

@return array Basenames of deleted log files

@since 3.0.214

## prune()

Prune log file to contain only entries from last [n] days


@param string $name Name of log file, excluding path and extension.

@param int $days Number of days

@return int Number of items in newly pruned log file or boolean false on failure

@throws WireException

## pruneAll()

Prune all log files to given number of days

@param int $days

@return array

@since 3.0.214

## disable()

Disable the given log name temporarily so that save() calls do not record entries during this request

@param string $name Log name or specify '*' to disable all

@return self

@since 3.0.148

@see WireLog::enable()

## enable()

Enable a previously disabled log

@param string $name Log name or specify '*' to reverse a previous disable('*') call.

@return self

@since 3.0.148

@see WireLog::disable()

## path()

Return disk path to log files

@return string

@since 3.0.214

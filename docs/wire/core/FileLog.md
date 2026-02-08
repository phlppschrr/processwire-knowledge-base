# FileLog

Source: `wire/core/FileLog.php`

ProcessWire FileLog

Creates and maintains a text-based log file.

ProcessWire 3.x, Copyright 2023 by Ryan Cramer
https://processwire.com

## defaultChunkSize

Default size of chunks used for reading from logs

## debug

Debug mode used during development of this class

## __construct()

Construct the FileLog

@param string $path Path where the log will be stored (path should have trailing slash)
	This may optionally include the filename if you intend to leave the second param blank.

@param string $identifier Basename for the log file, not including the extension.

## wired()

Wired to API

## __get()

@param string $name

@return mixed

## cleanStr()

Clean a string for use in a log file entry

@param $str

@return string

## save()

Save the given log entry string

@param string $str

@param array $options options to modify behavior (Added 3.0.143)
 - `allowDups` (bool): Allow duplicating same log entry in same runtime/request? (default=true)
 - `mergeDups` (int): Merge previous duplicate entries that also appear near end of file?
    To enable, specify int for quantity of bytes to consider from EOF, value of 1024 or higher (default=0, disabled)
 - `maxTries` (int): If log entry fails to save, maximum times to re-try (default=20)
 - `maxTriesDelay` (int): Micro seconds (millionths of a second) to delay between re-tries (default=2000)

@return bool Success state: true if log written, false if not.

## removeLineFromChunk()

Remove given $line from $chunk and add counter to end of $line indicating quantity that was removed

@param string $line

@param string $chunk

@param int $chunkSize

@since 3.0.143

## size()

Get filesize

@return int|false

## filename()

Get file basename

@return string

## pathname()

Get file pathname

@return string|bool

## mtime()

Get file modification time

@return int|false

## get()

Get lines from the end of a file based on chunk size (deprecated)

@param int $chunkSize

@param int $chunkNum

@return array

@deprecated Use find() instead

## getChunkArray()

Get lines from the end of a file based on chunk size

@param int $chunkSize

@param int $chunkNum

@param bool $reverse

@return array

## getChunk()

Get a chunk of data (string) from the end of the log file

Returned string is automatically adjusted at the beginning and
ending to contain only full log lines.

@param int $chunkNum Current chunk/pagination number (default=1, first)

@param int $chunkSize Number of bytes to retrieve (default=0, which assigns default chunk size of 12288)

@param bool $reverse True=pull from end of file, false=pull from beginning (default=true)

@param bool $clean Get a clean chunk that starts at the beginning of a line? (default=true)

@return string

## getTotalChunks()

Get the total number of chunks in the file

@param int $chunkSize

@return int

## getTotalLines()

Get total number of lines in the log file

@return int

## getDate()

Get log lines that lie within a date range

@param int $dateFrom Starting date (unix timestamp or strtotime compatible string)

@param int $dateTo Ending date (unix timestamp or strtotime compatible string)

@param int $pageNum Current pagination number (default=1)

@param int $limit Items per pagination (default=100), or specify 0 for no limit.

@return array

## find()

Return lines from the end of the log file, with various options

@param int $limit Number of items to return (per pagination), or 0 for no limit.

@param int $pageNum Current pagination (default=1)

@param array $options
	- text (string): Return only lines containing the given string of text
	- reverse (bool): True=find from end of file, false=find from beginning (default=true)
	- toFile (string): Send results to the given basename (default=none)
	- dateFrom (unix timestamp): Return only lines newer than the given date (default=oldest)
	- dateTo (unix timestamp): Return only lines older than the given date  (default=now)
		Note: dateFrom and dateTo may be combined to return a range.

@return int|array of strings (associative), each indexed by string containing slash separated
	numeric values of: "current/total/start/end/total" which is useful with pagination.
	If the 'toFile' option is used, then return value is instead an integer qty of lines written.

@throws \Exception on fatal error

## isValidLine()

Returns whether the given log line is valid to be considered a log entry

@param $line

@param array $options

@param bool $stopNow Populates this with true when it can determine no more lines are necessary.

@return bool Returns boolean true if valid, false if not.

## prune()

Prune to number of bytes

@param $bytes

@return bool|int

@deprecated use pruneBytes() or pruneLines() instead

## pruneBytes()

Prune log file to specified number of bytes (from the end)

@param int $bytes

@return int|bool positive integer on success, 0 if no prune necessary, or boolean false on failure.

## pruneDate()

Prune log file to contain only entries newer than $oldestDate

@param int|string $oldestDate

@return int Number of lines written

## delete()

Delete the log file

@return bool

## chunkSize()

Get or set the default chunk size used when reading from logs and not overridden by method argument

@param int $chunkSize Specify chunk size to set, or omit to get

@return int

@since 3.0.143

## path()

Get path where the log is stored (with trailing slash)

@return string

# $fileLog->getChunk($chunkNum = 1, $chunkSize = 0, $reverse = true, $clean = true): string

Source: `wire/core/FileLog.php`

Get a chunk of data (string) from the end of the log file

Returned string is automatically adjusted at the beginning and
ending to contain only full log lines.

## Arguments

- int $chunkNum Current chunk/pagination number (default=1, first)
- int $chunkSize Number of bytes to retrieve (default=0, which assigns default chunk size of 12288)
- bool $reverse True=pull from end of file, false=pull from beginning (default=true)
- bool $clean Get a clean chunk that starts at the beginning of a line? (default=true)

## Return value

string

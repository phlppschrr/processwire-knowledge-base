# FileLog::getChunk()

Source: `wire/core/FileLog.php`

Get a chunk of data (string) from the end of the log file

Returned string is automatically adjusted at the beginning and
ending to contain only full log lines.

@param int $chunkNum Current chunk/pagination number (default=1, first)

@param int $chunkSize Number of bytes to retrieve (default=0, which assigns default chunk size of 12288)

@param bool $reverse True=pull from end of file, false=pull from beginning (default=true)

@param bool $clean Get a clean chunk that starts at the beginning of a line? (default=true)

@return string

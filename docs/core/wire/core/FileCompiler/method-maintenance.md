# FileCompiler::maintenance()

Source: `wire/core/FileCompiler.php`

Run maintenance on the FileCompiler cache

This should be called at the end of each request.

@param int $interval Number of seconds between maintenance runs (default=86400)

@return bool Whether or not it was necessary to run maintenance

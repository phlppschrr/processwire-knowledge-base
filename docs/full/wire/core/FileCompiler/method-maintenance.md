# $fileCompiler->maintenance($interval = 86400): bool

Source: `wire/core/FileCompiler.php`

Run maintenance on the FileCompiler cache

This should be called at the end of each request.

## Arguments

- `$interval` (optional) `int` Number of seconds between maintenance runs (default=86400)

## Return value

bool Whether or not it was necessary to run maintenance

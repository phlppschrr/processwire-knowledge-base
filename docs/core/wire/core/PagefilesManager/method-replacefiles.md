# $pagefilesManager->replaceFiles($fromPath, $move = false): int

Source: `wire/core/PagefilesManager.php`

Replace all page’s files with those from given path

## Arguments

- string $fromPath
- bool $move Move files to destination rather than copy? (default=false)

## Return value

int Number of files/directories copied.

## Throws

- WireException if given a path that does not exist.

## Meta

- @since 3.0.114

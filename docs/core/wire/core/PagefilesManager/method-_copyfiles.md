# $pagefilesManager->_copyFiles($fromPath, $toPath, $rename = false): int

Source: `wire/core/PagefilesManager.php`

Recursively copy all files in $fromPath to $toPath, for internal use

## Arguments

- string $fromPath Path to copy from
- string $toPath Path to copy to
- bool $rename Rename files rather than copy? (makes this perform like a move rather than copy)

## Return value

int Number of files copied

# $pagefilesManager->replaceFiles($fromPath, $move = false): int

Source: `wire/core/PagefilesManager.php`

Replace all page’s files with those from given path

## Usage

~~~~~
// basic usage
$int = $pagefilesManager->replaceFiles($fromPath);

// usage with all arguments
$int = $pagefilesManager->replaceFiles($fromPath, $move = false);
~~~~~

## Arguments

- `$fromPath` `string`
- `$move` (optional) `bool` Move files to destination rather than copy? (default=false)

## Return value

- `int` Number of files/directories copied.

## Exceptions

- `WireException` if given a path that does not exist.

## Since

3.0.114

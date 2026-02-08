# $pagefilesManager->importFiles($fromPath, $move = false): int

Source: `wire/core/PagefilesManager.php`

Copy/import files from given path into the page’s files directory

## Usage

~~~~~
// basic usage
$int = $pagefilesManager->importFiles($fromPath);

// usage with all arguments
$int = $pagefilesManager->importFiles($fromPath, $move = false);
~~~~~

## Arguments

- `$fromPath` `string` Path to copy/import files from.
- `$move` (optional) `bool` Move files into directory rather than copy?

## Return value

- `int` Number of files/directories copied.

## Since

3.0.114

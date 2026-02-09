# $pagefilesManager->copyFiles($toPath): int

Source: `wire/core/PagefilesManager.php`

Recursively copy all files managed by this PagefilesManager into a new path.

## Usage

~~~~~
// basic usage
$int = $pagefilesManager->copyFiles($toPath);
~~~~~

## Arguments

- $toPath string Path to copy files into.

## Return value

- `int` Number of files/directories copied.

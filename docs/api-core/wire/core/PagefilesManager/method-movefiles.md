# $pagefilesManager->moveFiles($toPath): int

Source: `wire/core/PagefilesManager.php`

Recursively move all files managed by this PagefilesManager into a new path.

## Usage

~~~~~
// basic usage
$int = $pagefilesManager->moveFiles($toPath);
~~~~~

## Arguments

- $toPath string Path to move files into.

## Return value

- `int` Number of files/directories moved.

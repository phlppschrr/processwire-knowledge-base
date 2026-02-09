# $pagefilesManager->_copyFiles($fromPath, $toPath, $rename = false): int

Source: `wire/core/PagefilesManager.php`

Recursively copy all files in $fromPath to $toPath, for internal use

## Usage

~~~~~
// basic usage
$int = $pagefilesManager->_copyFiles($fromPath, $toPath);

// usage with all arguments
$int = $pagefilesManager->_copyFiles($fromPath, $toPath, $rename = false);
~~~~~

## Arguments

- `$fromPath` `string` Path to copy from
- `$toPath` `string` Path to copy to
- `$rename` (optional) `bool` Rename files rather than copy? (makes this perform like a move rather than copy)

## Return value

- `int` Number of files copied

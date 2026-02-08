# $pagefilesManager->emptyPath($rmdir = false, $recursive = true): bool

Source: `wire/core/PagefilesManager.php`

Empty out the published files (delete all of them)

## Usage

~~~~~
// basic usage
$bool = $pagefilesManager->emptyPath();

// usage with all arguments
$bool = $pagefilesManager->emptyPath($rmdir = false, $recursive = true);
~~~~~

## Arguments

- `$rmdir` (optional) `bool` Remove the directory too? (default=false)
- `$recursive` (optional) `bool` Recursively do the same for subdirectories? (default=true)

## Return value

- `bool` True on success, false on error (since 3.0.17, previous versions had no return value).

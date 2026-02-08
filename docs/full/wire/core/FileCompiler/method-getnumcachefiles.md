# $fileCompiler->getNumCacheFiles($all = false, $targetPath = null): int

Source: `wire/core/FileCompiler.php`

Get a count of how many files are in the cache

## Usage

~~~~~
// basic usage
$int = $fileCompiler->getNumCacheFiles();

// usage with all arguments
$int = $fileCompiler->getNumCacheFiles($all = false, $targetPath = null);
~~~~~

## Arguments

- `$all` (optional) `bool` Specify true to get a count for all file compiler caches
- `$targetPath` (optional) `string` for internal recursion use, public calls should omit this

## Return value

- `int`

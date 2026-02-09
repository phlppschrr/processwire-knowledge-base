# $cacheFile->setSecondaryID($id)

Source: `wire/core/CacheFile.php`

An extra part to be appended to the filename

When a call to remove the cache is included, then all 'secondary' versions of it will be included too

## Usage

~~~~~
// basic usage
$result = $cacheFile->setSecondaryID($id);
~~~~~

## Arguments

- `$id` `string|int`

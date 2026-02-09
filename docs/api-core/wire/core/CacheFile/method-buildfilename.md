# $cacheFile->buildFilename(): string

Source: `wire/core/CacheFile.php`

Build a filename for use by the cache

Filename takes this form: /path/primaryID/primaryID.cache
Or /path/primaryID/secondaryID.cache

## Usage

~~~~~
// basic usage
$string = $cacheFile->buildFilename();
~~~~~

## Return value

- `string`

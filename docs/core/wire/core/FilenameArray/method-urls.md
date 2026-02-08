# $filenameArray->urls($useVersion = null): array

Source: `wire/core/FilenameArray.php`

Get cache-busting URLs for this FilenameArray

This is the same as iterating this FilenameArray except that it appends cache-busting
query strings to the URLs that resolve to physical files.

## Arguments

- `$useVersion` (optional) `bool|null|string` See Config::versionUrls() for arument details

## Return value

array

## Throws

- WireException

## See also

- [Config::versionUrls()](../Config/method-versionurls.md)

## Since

3.0.227

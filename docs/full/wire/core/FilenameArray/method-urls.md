# $filenameArray->urls($useVersion = null): array

Source: `wire/core/FilenameArray.php`

Get cache-busting URLs for this FilenameArray

This is the same as iterating this FilenameArray except that it appends cache-busting
query strings to the URLs that resolve to physical files.

## Arguments

- bool|null|string $useVersion See Config::versionUrls() for arument details

## Return value

array

## Throws

- WireException

## See also

- [Config::versionUrls()](../Config/method-versionurls.md)

## Meta

- @since 3.0.227

# $config->versionUrl($url, $useVersion = null): string

Source: `wire/core/Config.php`

Given a file asset URLs return it with cache-busting version string

URLs that aready have query strings are left alone.

## Arguments

- `$url` `string` URL to a file asset (such as JS/CSS file)
- `$useVersion` (optional) `bool|null|string` See versionUrls() method for description of this argument.

## Return value

string URL updated with version strings where necessary

## See also

- [Config::versionUrls()](method-versionurls.md)

## Since

3.0.227

# $config->versionUrl($url, $useVersion = null): string

Source: `wire/core/Config.php`

Given a file asset URLs return it with cache-busting version string

URLs that aready have query strings are left alone.

## Arguments

- string $url URL to a file asset (such as JS/CSS file)
- bool|null|string $useVersion See versionUrls() method for description of this argument.

## Return value

string URL updated with version strings where necessary

## See also

- [Config::versionUrls()](method-versionurls.md)

## Meta

- @since 3.0.227

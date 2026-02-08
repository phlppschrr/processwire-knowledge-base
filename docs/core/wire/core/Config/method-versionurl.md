# Config::versionUrl()

Source: `wire/core/Config.php`

Given a file asset URLs return it with cache-busting version string

URLs that aready have query strings are left alone.


@param string $url URL to a file asset (such as JS/CSS file)

@param bool|null|string $useVersion See versionUrls() method for description of this argument.

@return string URL updated with version strings where necessary

@since 3.0.227

@see Config::versionUrls()

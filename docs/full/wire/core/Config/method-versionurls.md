# Config::versionUrls()

Source: `wire/core/Config.php`

Given array of file asset URLs return them with cache-busting version strings

URLs that aready have query strings or URLs with scheme (i.e. https://) are ignored,
except for URLs that already have a core version query string, i.e. `?v=3.0.227`
may be converted to a different version string when appropriate.

URLs that do not resolve to a physical file on the file system, relative URLs, or
URLs that are outside of ProcessWire’s web root, are only eligible to receive a
common/shared version in the URL (like the core version).

To set a different default value for the `$useVersion` argument, you can populate
the `$config->useVersionUrls` setting in your /site/config.php with the default
value you want to substitute.

~~~~~
foreach($config->versionUrls($config->styles) as $url) {
  echo "<link rel='stylesheet' href='$url' />";
}
// there is also this shortcut for the above
foreach($config->styles->urls() as $url) {
  echo "<link rel='stylesheet' href='$url' />";
}
~~~~~


@param array|FilenameArray|WireArray|\ArrayObject $urls Array of URLs to file assets such as JS/CSS files.

@param bool|null|string $useVersion What to use for the version string (`null` is default):
 - `true` (bool): Get version from filemtime.
 - `false` (bool): Never get file version, just use $config->version.
 - `null` (null): Auto-detect: use file version in debug mode or dev branch only, $config->version otherwise.
 - `foobar` (string): Specify any string to be the version to use on all URLs needing it.
`- ?foo=bar` (string): Optionally specify your own query string variable=value.
 - The default value (null) can be overridden by the `$config->useVersionUrls` setting.

@return array Array of URLs updated with version strings where needed

@since 3.0.227

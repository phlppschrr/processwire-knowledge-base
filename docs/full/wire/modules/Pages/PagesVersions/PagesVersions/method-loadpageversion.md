# $pagesVersions->loadPageVersion(Page $page, $version, array $options = []): bool

Source: `wire/modules/Pages/PagesVersions/PagesVersions.module.php`

Load and populate version data to given page

This is similar to the `getPageVersion()` method except that it populates
the given `$page` rather than populating and returning a cloned copy of it.

## Usage

~~~~~
// basic usage
$bool = $pagesVersions->loadPageVersion($page, $version);

// usage with all arguments
$bool = $pagesVersions->loadPageVersion(Page $page, $version, array $options = []);
~~~~~

## Arguments

- `$page` `Page`
- `$version` `int|string|PageVersionInfo`
- `$options` (optional) `array` - `names` (array): Optionally load only these field/property names from version.

## Return value

- `bool` True if version data was available and populated, false if not

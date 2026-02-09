# $pagesVersions->getPageVersion(Page $page, $version, array $options = []): Page|NullPage

Source: `wire/modules/Pages/PagesVersions/PagesVersions.module.php`

Get requested page version in a copy of given page

## Example

~~~~~
$page = $pages->get(1234);
$pageV2 = $pagesVersions->getPageVersion($page, 2);
~~~~~

## Usage

~~~~~
// basic usage
$page = $pagesVersions->getPageVersion($page, $version);

// usage with all arguments
$page = $pagesVersions->getPageVersion(Page $page, $version, array $options = []);
~~~~~

## Arguments

- `$page` `Page` Page that version is for
- `$version` `int` Version number to get
- `$options` (optional) `array` - `names` (array): Optionally load only these field/property names from version.

## Return value

- `Page|NullPage` - Returned page is a clone/copy of the given page updated for version data. - Returns a `NullPage` if requested version is not found or not allowed.

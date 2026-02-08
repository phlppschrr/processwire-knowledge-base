# $pagesVersions->getPageVersions(Page $page, array $options = []): PageVersionInfo[]|Page[]

Source: `wire/modules/Pages/PagesVersions/PagesVersions.module.php`

Get all versions for given page

## Example

~~~~~
$page = $pages->get(1234);
$versions = $pagesVersions->getPageVersions($page);
foreach($versions as $p) {
  echo $p->get('_version')->version; // i.e. 2, 3, 4, etc.
}
~~~~~

## Usage

~~~~~
// basic usage
$pageVersionInfo = $pagesVersions->getPageVersions($page);

// usage with all arguments
$pageVersionInfo = $pagesVersions->getPageVersions(Page $page, array $options = []);
~~~~~

## Arguments

- `$page` `Page`
- `$options` (optional) `array` - `getInfo` (bool): Specify true to instead get PageVersionInfo objects (default=false) - `sort` (string): Sort by property, one of: 'created', '-created', 'version', '-version' (default='-created') - `version` (array): Limit to this version number, for internal use (default=0)

## Return value

- `PageVersionInfo[]|Page[]` - Returns Array of `Page` objects or array of `PageVersionInfo` objects if `getInfo` requested. - When returning pages, version info is in `$page->_version` value of each page, which is a `PageVersionInfo` object.

## Exceptions

- `WireException`

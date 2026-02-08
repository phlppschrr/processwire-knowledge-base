# $pagesVersions->addPageVersion(Page $page, array $options = []): int

Source: `wire/modules/Pages/PagesVersions/PagesVersions.module.php`

Add a new page version and return the added version number

## Example

~~~~~
$page = $pages->get(1234);
$version = $pagesVersions->addPageVersion($page);
echo "Added version $version for page $page";
~~~~~

## Usage

~~~~~
// basic usage
$int = $pagesVersions->addPageVersion($page);

// usage with all arguments
$int = $pagesVersions->addPageVersion(Page $page, array $options = []);
~~~~~

## Arguments

- `$page` `Page`
- `$options` (optional) `array` - `description` (string): Optional text description for version. - `names` (array): Names of fields/properties to include in the version or omit for all.

## Return value

- `int` Version number or 0 if no version created

## Exceptions

- `WireException|\PDOException`

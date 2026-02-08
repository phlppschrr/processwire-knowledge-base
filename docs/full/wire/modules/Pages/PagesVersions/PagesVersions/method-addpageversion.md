# $pagesVersions->addPageVersion(Page $page, array $options = []): int

Source: `wire/modules/Pages/PagesVersions/PagesVersions.module.php`

Add a new page version and return the added version number

~~~~~
$page = $pages->get(1234);
$version = $pagesVersions->addPageVersion($page);
echo "Added version $version for page $page";
~~~~~

## Arguments

- Page $page
- array $options - `description` (string): Optional text description for version. - `names` (array): Names of fields/properties to include in the version or omit for all.

## Return value

int Version number or 0 if no version created

## Throws

- WireException|\PDOException

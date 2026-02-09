# $pagesVersions->getUnsupportedFields(?Page $page = null): Field[]

Source: `wire/modules/Pages/PagesVersions/PagesVersions.module.php`

Get fields where versions are not supported

## Usage

~~~~~
// basic usage
$field = $pagesVersions->getUnsupportedFields();

// usage with all arguments
$field = $pagesVersions->getUnsupportedFields(?Page $page = null);
~~~~~

## Arguments

- `$page` (optional) `Page|null` Page to limit check to or omit for all fields

## Return value

- `Field[]` Returned array of Field objects is indexed by Field name

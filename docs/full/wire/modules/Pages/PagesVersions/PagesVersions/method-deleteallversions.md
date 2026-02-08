# $pagesVersions->deleteAllVersions($areYouSure = false): int

Source: `wire/modules/Pages/PagesVersions/PagesVersions.module.php`

Delete all versions across all pages

## Usage

~~~~~
// basic usage
$int = $pagesVersions->deleteAllVersions();

// usage with all arguments
$int = $pagesVersions->deleteAllVersions($areYouSure = false);
~~~~~

## Arguments

- `$areYouSure` (optional) `bool` Specify true to indicate you are sure you want to do this

## Return value

- `int` Quantity of versions deleted

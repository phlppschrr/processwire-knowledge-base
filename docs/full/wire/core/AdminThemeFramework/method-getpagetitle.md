# $adminThemeFramework->getPageTitle(Page $p): string

Source: `wire/core/AdminThemeFramework.php`

Get navigation title for the given page, return blank if page should not be shown

## Usage

~~~~~
// basic usage
$string = $adminThemeFramework->getPageTitle($p);

// usage with all arguments
$string = $adminThemeFramework->getPageTitle(Page $p);
~~~~~

## Arguments

- `$p` `Page`

## Return value

- `string`

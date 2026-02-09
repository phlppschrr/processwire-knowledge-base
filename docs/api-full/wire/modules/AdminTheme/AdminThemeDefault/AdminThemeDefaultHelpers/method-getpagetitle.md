# $adminThemeDefaultHelpers->getPageTitle(Page $c): string

Source: `wire/modules/AdminTheme/AdminThemeDefault/AdminThemeDefaultHelpers.php`

Get navigation title for the given page, return blank if page should not be shown

## Usage

~~~~~
// basic usage
$string = $adminThemeDefaultHelpers->getPageTitle($c);

// usage with all arguments
$string = $adminThemeDefaultHelpers->getPageTitle(Page $c);
~~~~~

## Arguments

- `$c` `Page`

## Return value

- `string`

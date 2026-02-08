# $adminThemeRenoHelpers->renderQuicklinks(Page $page, array $items, $title, $json = ''): string

Source: `wire/modules/AdminTheme/AdminThemeReno/AdminThemeRenoHelpers.php`

Render quicklinks for templates/fields. Designed to be called by renderSideNav()

## Usage

~~~~~
// basic usage
$string = $adminThemeRenoHelpers->renderQuicklinks($page, $items, $title);

// usage with all arguments
$string = $adminThemeRenoHelpers->renderQuicklinks(Page $page, array $items, $title, $json = '');
~~~~~

## Arguments

- `$page` `Page`
- `$items` `array`
- `$title` `string`
- `$json` (optional) `string`

## Return value

- `string`

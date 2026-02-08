# $adminThemeDefaultHelpers->renderAdminNotices($notices, array $options = array()): string

Source: `wire/modules/AdminTheme/AdminThemeDefault/AdminThemeDefaultHelpers.php`

Render runtime notices div#notices

## Usage

~~~~~
// basic usage
$string = $adminThemeDefaultHelpers->renderAdminNotices($notices);

// usage with all arguments
$string = $adminThemeDefaultHelpers->renderAdminNotices($notices, array $options = array());
~~~~~

## Arguments

- `$options` (optional) `array` See defaults in method
- `$notices` `Notices`

## Return value

- `string`

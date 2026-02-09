# $adminThemeDefaultHelpers->renderTopNavItemArray(Page $p, array $nav): string

Source: `wire/modules/AdminTheme/AdminThemeDefault/AdminThemeDefaultHelpers.php`

Renders static navigation from an array coming from getModuleInfo()['nav'] array (see wire/core/Process.php)

## Usage

~~~~~
// basic usage
$string = $adminThemeDefaultHelpers->renderTopNavItemArray($p, $nav);

// usage with all arguments
$string = $adminThemeDefaultHelpers->renderTopNavItemArray(Page $p, array $nav);
~~~~~

## Arguments

- `$p` `Page`
- `$nav` `array`

## Return value

- `string`

# $adminThemeFramework->moduleToNavArray($module, Page $p): array

Source: `wire/core/AdminThemeFramework.php`

Get navigation array from a Process module

## Usage

~~~~~
// basic usage
$array = $adminThemeFramework->moduleToNavArray($module, $p);

// usage with all arguments
$array = $adminThemeFramework->moduleToNavArray($module, Page $p);
~~~~~

## Arguments

- `$module` `array|Module|string` Module info array or Module object or string
- `$p` `Page` Page upon which the Process module is contained

## Return value

- `array`

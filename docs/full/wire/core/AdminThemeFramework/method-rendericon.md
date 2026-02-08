# $adminThemeFramework->renderIcon($icon, $fw = false): string

Source: `wire/core/AdminThemeFramework.php`

Render markup for a font-awesome icon

## Usage

~~~~~
// basic usage
$string = $adminThemeFramework->renderIcon($icon);

// usage with all arguments
$string = $adminThemeFramework->renderIcon($icon, $fw = false);
~~~~~

## Arguments

- `$icon` `string` Name of icon to render, excluding the “fa-” prefix
- `$fw` (optional) `bool` Specify true to make fixed width (default=false).

## Return value

- `string`

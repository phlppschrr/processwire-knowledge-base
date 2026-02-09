# $adminThemeFramework->renderNavIcon($icon): string

Source: `wire/core/AdminThemeFramework.php`

Render markup for a font-awesome icon that precedes a navigation label

This is the same as renderIcon() except that fixed-width is assumed and a "nav-nav-icon"
class is added to it.

## Usage

~~~~~
// basic usage
$string = $adminThemeFramework->renderNavIcon($icon);
~~~~~

## Arguments

- `$icon` `string` Name of icon to render, excluding the “fa-” prefix

## Return value

- `string`

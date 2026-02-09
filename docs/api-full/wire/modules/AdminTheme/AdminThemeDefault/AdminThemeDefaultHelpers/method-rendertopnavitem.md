# $adminThemeDefaultHelpers->renderTopNavItem(Page $p, $level = 0): string

Source: `wire/modules/AdminTheme/AdminThemeDefault/AdminThemeDefaultHelpers.php`

Render a single top navigation item for the given page

This function designed primarily to be called by the renderTopNavItems() function.

## Usage

~~~~~
// basic usage
$string = $adminThemeDefaultHelpers->renderTopNavItem($p);

// usage with all arguments
$string = $adminThemeDefaultHelpers->renderTopNavItem(Page $p, $level = 0);
~~~~~

## Arguments

- `$p` `Page`
- `$level` (optional) `int` Recursion level (default=0)

## Return value

- `string`

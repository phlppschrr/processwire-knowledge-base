# $adminThemeFramework->allowPageInNav(Page $p, $children = array(), $permission = null): bool

Source: `wire/core/AdminThemeFramework.php`

Allow the given Page to appear in admin theme navigation?

## Usage

~~~~~
// basic usage
$bool = $adminThemeFramework->allowPageInNav($p);

// usage with all arguments
$bool = $adminThemeFramework->allowPageInNav(Page $p, $children = array(), $permission = null);
~~~~~

## Arguments

- `$p` `Page` Page to test
- `$children` (optional) `PageArray|array` Children of page, if applicable (optional)
- `$permission` (optional) `string|null` Specify required permission (optional)

## Return value

- `bool`

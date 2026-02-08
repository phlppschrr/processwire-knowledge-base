# $users->setAdminThemeByRole($adminTheme, Role $role): int

Source: `wire/core/Users.php`

Set admin theme for all users having role

## Usage

~~~~~
// basic usage
$int = $users->setAdminThemeByRole($adminTheme, $role);

// usage with all arguments
$int = $users->setAdminThemeByRole($adminTheme, Role $role);
~~~~~

## Arguments

- `$adminTheme` `AdminTheme|string` Admin theme instance or class/module name
- `$role` `Role`

## Return value

- `int` Number of users set for admin theme

## Exceptions

- `WireException`

## Since

3.0.176

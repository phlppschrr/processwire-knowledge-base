# $modules->get($key): Module|_Module|null

Source: `wire/core/Modules.php`

Get the requested Module

- If the module is not installed, but is installable, it will be installed, instantiated, and initialized.
  If you don't want that behavior, call `$modules->isInstalled('ModuleName')` as a conditional first.
- You can also get/load a module by accessing it directly, like `$modules->ModuleName`.
- To get a module with additional options, use `$modules->getModule($name, $options)` instead.

~~~~~
// Get the MarkupAdminDataTable module
$table = $modules->get('MarkupAdminDataTable');

// You can also do this
$table = $modules->MarkupAdminDataTable;
~~~~~

## Arguments

- `$key` `string|int` Module name (also accepts database ID)

## Return value

Module|_Module|null Returns a Module or null if not found

## Throws

- WirePermissionException If module requires a particular permission the user does not have

## See also

- [Modules::getModule()](method-getmodule.md)
- [Modules::isInstalled()](method-isinstalled.md)

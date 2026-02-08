# $processController->hasPermission($permissionName, $throw = true): bool

Source: `wire/core/ProcessController.php`

Does the current user have permission to execute the given process name?

Note: an empty permission name is accessible only by the superuser

## Usage

~~~~~
// basic usage
$bool = $processController->hasPermission($permissionName);

// usage with all arguments
$bool = $processController->hasPermission($permissionName, $throw = true);
~~~~~

## Arguments

- `$permissionName` `string`
- `$throw` (optional) `bool` Whether to throw an Exception if the user does not have permission

## Return value

- `bool`

## Exceptions

- `ProcessControllerPermissionException`

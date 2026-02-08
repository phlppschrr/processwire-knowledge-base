# $processController->hasPermission($permissionName, $throw = true): bool

Source: `wire/core/ProcessController.php`

Does the current user have permission to execute the given process name?

Note: an empty permission name is accessible only by the superuser

## Arguments

- string $permissionName
- bool $throw Whether to throw an Exception if the user does not have permission

## Return value

bool

## Throws

- ProcessControllerPermissionException

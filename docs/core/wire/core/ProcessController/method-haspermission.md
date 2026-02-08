# ProcessController::hasPermission()

Source: `wire/core/ProcessController.php`

Does the current user have permission to execute the given process name?

Note: an empty permission name is accessible only by the superuser

@param string $permissionName

@param bool $throw Whether to throw an Exception if the user does not have permission

@return bool

@throws ProcessControllerPermissionException

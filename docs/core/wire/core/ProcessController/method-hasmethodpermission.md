# $processController->hasMethodPermission($method, $throw = true): bool

Source: `wire/core/ProcessController.php`

Does user have permission for the given $method name in the current Process?

## Usage

~~~~~
// basic usage
$bool = $processController->hasMethodPermission($method);

// usage with all arguments
$bool = $processController->hasMethodPermission($method, $throw = true);
~~~~~

## Arguments

- `$method` `string`
- `$throw` (optional) `bool` Throw exception if not permission?

## Return value

- `bool`

## Exceptions

- `ProcessControllerPermissionException`

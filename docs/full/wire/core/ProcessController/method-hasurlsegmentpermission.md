# $processController->hasUrlSegmentPermission($urlSegment, $throw = true): bool

Source: `wire/core/ProcessController.php`

Does user have permission for the given urlSegment in the current Process?

## Usage

~~~~~
// basic usage
$bool = $processController->hasUrlSegmentPermission($urlSegment);

// usage with all arguments
$bool = $processController->hasUrlSegmentPermission($urlSegment, $throw = true);
~~~~~

## Arguments

- `$urlSegment` `string`
- `$throw` (optional) `bool` Throw exception if not permission?

## Return value

- `bool`

## Exceptions

- `ProcessControllerPermissionException`

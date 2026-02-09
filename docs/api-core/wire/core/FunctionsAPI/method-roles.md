# $functionsAPI->roles($selector = ''): Roles|Role|PageArray|null|NullPage

Source: `wire/core/FunctionsAPI.php`

Get, find or save roles ($roles API variable as a function)

Accessing `roles()` is exactly the same as accessing `$roles`. Though there are a couple of optional
shortcuts available by providing an argument to this function.

## Usage

~~~~~
// basic usage
$roles = $functionsAPI->roles();

// usage with all arguments
$roles = $functionsAPI->roles($selector = '');
~~~~~

## Arguments

- `$selector` (optional) `string|int` - Specify name or ID of role to get (Role object) - Specify selector string matching roles to find (PageArray object)

## Return value

- `Roles|Role|PageArray|null|NullPage`

## See Also

- Roles

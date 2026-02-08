# $functionsAPI->permissions($selector = ''): Permissions|Permission|PageArray|null|NullPage

Source: `wire/core/FunctionsAPI.php`

Get, find or save permissions ($permissions API variable as a function)

Accessing `permissions()` is exactly the same as accessing `$permissions`. Though there are a couple of optional
shortcuts available by providing an argument to this function.

## Example

~~~~~
// Get a permission
$p = permissions()->get('page-edit'); // regular syntax
$p = permissions('page-edit'); // shortcut syntax

// Find permissions
$ps = permissions()->find('name^=page'); // regular syntax
$ps = permissions('name^=page'); // shortcut syntax
~~~~~

## Usage

~~~~~
// basic usage
$permissions = $functionsAPI->permissions();

// usage with all arguments
$permissions = $functionsAPI->permissions($selector = '');
~~~~~

## Arguments

- `$selector` (optional) `string|int` - Specify permission name or ID to retrieve that Permission (Permission) - Specify a selector string to return all permissions matching selector (PageArray)

## Return value

- `Permissions|Permission|PageArray|null|NullPage`

## See Also

- Permissions

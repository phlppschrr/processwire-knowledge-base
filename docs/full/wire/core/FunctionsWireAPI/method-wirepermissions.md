# $functionsWireAPI->wirePermissions($selector = ''): Permissions|Permission|PageArray|null|NullPage

Source: `wire/core/FunctionsWireAPI.php`

Access the $permissions API varaible as a function

See the pages() function for usage details.

## Usage

~~~~~
// basic usage
$permissions = $functionsWireAPI->wirePermissions();

// usage with all arguments
$permissions = $functionsWireAPI->wirePermissions($selector = '');
~~~~~

## Arguments

- `$selector` (optional) `string`

## Return value

- `Permissions|Permission|PageArray|null|NullPage`

# $wireHooks->hasPathHooks($requestPath = ''): bool

Source: `wire/core/WireHooks.php`

Return whether or not any path hooks are pending

## Usage

~~~~~
// basic usage
$bool = $wireHooks->hasPathHooks();

// usage with all arguments
$bool = $wireHooks->hasPathHooks($requestPath = '');
~~~~~

## Arguments

- `$requestPath` (optional) `string` Optionally provide request path to determine if any might match (3.0.174+)

## Return value

- `bool`

## Since

3.0.173

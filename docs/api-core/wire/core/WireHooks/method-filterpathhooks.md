# $wireHooks->filterPathHooks($requestPath, $has = false): array|bool

Source: `wire/core/WireHooks.php`

Return path hooks that have potential to match given request path

## Usage

~~~~~
// basic usage
$array = $wireHooks->filterPathHooks($requestPath);

// usage with all arguments
$array = $wireHooks->filterPathHooks($requestPath, $has = false);
~~~~~

## Arguments

- `$requestPath` `string`
- `$has` (optional) `bool` Specify true to change return value to boolean as to whether any can match (default=false)

## Return value

- `array|bool`

## Since

3.0.174

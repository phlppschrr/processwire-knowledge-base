# $wireHooks->removeHooks(Wire $object, $hookIDs): Wire

Source: `wire/core/WireHooks.php`

Given a hook ID or multiple hook IDs (in array or CSV string) remove the hooks

## Usage

~~~~~
// basic usage
$wire = $wireHooks->removeHooks($object, $hookIDs);

// usage with all arguments
$wire = $wireHooks->removeHooks(Wire $object, $hookIDs);
~~~~~

## Arguments

- `$object` `Wire`
- `$hookIDs` `array|string`

## Return value

- `Wire`

## Since

3.0.137

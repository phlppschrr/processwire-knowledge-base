# $wireHooks->addPathHook(Wire $object, $path, $toObject, $toMethod, $options = array()): string

Source: `wire/core/WireHooks.php`

Add a hook that handles a request path

## Usage

~~~~~
// basic usage
$string = $wireHooks->addPathHook($object, $path, $toObject, $toMethod);

// usage with all arguments
$string = $wireHooks->addPathHook(Wire $object, $path, $toObject, $toMethod, $options = array());
~~~~~

## Arguments

- `$object` `Wire`
- `$path` `string`
- `$toObject` `Wire|null|callable`
- `$toMethod` `string`
- `$options` (optional) `array`

## Return value

- `string`

## Exceptions

- `WireException`

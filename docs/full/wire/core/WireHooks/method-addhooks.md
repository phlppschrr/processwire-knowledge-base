# WireHooks::addHooks()

Source: `wire/core/WireHooks.php`

Add a hooks to multiple methods at once

This is the same as addHook() except that the $method argument is an array or CSV string of hook definitions.
See the addHook() method for more detailed info on arguments.

@param Wire $object

@param array|string $methods Array of one or more strings hook definitions, or CSV string of hook definitions

@param object|null|callable $toObject

@param string|array|null $toMethod

@param array $options

@return string CSV string of hook IDs that were added

@throws WireException

@since 3.0.137

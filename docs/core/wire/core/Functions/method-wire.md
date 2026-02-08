# Functions::wire()

Source: `wire/core/Functions.php`

Return an API variable, or return current ProcessWire instance if given no arguments

- Call `wire()` with no arguments returns the current ProcessWire instance.
- Call `wire('var')` to return the API variable represented by 'var', or null if not present.
- Call `wire('all')` or `wire('*')` to return an iterable object of all API variables.
- Call `wire($object)` to attach $object to the current instance ($object must be Wire-derived object).


@param string $name If omitted, returns current ProcessWire instance.

@return null|ProcessWire|Wire|Session|Page|Pages|Modules|User|Users|Roles|Permissions|Templates|Fields|Fieldtypes|Sanitizer|Config|Notices|WireDatabasePDO|WireHooks|WireDateTime|WireFileTools|WireMailTools|WireInput|string|mixed Requested API variable or null if it does not exist

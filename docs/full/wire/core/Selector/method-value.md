# Selector::value()

Source: `wire/core/Selector.php`

Get the value(s) of this Selector

Note that if calling this as a property (rather than a method) it can return either a string or an array.

@param bool|int $forceString Specify one of the following:
 - `true` (bool): to only return a string, where multiple-values will be split by pipe "|". (default)
 - `false` (bool): to return string if 1 value, or array of multiple values (same behavior as value property).
 - `1` (int): to return only the first value (string).

@return string|array|null

@since 3.0.42 Prior versions only supported the 'value' property.

@see Selector::values()

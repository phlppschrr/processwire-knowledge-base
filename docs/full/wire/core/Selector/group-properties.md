# Selector: properties

Source: `wire/core/Selector.php`

@property bool $not Is this a NOT selector? Indicates the selector returns the opposite if what it would otherwise.

@property string|null $group Group name for this selector (if field was prepended with a "group_name@").

@property string $quote Type of quotes value was in, or blank if it was not quoted. One of: '"[{(

@property-read string $str String value of selector, i.e. “a=b”.

@property null|bool $forceMatch When boolean, forces match (true) or force non-match (false). (default=null)

@property array $altOperators Alternate operators to use when primary fails match, supported only by compareTypeFind. Since 3.0.161 (default=[])

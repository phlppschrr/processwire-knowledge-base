# Selector: other

Source: `wire/core/Selector.php`

@property array $fields Fields that were present in selector (same as $field, but always an array).

@property string|array $field Field or fields present in the selector (string if single, or array of strings if multiple). Preferable to use $fields property instead.

@property-read string $operator Operator used by the selector.

@property array $values Values that were present in selector (same as $value, but always array).

@property string|array $value Value or values present in the selector (string if single, or array of strings if multiple). Preferable to use $values property instead.

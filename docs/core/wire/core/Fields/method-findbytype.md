# $fields->findByType($type, array $options = array()): array|Field[]

Source: `wire/core/Fields.php`

Find fields by type

## Arguments

- `$type` `string|Fieldtype` Fieldtype class name or object
- `$options` (optional) `array` - `inherit` (bool): Also find types that inherit from given type? (default=true) - `valueType` (string): Value type to return, one of 'field', 'id', or 'name' (default='field') - `indexType` (string): Index type to use, one of 'name', 'id', or '' blank for non-associative array (default='name')

## Return value

array|Field[]

## Since

3.0.194

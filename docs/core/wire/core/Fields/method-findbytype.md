# $fields->findByType($type, array $options = array()): array|Field[]

Source: `wire/core/Fields.php`

Find fields by type

## Arguments

- string|Fieldtype $type Fieldtype class name or object
- array $options - `inherit` (bool): Also find types that inherit from given type? (default=true) - `valueType` (string): Value type to return, one of 'field', 'id', or 'name' (default='field') - `indexType` (string): Index type to use, one of 'name', 'id', or '' blank for non-associative array (default='name')

## Return value

array|Field[]

## Meta

- @since 3.0.194

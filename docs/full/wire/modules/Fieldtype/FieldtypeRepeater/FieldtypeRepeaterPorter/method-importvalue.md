# $fieldtypeRepeaterPorter->importValue(Page $page, Field $field, $value, array $options = array()): bool|PageArray

Source: `wire/modules/Fieldtype/FieldtypeRepeater/FieldtypeRepeaterPorter.php`

Import repeater value previously exported by exportValue()

## Usage

~~~~~
// basic usage
$bool = $fieldtypeRepeaterPorter->importValue($page, $field, $value);

// usage with all arguments
$bool = $fieldtypeRepeaterPorter->importValue(Page $page, Field $field, $value, array $options = array());
~~~~~

## Arguments

- `$page` `Page`
- `$field` `Field`
- `$value` `array`
- `$options` (optional) `array`

## Return value

- `bool|PageArray`

## Exceptions

- `WireException`

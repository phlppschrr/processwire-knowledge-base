# $fieldtypeRepeaterPorter->exportValue(Page $page, Field $field, $value, array $options = array()): array

Source: `wire/modules/Fieldtype/FieldtypeRepeater/FieldtypeRepeaterPorter.php`

Export repeater value

## Usage

~~~~~
// basic usage
$array = $fieldtypeRepeaterPorter->exportValue($page, $field, $value);

// usage with all arguments
$array = $fieldtypeRepeaterPorter->exportValue(Page $page, Field $field, $value, array $options = array());
~~~~~

## Arguments

- `$page` `Page`
- `$field` `Field`
- `$value` `RepeaterPageArray`
- `$options` (optional) `array` - `minimal` (bool): Export a minimal array of just fields and values indexed by repeater page name (default=false)

## Return value

- `array`

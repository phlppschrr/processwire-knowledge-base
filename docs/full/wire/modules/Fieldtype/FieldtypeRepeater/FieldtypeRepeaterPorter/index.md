# FieldtypeRepeaterPorter

Source: `wire/modules/Fieldtype/FieldtypeRepeater/FieldtypeRepeaterPorter.php`

Inherits: `Wire`

Export and Import tools for FieldtypeRepeater

Methods:
- [`exportConfigData(Field $field, array $data): array`](method-exportconfigdata.md) Export configuration values for external consumption
- [`importConfigData(Field $field, array $data, array &$errors): array`](method-importconfigdata.md) Convert an array of exported data to a format that will be understood internally
- [`exportValue(Page $page, Field $field, RepeaterPageArray $value, array $options = array()): array`](method-exportvalue.md) Export repeater value
- [`importValue(Page $page, Field $field, array $value, array $options = array()): bool|PageArray`](method-importvalue.md) Import repeater value previously exported by exportValue()

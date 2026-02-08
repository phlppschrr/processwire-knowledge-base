# Fieldtype::___exportConfigData()

Source: `wire/core/Fieldtype.php`

Export configuration values for external consumption

Use this method to externalize any config values when necessary.
For example, internal IDs should be converted to GUIDs where possible.
Most Fieldtype modules can use the default implementation already provided here.


@param Field $field

@param array $data

@return array

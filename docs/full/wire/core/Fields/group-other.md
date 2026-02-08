# Fields: other

Source: `wire/core/Fields.php`

@method Field|null get($key) Get a field by name or id

@method bool changeFieldtype(Field $field1, $keepSettings = false)

@method bool saveFieldgroupContext(Field $field, Fieldgroup $fieldgroup, $namespace = '')

@method bool deleteFieldDataByTemplate(Field $field, Template $template)

@method void changedType(Saveable $item, Fieldtype $fromType, Fieldtype $toType)

@method void changeTypeReady(Saveable $item, Fieldtype $fromType, Fieldtype $toType)

@method bool|Field clone(Field $item, $name = '') Clone a field and return it or return false on fail.

@method array getTags($getFieldNames = false) Get tags for all fields (3.0.179+)

@method bool applySetupName(Field $field, $setupName = '')

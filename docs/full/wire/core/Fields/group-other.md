# Fields: other

Source: `wire/core/Fields.php`

- [`get($key): Field|null`](method-get.md) Get a field by name or id
- [`changeFieldtype(Field $field1, $keepSettings = false): bool`](method-___changefieldtype.md)
- [`saveFieldgroupContext(Field $field, Fieldgroup $fieldgroup, $namespace = ''): bool`](method-___savefieldgroupcontext.md)
- [`deleteFieldDataByTemplate(Field $field, Template $template): bool`](method-___deletefielddatabytemplate.md)
- [`changedType(Saveable $item, Fieldtype $fromType, Fieldtype $toType): void`](method-___changedtype.md)
- [`changeTypeReady(Saveable $item, Fieldtype $fromType, Fieldtype $toType): void`](method-___changetypeready.md)
- [`clone(Field $item, $name = ''): bool|Field`](method-___clone.md) Clone a field and return it or return false on fail.
- [`getTags($getFieldNames = false): array`](method-___gettags.md) Get tags for all fields (3.0.179+)
- [`applySetupName(Field $field, $setupName = ''): bool`](method-___applysetupname.md)

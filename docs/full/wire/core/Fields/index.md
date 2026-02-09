# Fields

Source: `wire/core/Fields.php`

Inherits: `WireSaveableItems`


Groups:
Group: [other](group-other.md)

ProcessWire Fields

Manages collection of ALL Field instances, not specific to any particular Fieldgroup


Manages all custom fields in ProcessWire, independently of any Fieldgroup.
$fields
Each field returned is an object of type `Field`. The $fields API variable is iterable:
~~~~~
foreach($fields as $field) {
  echo "<p>Name: $field->name, Type: $field->type, Label: $field->label</p>";
}
~~~~~

Methods:
- [`__construct()`](method-__construct.md)
- [`loadRowsReady(array &$rows)`](method-loadrowsready.md)
- [`makeItem(array $a = array()): Saveable|Wire`](method-makeitem.md)
- [`initItem(array &$row, ?WireArray $items = null): Saveable|WireData|Wire`](method-inititem.md)
- [`getWireArray(): WireArray`](method-getwirearray.md)
- [`save(Saveable $item): bool`](method-___save.md) (hookable)
- [`checkFieldTable(Field $field)`](method-checkfieldtable.md)
- [`delete(Saveable $item): bool`](method-___delete.md) (hookable)
- [`clone(Saveable $item, string $name = ''): Field`](method-___clone.md) (hookable)
- [`saveFieldgroupContext(Field $field, Fieldgroup $fieldgroup, string $namespace = ''): bool`](method-___savefieldgroupcontext.md) (hookable)
- [`changeFieldtype(Field $field1, bool $keepSettings = false): bool`](method-___changefieldtype.md) (hookable)
- [`deleteFieldDataByTemplate(Field $field, Template $template): bool`](method-___deletefielddatabytemplate.md) (hookable)
- [`getNumPages(Field $field, array $options = array()): int|array`](method-getnumpages.md)
- [`getNumRows(Field $field, array $options = array()): int|array`](method-getnumrows.md)
- [`isNative(string $name): bool`](method-isnative.md)
- [`getTags(bool|string $getFieldNames = false): array`](method-___gettags.md) (hookable)
- [`findByTag(string $tag, bool $getFieldNames = false): array`](method-findbytag.md)
- [`findByType(string|Fieldtype $type, array $options = array()): array|Field[]`](method-findbytype.md)
- [`getAllNames(string $indexType = ''): array`](method-getallnames.md)
- [`changedType(Saveable $item, Fieldtype $fromType, Fieldtype $toType)`](method-___changedtype.md) (hookable)
- [`changeTypeReady(Saveable $item, Fieldtype $fromType, Fieldtype $toType)`](method-___changetypeready.md) (hookable)
- [`applySetupName(Field $field, string $setupName = ''): bool`](method-___applysetupname.md) (hookable)

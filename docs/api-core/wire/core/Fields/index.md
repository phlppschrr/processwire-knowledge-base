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
- [`__construct()`](method-__construct.md) Construct
- [`loadRowsReady(array &$rows)`](method-loadrowsready.md) Called after rows loaded from DB but before populated to this instance
- [`makeItem(array $a = array()): Saveable|Wire`](method-makeitem.md) Make an item and populate with given data
- [`initItem(array &$row, ?WireArray $items = null): Saveable|WireData|Wire`](method-inititem.md) Create a new Saveable item from a raw array ($row) and add it to $items
- [`getWireArray(): WireArray`](method-getwirearray.md) Get WireArray container that items are stored in
- [`save(Saveable $item): bool`](method-___save.md) (hookable) Save a Field to the database
- [`checkFieldTable(Field $field)`](method-checkfieldtable.md) Check that the given Field's table exists and create it if it doesn't
- [`delete(Saveable $item): bool`](method-___delete.md) (hookable) Delete a Field from the database
- [`clone(Saveable $item, string $name = ''): Field`](method-___clone.md) (hookable) Create and return a cloned copy of the given Field
- [`saveFieldgroupContext(Field $field, Fieldgroup $fieldgroup, string $namespace = ''): bool`](method-___savefieldgroupcontext.md) (hookable) Save the context of the given field for the given fieldgroup
- [`changeFieldtype(Field $field1, bool $keepSettings = false): bool`](method-___changefieldtype.md) (hookable) Change a field's type
- [`deleteFieldDataByTemplate(Field $field, Template $template): bool`](method-___deletefielddatabytemplate.md) (hookable) Physically delete all field data (from the database) used by pages of a given template
- [`getNumPages(Field $field, array $options = array()): int|array`](method-getnumpages.md) Return a count of pages containing populated values for the given field
- [`getNumRows(Field $field, array $options = array()): int|array`](method-getnumrows.md) Return a count of database rows populated the given field
- [`isNative(string $name): bool`](method-isnative.md) Is the given field name native/permanent to the database?
- [`getTags(bool|string $getFieldNames = false): array`](method-___gettags.md) (hookable) Get list of all tags used by fields
- [`findByTag(string $tag, bool $getFieldNames = false): array`](method-findbytag.md) Return all fields that have the given $tag
- [`findByType(string|Fieldtype $type, array $options = array()): array|Field[]`](method-findbytype.md) Find fields by type
- [`getAllNames(string $indexType = ''): array`](method-getallnames.md) Get all field names
- [`changedType(Saveable $item, Fieldtype $fromType, Fieldtype $toType)`](method-___changedtype.md) (hookable) Hook called when a field has changed type
- [`changeTypeReady(Saveable $item, Fieldtype $fromType, Fieldtype $toType)`](method-___changetypeready.md) (hookable) Hook called right before a field is about to change type
- [`applySetupName(Field $field, string $setupName = ''): bool`](method-___applysetupname.md) (hookable) Setup a new field using predefined setup name(s) from the Field’s fieldtype

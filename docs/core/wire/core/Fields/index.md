# Fields

Source: `wire/core/Fields.php`

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

Groups:
Group: [other](group-other.md)

Methods:
Method: [__construct()](method-__construct.md)
Method: [loadRowsReady()](method-loadrowsready.md)
Method: [makeItem()](method-makeitem.md)
Method: [initItem()](method-inititem.md)
Method: [getWireArray()](method-getwirearray.md)
Method: [save()](method-___save.md) (hookable)
Method: [checkFieldTable()](method-checkfieldtable.md)
Method: [delete()](method-___delete.md) (hookable)
Method: [clone()](method-___clone.md) (hookable)
Method: [saveFieldgroupContext()](method-___savefieldgroupcontext.md) (hookable)
Method: [changeFieldtype()](method-___changefieldtype.md) (hookable)
Method: [deleteFieldDataByTemplate()](method-___deletefielddatabytemplate.md) (hookable)
Method: [getNumPages()](method-getnumpages.md)
Method: [getNumRows()](method-getnumrows.md)
Method: [isNative()](method-isnative.md)
Method: [getTags()](method-___gettags.md) (hookable)
Method: [findByTag()](method-findbytag.md)
Method: [findByType()](method-findbytype.md)
Method: [getAllNames()](method-getallnames.md)
Method: [changedType()](method-___changedtype.md) (hookable)
Method: [changeTypeReady()](method-___changetypeready.md) (hookable)
Method: [applySetupName()](method-___applysetupname.md) (hookable)

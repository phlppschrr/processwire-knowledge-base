# Fields

Source: `wire/core/Fields.php`

ProcessWire Fields

Manages collection of ALL Field instances, not specific to any particular Fieldgroup

ProcessWire 3.x, Copyright 2024 by Ryan Cramer
https://processwire.com

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
Method: [___save()](method-___save.md)
Method: [checkFieldTable()](method-checkfieldtable.md)
Method: [___delete()](method-___delete.md)
Method: [___clone()](method-___clone.md)
Method: [___saveFieldgroupContext()](method-___savefieldgroupcontext.md)
Method: [___changeFieldtype()](method-___changefieldtype.md)
Method: [___deleteFieldDataByTemplate()](method-___deletefielddatabytemplate.md)
Method: [getNumPages()](method-getnumpages.md)
Method: [getNumRows()](method-getnumrows.md)
Method: [isNative()](method-isnative.md)
Method: [___getTags()](method-___gettags.md)
Method: [findByTag()](method-findbytag.md)
Method: [findByType()](method-findbytype.md)
Method: [getAllNames()](method-getallnames.md)
Method: [___changedType()](method-___changedtype.md)
Method: [___changeTypeReady()](method-___changetypeready.md)
Method: [___applySetupName()](method-___applysetupname.md)

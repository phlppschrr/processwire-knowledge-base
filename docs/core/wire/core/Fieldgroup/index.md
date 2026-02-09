# Fieldgroup

Source: `wire/core/Fieldgroup.php`

Inherits: `WireArray`
Implements: `Saveable`, `Exportable`, `HasLookupItems`


Groups:
Group: [other](group-other.md)
Group: [retrieval](group-retrieval.md)

ProcessWire Fieldgroup

A group of fields that is ultimately attached to a Template.

Fieldgroup is a type of WireArray that holds a group of Field objects for template(s).
For full details on all methods available in a Fieldgroup, be sure to also see the `WireArray` class.

The existance of Fieldgroups is hidden at the ProcessWire web admin level
as it appears that fields are attached directly to Templates. However, they
are separated in the API in case want want to have fieldgroups used by
multiple templates in the future (like ProcessWire 1.x).

Methods:
Method: [add()](method-add.md)
Method: [remove()](method-remove.md)
Method: [softRemove()](method-softremove.md)
Method: [getField()](method-getfield.md)
Method: [hasFieldContext()](method-hasfieldcontext.md)
Method: [getFieldContext()](method-getfieldcontext.md)
Method: [hasField()](method-hasfield.md)
Method: [get()](method-get.md)
Method: [set()](method-set.md)
Method: [save()](method-save.md)
Method: [__toString()](method-__tostring.md)
Method: [getPageInputfields()](method-getpageinputfields.md)
Method: [getTemplates()](method-gettemplates.md)
Method: [getNumTemplates()](method-getnumtemplates.md)
Method: [saveContext()](method-savecontext.md)

Constants:
Const: [contextNamespacePrefix](const-contextnamespaceprefix.md)

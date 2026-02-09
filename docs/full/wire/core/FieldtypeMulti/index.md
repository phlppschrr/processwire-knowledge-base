# FieldtypeMulti

Source: `wire/core/FieldtypeMulti.php`

Inherits: `Fieldtype`


Groups:
Group: [other](group-other.md)

ProcessWire FieldtypeMulti

Interface and some functionality for Fieldtypes that can contain multiple values.




To support automatic “order by” sorting: The `$useOrderByCols` property of this Fieldtype must be set to boolean true,
indicating that the Fieldtype supports sorting. The actual columns to order by are an array of 'col' or '-col' specified
with the Field object in an $orderByCols property (array).

To support pagination: Both the `$useOrderByCols` and the `$usePagination` properties of this Fieldtype must be set to
boolean true, indicating the Fieldtype supports pagination (and sorting). When enabled, the wakeupValue() method will receive
pagination information in the value it is given. All other aspects of pagination must be handled by the individual Fieldtype.

Methods:
Method: [getDatabaseSchema()](method-getdatabaseschema.md)
Method: [getSelectorInfo()](method-___getselectorinfo.md) (hookable)
Method: [getCompatibleFieldtypes()](method-___getcompatiblefieldtypes.md) (hookable)
Method: [getBlankValue()](method-getblankvalue.md)
Method: [sanitizeValue()](method-sanitizevalue.md)
Method: [wakeupValue()](method-___wakeupvalue.md) (hookable)
Method: [sleepValue()](method-___sleepvalue.md) (hookable)
Method: [savePageField()](method-___savepagefield.md) (hookable)
Method: [loadPageField()](method-___loadpagefield.md) (hookable)
Method: [getLoadQuery()](method-getloadquery.md)
Method: [getLoadQueryWhere()](method-getloadquerywhere.md)
Method: [setupPageFieldRows()](method-setuppagefieldrows.md)
Method: [lockForWriting()](method-lockforwriting.md)
Method: [unlockForWriting()](method-unlockforwriting.md)
Method: [getMaxColumnValue()](method-getmaxcolumnvalue.md)
Method: [getLoadQueryAutojoin()](method-getloadqueryautojoin.md)
Method: [getMatchQuery()](method-getmatchquery.md)
Method: [getConfigInputfields()](method-___getconfiginputfields.md) (hookable)

Constants:
Const: [multiValueSeparator](const-multivalueseparator.md)

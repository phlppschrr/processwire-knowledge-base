# FieldtypeMulti

Source: `wire/core/FieldtypeMulti.php`

ProcessWire FieldtypeMulti

Interface and some functionality for Fieldtypes that can contain multiple values.

ProcessWire 3.x, Copyright 2022 by Ryan Cramer
https://processwire.com



To support automatic “order by” sorting: The `$useOrderByCols` property of this Fieldtype must be set to boolean true,
indicating that the Fieldtype supports sorting. The actual columns to order by are an array of 'col' or '-col' specified
with the Field object in an $orderByCols property (array).

To support pagination: Both the `$useOrderByCols` and the `$usePagination` properties of this Fieldtype must be set to
boolean true, indicating the Fieldtype supports pagination (and sorting). When enabled, the wakeupValue() method will receive
pagination information in the value it is given. All other aspects of pagination must be handled by the individual Fieldtype.

Groups:
Group: [other](group-other.md)

Methods:
Method: [getDatabaseSchema()](method-getdatabaseschema.md)
Method: [___getSelectorInfo()](method-___getselectorinfo.md)
Method: [___getCompatibleFieldtypes()](method-___getcompatiblefieldtypes.md)
Method: [getBlankValue()](method-getblankvalue.md)
Method: [sanitizeValue()](method-sanitizevalue.md)
Method: [___wakeupValue()](method-___wakeupvalue.md)
Method: [___sleepValue()](method-___sleepvalue.md)
Method: [___savePageField()](method-___savepagefield.md)
Method: [___loadPageField()](method-___loadpagefield.md)
Method: [getLoadQuery()](method-getloadquery.md)
Method: [getLoadQueryWhere()](method-getloadquerywhere.md)
Method: [setupPageFieldRows()](method-setuppagefieldrows.md)
Method: [lockForWriting()](method-lockforwriting.md)
Method: [unlockForWriting()](method-unlockforwriting.md)
Method: [getMaxColumnValue()](method-getmaxcolumnvalue.md)
Method: [getLoadQueryAutojoin()](method-getloadqueryautojoin.md)
Method: [getMatchQuery()](method-getmatchquery.md)
Method: [___getConfigInputfields()](method-___getconfiginputfields.md)

Constants:
Const: [multiValueSeparator](const-multivalueseparator.md)

# MarkupFieldtype

Source: `wire/core/MarkupFieldtype.php`

Inherits: `WireData`
Implements: `Module`

Class MarkupFieldtype

Provides pre-packaged markup rendering for Fieldtypes
and potentially serves as a module type. This base class
just provides generic rendering for various differnet types,
accommodating just about any Fieldtype. But it is built to be
extended for more specific needs in various Fieldtypes.

USAGE:

$m = new MarkupFieldtype($page, $field, $value);
echo $m->render();

// Alternate usage:
$m = new MarkupFieldtype();
$m->setPage($page);
$m->setField($field);
$m->setValue($value);
echo $m->render();

// Render just a specific property:
echo $m->render('property');

Methods:
Method: [__construct()](method-__construct.md)
Method: [render()](method-render.md)
Method: [renderValue()](method-rendervalue.md)
Method: [renderProperty()](method-renderproperty.md)
Method: [valueToString()](method-valuetostring.md)
Method: [arrayToString()](method-arraytostring.md)
Method: [objectToString()](method-objecttostring.md)
Method: [renderInputfieldValue()](method-renderinputfieldvalue.md)
Method: [isLinkablePageProperty()](method-islinkablepageproperty.md)
Method: [__toString()](method-__tostring.md)
Method: [setValue()](method-setvalue.md)
Method: [getValue()](method-getvalue.md)

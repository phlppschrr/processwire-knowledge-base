# MarkupFieldtype

Source: `wire/core/MarkupFieldtype.php`

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

## __construct()

Construct the MarkupFieldtype

If you construct without providing page and field, please populate them
separately with the setPage and setField methods before calling render().

@param Page|null $page

@param Field|null $field

@param mixed $value

## render()

Render markup for the field or for the property from field

@param string $property Optional property (for object or array field values)

@return string

## renderValue()

Render the entire $page->get($field->name) value.

Classes descending from MarkupFieldtype this would implement their own method.

@param mixed $value The unformatted value to render.

@return string

## renderProperty()

Render the just a property from the $page->get($field->name) value.

Applicable only if the value of the field is an array or object.

Classes descending from MarkupFieldtype would implement their own method.

@param string $property The property name being rendered.

@param mixed $value The value of the property.

@return string

## valueToString()

Convert any value to a string

@param mixed $value

@param bool $encode

@return string

## arrayToString()

Render an unknown array or WireArray to a string

@param array|WireArray $value

@param bool $encode

@return string

## objectToString()

Render an object to a string

@param Wire|object $value

@return string

## renderInputfieldValue()

Render a value using an Inputfield's renderValue() method

@param $value

@return string

## isLinkablePageProperty()

Is the given page property/field name one that should be linked to the source page in output?

@param Page $page

@param $property

@return bool

## __toString()

The string value of a MarkupFieldtype is always the fully rendered field

@return string

## setValue()

Set the value

It is not necessary to call this as the value will be determined automatically from $page and $field.
If you set this, it should be a formatted value.

@param $value

## getValue()

Get the value

@return mixed

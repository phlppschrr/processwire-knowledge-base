# MarkupFieldtype::renderProperty()

Source: `wire/core/MarkupFieldtype.php`

Render the just a property from the $page->get($field->name) value.

Applicable only if the value of the field is an array or object.

Classes descending from MarkupFieldtype would implement their own method.

@param string $property The property name being rendered.

@param mixed $value The value of the property.

@return string

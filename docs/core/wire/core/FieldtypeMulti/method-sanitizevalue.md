# FieldtypeMulti::sanitizeValue()

Source: `wire/core/FieldtypeMulti.php`

Per the Fieldtype interface, sanitize the combined value for use in a Page

In this case, make sure that it's a WireArray (able to hold multiple values)

@param Page $page

@param Field $field

@param mixed $value

@return WireArray

# Fieldtype::___wakeupValue()

Source: `wire/core/Fieldtype.php`

Given a raw value (value as stored in database), return the value as it would appear in a Page object.

In many cases, no change to the value may be necessary, but if a Page expects this value as an object (for instance)
then this would be the method that converts that value to an object and returns it.

This method is called by the Page class, which takes the value provided by `Fieldtype::loadPageField()` and sends
it to this method before making it a part of the Page.


@param Page $page

@param Field $field

@param string|int|array $value

@return string|int|array|object $value

@see Fieldtype::sleepValue()

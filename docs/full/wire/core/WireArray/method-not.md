# WireArray::not()

Source: `wire/core/WireArray.php`

Filter this WireArray to only include items that DO NOT match the selector (destructive)

~~~~~
// returns all pages that don't have a 'nonav' variable set to a positive value.
$pages->not("nonav");
~~~~~


@param string|array|Selectors $selector

@return $this reference to current instance.

@see filterData

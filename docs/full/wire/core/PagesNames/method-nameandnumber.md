# PagesNames::nameAndNumber()

Source: `wire/core/PagesNames.php`

If given name has a numbered suffix, return array with name (excluding suffix) and the numbered suffix

Returns array like `[ 'name', 123 ]` where `name` is name without the suffix, and `123` is the numbered suffix.
If the name did not have a numbered suffix, then the 123 will be 0 and `name` will be the given `$name`.


@param string $name

@param string $delimiter Character(s) that separate name and numbered suffix

@return array

# Fieldtype::getFieldClass()

Source: `wire/core/Fieldtype.php`

Get class name to use Field objects of this type (must be class that extends Field class)

Return blank if default class (Field) should be used.

@param array $a Field data from DB (if needed)

@return string Return class name or blank to use default Field class

@since 3.0.146

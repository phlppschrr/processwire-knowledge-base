# SelectableOptionArray::addByProperty()

Source: `wire/modules/Fieldtype/FieldtypeOptions/SelectableOptionArray.php`

Add option by property (id, name, title)

@param string $property One of id, name or title

@param string|int $value Value to match for above property

@return SelectableOption|false Returns option added or false if not found

@throws WireException

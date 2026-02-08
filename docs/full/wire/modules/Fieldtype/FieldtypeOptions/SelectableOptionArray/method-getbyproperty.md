# SelectableOptionArray::getByProperty()

Source: `wire/modules/Fieldtype/FieldtypeOptions/SelectableOptionArray.php`

Get SelectableOption by $property matching $value, or boolean false if not found

@param string $property May be "title", "value" or "id"

@param string|int $value

@param bool|null $noValue Value to return if option not present (default=false)

@return bool|null|SelectableOption

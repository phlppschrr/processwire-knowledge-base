# Fieldtype::___getConfigArray()

Source: `wire/core/Fieldtype.php`

Same as getConfigInputfields but with definition as an array instead

If both getConfigInputfields and getConfigInputfieldsArray are implemented then
definitions from both will be used. It's probably simplest just to implement one
or the other.


@param Field $field

@return array

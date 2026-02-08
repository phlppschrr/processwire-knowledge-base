# CommentList::options()

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentList.php`

Get or set options

@param string|null|array $key Use one of the following:
 - Omit to get array of all options
 - Specify option name to get (and omit $value argument)
 - Specify option name to set and provide a non-null $value argument
 - Specify array of one or more [ 'option' => 'value' ] to set and omit $value argument

@param string|int|bool|null $value When setting an individual option, value should be specified here, otherwise omit

@return array|string|int|bool|null When getting singe option, value is returned, otherwise array of all options is returned.

@since 3.0.138

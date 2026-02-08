# $commentList->options($key = null, $value = null): array|string|int|bool|null

Source: `wire/modules/Fieldtype/FieldtypeComments/CommentList.php`

Get or set options

## Arguments

- string|null|array $key Use one of the following: - Omit to get array of all options - Specify option name to get (and omit $value argument) - Specify option name to set and provide a non-null $value argument - Specify array of one or more [ 'option' => 'value' ] to set and omit $value argument
- string|int|bool|null $value When setting an individual option, value should be specified here, otherwise omit

## Return value

array|string|int|bool|null When getting singe option, value is returned, otherwise array of all options is returned.

## Meta

- @since 3.0.138

# $pagesRawFinder->findCustomFieldtypeOptions(Field $field, $cols, $getArray, $getAllCols)

Source: `wire/core/PagesRaw.php`

Find custom Options fieldtype columns

Options field stores its values/titles in separate table.

To use, specify one of the following in the fields to get (where field_name is an options field name):

- `field_name` to just include the IDs of the selected options for each page.
- `field_name.*` to include all available properties for selected options for each page.
- `field_name.title` to include the selected option titles.
- `field_name.value` to include the selected option values.

## Arguments

- Field $field
- array $cols
- bool $getArray
- bool $getAllCols

## Meta

- @since 3.0.193

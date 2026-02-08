# Fieldtype::___formatValue()

Source: `wire/core/Fieldtype.php`

Format the given value for output and return a string of the formatted value

Page instances call upon this method to do any necessary formatting of a value in preparation for output,
but only if output formatting `$page->of()` is enabled. The most common use of this method is for text-only fields that
need to have some text formatting applied to them, like Markdown, SmartyPants, Textile, etc. As a result,
Fieldtype modules don't need to implement this unless it's applicable.


@param Page $page Page that the value lives on

@param Field $field Field that represents the value

@param string|int|object $value The value to format

@return mixed

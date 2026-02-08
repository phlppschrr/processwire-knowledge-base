# Field::getContext()

Source: `wire/core/Field.php`

Get this field in context of a Page/Template


@param Page|Template|Fieldgroup|string $for Specify Page, Template, or template name string

@param string $namespace Optional namespace (internal use)

@param bool $has Return boolean rather than Field to check if context exists? (default=false)

@return Field|bool

@since 3.0.162

@see Fieldgroup::getFieldContext(), Field::hasContext()

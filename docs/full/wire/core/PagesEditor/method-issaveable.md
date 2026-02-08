# PagesEditor::isSaveable()

Source: `wire/core/PagesEditor.php`

Is the given page in a state where it can be saved from the API?


@param Page $page

@param string $reason Text containing the reason why it can't be saved (assuming it's not saveable)

@param string|Field $fieldName Optional fieldname to limit check to.

@param array $options Options array given to the original save method (optional)

@return bool True if saveable, False if not

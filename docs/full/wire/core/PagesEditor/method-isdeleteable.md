# PagesEditor::isDeleteable()

Source: `wire/core/PagesEditor.php`

Is the given page deleteable from the API?

Note: this does not account for user permission checking.
It only checks if the page is in a state to be deleteable via the API.


@param Page $page

@param bool $throw Throw WireException with additional details?

@return bool True if deleteable, False if not

@throws WireException If requested to do so via $throw argument

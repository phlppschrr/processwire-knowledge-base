# $pagesEditor->isSaveable(Page $page, &$reason, $fieldName = '', array $options = array()): bool

Source: `wire/core/PagesEditor.php`

Is the given page in a state where it can be saved from the API?

## Arguments

- Page $page
- string $reason Text containing the reason why it can't be saved (assuming it's not saveable)
- string|Field $fieldName Optional fieldname to limit check to.
- array $options Options array given to the original save method (optional)

## Return value

bool True if saveable, False if not

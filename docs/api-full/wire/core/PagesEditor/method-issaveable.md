# $pagesEditor->isSaveable(Page $page, &$reason, $fieldName = '', array $options = array()): bool

Source: `wire/core/PagesEditor.php`

Is the given page in a state where it can be saved from the API?

## Usage

~~~~~
// basic usage
$bool = $pagesEditor->isSaveable($page, $reason);

// usage with all arguments
$bool = $pagesEditor->isSaveable(Page $page, &$reason, $fieldName = '', array $options = array());
~~~~~

## Arguments

- `$page` `Page`
- `$reason` `string` Text containing the reason why it can't be saved (assuming it's not saveable)
- `$fieldName` (optional) `string|Field` Optional fieldname to limit check to.
- `$options` (optional) `array` Options array given to the original save method (optional)

## Return value

- `bool` True if saveable, False if not

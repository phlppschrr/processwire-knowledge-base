# $pagesEditor->setupNew(Page $page)

Source: `wire/core/PagesEditor.php`

Auto-populate some fields for a new page that does not yet exist

Currently it does this:

- Assigns a parent if one is not already assigned.
- Sets up a unique page->name based on the format or title if one isn't provided already.
- Assigns a sort value.
- Populates any default values for fields.

## Usage

~~~~~
// basic usage
$result = $pagesEditor->setupNew($page);

// usage with all arguments
$result = $pagesEditor->setupNew(Page $page);
~~~~~

## Arguments

- `$page` `Page`

## Exceptions

- `\Exception|WireException|\PDOException` if failure occurs while in DB transaction

# $markupFieldtype->isLinkablePageProperty(Page $page, $property): bool

Source: `wire/core/MarkupFieldtype.php`

Is the given page property/field name one that should be linked to the source page in output?

## Usage

~~~~~
// basic usage
$bool = $markupFieldtype->isLinkablePageProperty($page, $property);

// usage with all arguments
$bool = $markupFieldtype->isLinkablePageProperty(Page $page, $property);
~~~~~

## Arguments

- `$page` `Page`
- $property

## Return value

- `bool`

# InputfieldPageTableAjax

Source: `wire/modules/Inputfield/InputfieldPageTable/InputfieldPageTableAjax.php`

Inherits: `Wire`

## Summary

Ajax handler for FieldtypePageTable/InputfieldPageTable

Common methods:
- [`checkAjax()`](method-___checkajax.md)
- [`renderAjax()`](method-renderajax.md)
- [`addItem()`](method-additem.md)
- [`sortItems()`](method-sortitems.md)

Groups:
Group: [other](group-other.md)

Concept by Antti Peisa
Code by Ryan Cramer
Sponsored by Avoine

## Methods
- [`__construct()`](method-__construct.md) Construct
- [`checkAjax()`](method-___checkajax.md) (hookable) Check if current request is a valid ajax request and call renderAjax() if it is.
- [`renderAjax(Page $page, Field $field)`](method-renderajax.md) Render the ajax request output directly and halt execution
- [`addItem(Page $page, Field $field, Page $item): bool`](method-additem.md) Handler for the InputfieldPageTableAdd ajax action
- [`sortItems(Page $page, Field $field, string $sort)`](method-sortitems.md) Update items to make sure they are in same order specified in GET var InputfieldPageTableSort

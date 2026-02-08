# $page->___links($selector = '', $field = ''): PageArray

Source: `wire/core/Page.php`

Return pages linking to this one (in Textarea/HTML fields)

Applies only to Textarea fields with “html” content-type and link abstraction enabled.

## Arguments

- string|bool $selector Optional selector to filter by or boolean true for “include=all”. (default='')
- string|Field $field Optionally limit results to specified field. (default=all applicable Textarea fields)

## Return value

PageArray

## Meta

- @since 3.0.107

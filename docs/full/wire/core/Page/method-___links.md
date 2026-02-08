# Page::___links()

Source: `wire/core/Page.php`

Return pages linking to this one (in Textarea/HTML fields)

Applies only to Textarea fields with “html” content-type and link abstraction enabled.


@param string|bool $selector Optional selector to filter by or boolean true for “include=all”. (default='')

@param string|Field $field Optionally limit results to specified field. (default=all applicable Textarea fields)

@return PageArray

@since 3.0.107

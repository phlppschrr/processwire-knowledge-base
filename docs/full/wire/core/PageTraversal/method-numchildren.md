# PageTraversal::numChildren()

Source: `wire/core/PageTraversal.php`

Return number of children, optionally with conditions

Use this over $page->numChildren property when you want to specify a selector or when you want the result to
include only visible children. See the options for the $selector argument.

@param Page $page

@param bool|string|int|array $selector
	When not specified, result includes all children without conditions, same as $page->numChildren property.
	When a string or array, a selector is assumed and quantity will be counted based on selector.
	When boolean true, number includes only visible children (excludes unpublished, hidden, no-access, etc.)
	When boolean false, number includes all children without conditions, including unpublished, hidden, no-access, etc.
	When integer 1 number includes viewable children (as opposed to visible, viewable includes hidden pages + it also includes unpublished pages if user has page-edit permission).

@param array $options
 - `descendants` (bool): Use descendants rather than direct children

@return int Number of children

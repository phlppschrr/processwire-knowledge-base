# MarkupQA::verbose()

Source: `wire/core/MarkupQA.php`

Get or set verbose state

Whether or not to set/track verbose information to page, i.e.
`$page->_markupQA = array('field_name' => array(counts))`

When getting, if $page or $field have not been populated, verbose is always false.

@param bool|null $set Omit this argument to get or specify bool to set

@return bool

# Templates::getParentPages()

Source: `wire/core/Templates.php`

Return all possible parent pages for the given template, if predefined

@param Template $template

@param bool $checkAccess Specify true to exclude parent pages that user doesn't have access to add pages to (default=false)

@param int $maxStatus Max allowed `Page::status*` constant (default=0 which means not applicable). Since 3.0.138

@return PageArray

# Page::is()

Source: `wire/core/Page.php`

Does this page have the specified status number or template name?

See status flag constants at top of Page class.
You may also use status names: hidden, locked, unpublished, system, systemID


@param int|string|Selectors $status Status number, status name, or Template name or selector string/object

@return bool

# PagesRequest::checkAccessDelegated()

Source: `wire/core/PagesRequest.php`

Check access to a delegated page (like a repeater)

Note: this should move to PagePermissions.module or FieldtypeRepeater.module
if a similar check is needed somewhere else in the core.

@param Page $page

@return Page|null|bool

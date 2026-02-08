# PagesEditor::setupPageName()

Source: `wire/core/PagesEditor.php`

Auto-assign a page name to gven page

Typically this would be used only if page had no name or if it had a temporary untitled name.

Page will be populated with the name given. This method will not populate names to pages that
already have a name, unless the name is "untitled"


@param Page $page

@param array $options
	- format: Optionally specify the format to use, or leave blank to auto-determine.

@return string If a name was generated it is returned. If no name was generated blank is returned.

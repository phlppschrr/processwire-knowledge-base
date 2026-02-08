# PagesEditor::addStatus()

Source: `wire/core/PagesEditor.php`

Silently add status flag to a Page and save

This action does not update the Page modified date.
It updates the status for both the given instantiated Page object and the value in the DB.


@param Page $page

@param int $status Use Page::status* constants

@return bool

@since 3.0.146

@see PagesEditor::setStatus(), PagesEditor::removeStatus()

# PagesEditor::savePageFinish()

Source: `wire/core/PagesEditor.php`

Save individual Page fields and supporting actions

triggers hooks: saved, added, moved, renamed, templateChanged

@param Page $page

@param bool $isNew

@param array $options

@return bool

@throws \Exception|WireException|\PDOException If any field-saving failure occurs while in a DB transaction

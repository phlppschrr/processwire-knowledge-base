# Template: behaviors

Source: `wire/core/Template.php`

@property int $allowChangeUser Allow the createdUser/created_users_id field of pages to be changed? (with API or in admin w/superuser only). 0=no, 1=yes

@property int $noGlobal Template should ignore the global option of fields? (0=no, 1=yes)

@property int $noMove Pages using this template are not moveable? (0=moveable, 1=not movable)

@property int $noTrash Pages using this template may not go in trash? (i.e. they will be deleted not trashed) (0=trashable, 1=not trashable)

@property int $noSettings Don't show a settings tab on pages using this template? (0=use settings tab, 1=no settings tab)

@property int $noChangeTemplate Don't allow pages using this template to change their template? (0=template change allowed, 1=template change not allowed)

@property int $noUnpublish Don't allow pages using this template to ever exist in an unpublished state - if page exists, it must be published. (0=page may be unpublished, 1=page may not be unpublished)

@property int $noShortcut Don't allow pages using this template to appear in shortcut "add new page" menu.

@property int $noLang Disable multi-language for this template (when language support active).

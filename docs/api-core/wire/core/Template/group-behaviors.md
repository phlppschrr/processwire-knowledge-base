# Template: behaviors

Source: `wire/core/Template.php`

- `$allowChangeUser: int` Allow the createdUser/created_users_id field of pages to be changed? (with API or in admin w/superuser only). 0=no, 1=yes
- `$noGlobal: int` Template should ignore the global option of fields? (0=no, 1=yes)
- `$noMove: int` Pages using this template are not moveable? (0=moveable, 1=not movable)
- `$noTrash: int` Pages using this template may not go in trash? (i.e. they will be deleted not trashed) (0=trashable, 1=not trashable)
- `$noSettings: int` Don't show a settings tab on pages using this template? (0=use settings tab, 1=no settings tab)
- `$noChangeTemplate: int` Don't allow pages using this template to change their template? (0=template change allowed, 1=template change not allowed)
- `$noUnpublish: int` Don't allow pages using this template to ever exist in an unpublished state - if page exists, it must be published. (0=page may be unpublished, 1=page may not be unpublished)
- `$noShortcut: int` Don't allow pages using this template to appear in shortcut "add new page" menu.
- `$noLang: int` Disable multi-language for this template (when language support active).

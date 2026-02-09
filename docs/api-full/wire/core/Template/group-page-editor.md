# Template: page-editor

Source: `wire/core/Template.php`

- `$nameContentTab: int` Pages should display the name field on the content tab? (0=no, 1=yes)
- `$tabContent: string` Optional replacement for default "Content" label
- `$tabChildren: string` Optional replacement for default "Children" label
- `$nameLabel: string` Optional replacement for the default "Name" label on pages using this template
- `$errorAction: int` Action to take when published page missing required field is saved (0=notify only, 1=restore prev value, 2=unpublish page)

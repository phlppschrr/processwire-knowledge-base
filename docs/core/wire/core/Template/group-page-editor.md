# Template: page-editor

Source: `wire/core/Template.php`

@property int $nameContentTab Pages should display the name field on the content tab? (0=no, 1=yes)

@property string $tabContent Optional replacement for default "Content" label

@property string $tabChildren Optional replacement for default "Children" label

@property string $nameLabel Optional replacement for the default "Name" label on pages using this template

@property int $errorAction Action to take when published page missing required field is saved (0=notify only, 1=restore prev value, 2=unpublish page)

# AdminThemeFramework: other

Source: `wire/core/AdminThemeFramework.php`

@property bool $isSuperuser

@property bool $isEditor

@property bool $isLoggedIn

@property bool|string $isModal

@property bool|int $useAsLogin

@property string $browserTitle Optional custom browser title for this request (3.0.217+)

@method array getUserNavArray()

@method array getPrimaryNavArray()

@method string renderFile($basename, array $vars = [])

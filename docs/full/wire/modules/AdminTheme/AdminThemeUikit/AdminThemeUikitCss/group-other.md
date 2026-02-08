# AdminThemeUikitCss: other

Source: `wire/modules/AdminTheme/AdminThemeUikit/AdminThemeUikitCss.php`

@property bool $upgrade Set to true when upgrading core Uikit version. (default=false)

@property string $frameworkLessFile Full disk path to LESS file that includes the framework/Uikit.

@property array $baseStyles Base style options (default=[ 'reno', 'rock' ])

@property string $defaultStyle Default style (default='reno')

@property string $defaultCssFile Core CSS file to create when upgrading (relative to module root)

@property string $styleDir Directory where base .less files are located (relative to module root)

@property array $replacements Array of [find=>replace] for compiled CSS file.

@property string $configPhpHash Hash used internally to detect changes to $config->AdminThemeUikit settings.

@property string $configPhpName Name of property in $config that holds custom settings (default='AdminThemeUikit').

@property int $requireCssVersion

@property int $cssVersion

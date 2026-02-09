# AdminThemeUikitCss: other

Source: `wire/modules/AdminTheme/AdminThemeUikit/AdminThemeUikitCss.php`

- $upgrade: bool Set to true when upgrading core Uikit version. (default=false)

- $frameworkLessFile: string Full disk path to LESS file that includes the framework/Uikit.

- $baseStyles: array Base style options (default=[ 'reno', 'rock' ])

- $defaultStyle: string Default style (default='reno')

- $defaultCssFile: string Core CSS file to create when upgrading (relative to module root)

- $styleDir: string Directory where base .less files are located (relative to module root)

- $replacements: array Array of [find=>replace] for compiled CSS file.

- $configPhpHash: string Hash used internally to detect changes to $config->AdminThemeUikit settings.

- $configPhpName: string Name of property in $config that holds custom settings (default='AdminThemeUikit').

- $requireCssVersion: int

- $cssVersion: int

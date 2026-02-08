# AdminThemeUikitCss

Source: `wire/modules/AdminTheme/AdminThemeUikit/AdminThemeUikitCss.php`

AdminThemeUikit CSS

Manages selection of CSS file and determines when CSS file to be recompiled from LESS
source files.



Settings that may be specified in $config->AdminThemeUikit array:

@property string $style Configured style name to use, one of blank (for default), 'reno' or 'rock'.

@property bool $recompile Recompile all LESS to CSS now? (set to true for 1 request only)

@property bool $compress Compress compiled CSS? (default=true)

@property array $customLessFiles Custom .less file(s) to include, relative to PW root.

@property string $customCssFile Custom target .css file to compile custom .less file(s) to, relative to PW root.

@property array $vars LESS variables to be used when compiling. Eg ['rock-primary' => '#FF0000']

@property string $parse LESS string to parse, eg "@rock-primary: #FF0000;"

@since 3.0.179

Groups:
Group: [other](group-other.md)

Methods:
Method: [__construct()](method-__construct.md)
Method: [getDefaults()](method-getdefaults.md)
Method: [getCssFile()](method-getcssfile.md)
Method: [fileToUrl()](method-filetourl.md)
Method: [getDefaultCssFile()](method-getdefaultcssfile.md)
Method: [configPhpSettingsChanged()](method-configphpsettingschanged.md)
Method: [customFile()](method-customfile.md)
Method: [getAdminStyleLessFile()](method-getadminstylelessfile.md)

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

## other

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

## __construct()

Construct

@param AdminTheme $adminTheme

@param array $options

## getDefaults()

@return array

## getCssFile()

Get the primary Uikit CSS file URL to use (whether default or custom)

@param bool $getPath Get disk path rather than URL?

@return string

## fileToUrl()

Get URL for given full path/file

@param string $file

@return string

## getDefaultCssFile()

Get default Uikit CSS file URL or disk path

@param bool $getPath

@return string

## configPhpSettingsChanged()

Have the $config->AdminThemeUikit settings changed?

@return bool

@throws WireException

## customFile()

Apply custom file/path replacements

@param string $file

@param string $requireExtension Extension to require on given file

@return string

## getAdminStyleLessFile()

Get admin base style file to use

@return string

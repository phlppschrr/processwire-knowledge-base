# AdminThemeUikitCss

Source: `wire/modules/AdminTheme/AdminThemeUikit/AdminThemeUikitCss.php`

Inherits: `WireData`


Groups:
Group: [other](group-other.md)

AdminThemeUikit CSS

Manages selection of CSS file and determines when CSS file to be recompiled from LESS
source files.



Settings that may be specified in $config->AdminThemeUikit array:

- `$style: string` Configured style name to use, one of blank (for default), 'reno' or 'rock'.
- `$recompile: bool` Recompile all LESS to CSS now? (set to true for 1 request only)
- `$compress: bool` Compress compiled CSS? (default=true)
- `$customLessFiles: array` Custom .less file(s) to include, relative to PW root.
- `$customCssFile: string` Custom target .css file to compile custom .less file(s) to, relative to PW root.
- `$vars: array` LESS variables to be used when compiling. Eg ['rock-primary' => '#FF0000']
- `$parse: string` LESS string to parse, eg "@rock-primary: #FF0000;"

@since 3.0.179

Methods:
- [`__construct(AdminTheme $adminTheme, array $options = array())`](method-__construct.md)
- [`getDefaults(): array`](method-getdefaults.md)
- [`getCssFile(bool $getPath = false): string`](method-getcssfile.md)
- [`fileToUrl(string $file): string`](method-filetourl.md)
- [`getDefaultCssFile(bool $getPath = false): string`](method-getdefaultcssfile.md)
- [`configPhpSettingsChanged(): bool`](method-configphpsettingschanged.md)
- [`customFile(string $file, string $requireExtension = ''): string`](method-customfile.md)
- [`getAdminStyleLessFile(): string`](method-getadminstylelessfile.md)

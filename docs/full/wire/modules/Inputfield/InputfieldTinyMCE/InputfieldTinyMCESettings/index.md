# InputfieldTinyMCESettings

Source: `wire/modules/Inputfield/InputfieldTinyMCE/InputfieldTinyMCESettings.php`

Inherits: `InputfieldTinyMCEClass`


Groups:
Group: [other](group-other.md)

InputfieldTinyMCETools

Helper for managing TinyMCE settings and defaults

Methods:
- [`getSettings(array|null $defaults = null, string $cacheKey = ''): array`](method-getsettings.md) Get settings from Inputfield vary from the $defaults
- [`getDefaults($key = ''): array`](method-getdefaults.md) Default settings for ProcessWire.config.InputfieldTinyMCE
- [`getOriginalDefaults(string $key = ''): array|mixed|null`](method-getoriginaldefaults.md) Get original defaults from source JSON, prior to being overriden by module default settings
- [`getAddDefaults(): array|mixed`](method-getadddefaults.md) Get 'add_' or 'replace_' default settings
- [`applyPlugins(array &$settings, array $defaults)`](method-applyplugins.md) Apply plugins settings
- [`applySkin(array &$settings, array $defaults)`](method-applyskin.md) Apply skin or skin_url directly to given settings/defaults
- [`getAlignClasses(): array`](method-getalignclasses.md) Get image alignment classes
- [`getFromSettingsFile(): array`](method-getfromsettingsfile.md) Get settings from custom settings file
- [`getFromSettingsJSON(): array`](method-getfromsettingsjson.md) Get settings from custom JSON
- [`getContentCssUrl(string $content_css = ''): string`](method-getcontentcssurl.md) Get content_css URL
- [`prepareSettingsForOutput(array $settings): array`](method-___preparesettingsforoutput.md) (hookable) Prepare given settings ready for output
- [`getLanguagePackCode(): string`](method-getlanguagepackcode.md) Get language pack code
- [`getLanguageSettings(): array`](method-getlanguagesettings.md) Get language pack settings
- [`applyAddSettings(array &$settings, array &$addSettings, array $defaults)`](method-applyaddsettings.md) Apply 'add_*' settings in $addSettings, plus merge all $addSettings into given $settings
- [`mergeSetting(string|array|mixed $value, string|array|mixed $addValue): string|array|mixed`](method-mergesetting.md) Merge two setting values into one that combines them
- [`mergeSettings(array $settings1, array $settings2 = array()): array`](method-mergesettings.md) Merge all settings in given array and combine those with "add_" prefix
- [`applyRenderReadySettings(array $addSettings = array())`](method-applyrenderreadysettings.md) Determine which settings go where and apply to Inputfield
- [`applySettingsField(string $fieldName): bool|Field`](method-applysettingsfield.md) Apply settings settings to $this->inputfield to inherit from another field

# InputfieldTinyMCESettings

Source: `wire/modules/Inputfield/InputfieldTinyMCE/InputfieldTinyMCESettings.php`

Inherits: `InputfieldTinyMCEClass`


Groups:
Group: [other](group-other.md)

InputfieldTinyMCETools

Helper for managing TinyMCE settings and defaults

Methods:
- [`getSettings(array|null $defaults = null, string $cacheKey = ''): array`](method-getsettings.md)
- [`getDefaults($key = ''): array`](method-getdefaults.md)
- [`getOriginalDefaults(string $key = ''): array|mixed|null`](method-getoriginaldefaults.md)
- [`getAddDefaults(): array|mixed`](method-getadddefaults.md)
- [`applyPlugins(array &$settings, array $defaults)`](method-applyplugins.md)
- [`applySkin(array &$settings, array $defaults)`](method-applyskin.md)
- [`getAlignClasses(): array`](method-getalignclasses.md)
- [`getFromSettingsFile(): array`](method-getfromsettingsfile.md)
- [`getFromSettingsJSON(): array`](method-getfromsettingsjson.md)
- [`getContentCssUrl(string $content_css = ''): string`](method-getcontentcssurl.md)
- [`prepareSettingsForOutput(array $settings): array`](method-___preparesettingsforoutput.md) (hookable)
- [`getLanguagePackCode(): string`](method-getlanguagepackcode.md)
- [`getLanguageSettings(): array`](method-getlanguagesettings.md)
- [`applyAddSettings(array &$settings, array &$addSettings, array $defaults)`](method-applyaddsettings.md)
- [`mergeSetting(string|array|mixed $value, string|array|mixed $addValue): string|array|mixed`](method-mergesetting.md)
- [`mergeSettings(array $settings1, array $settings2 = array()): array`](method-mergesettings.md)
- [`applyRenderReadySettings(array $addSettings = array())`](method-applyrenderreadysettings.md)
- [`applySettingsField(string $fieldName): bool|Field`](method-applysettingsfield.md)

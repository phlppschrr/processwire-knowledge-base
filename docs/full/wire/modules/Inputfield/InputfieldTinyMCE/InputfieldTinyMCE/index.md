# InputfieldTinyMCE

Source: `wire/modules/Inputfield/InputfieldTinyMCE/InputfieldTinyMCE.module.php`

Inherits: `InputfieldTextarea`
Implements: `ConfigurableModule`

InputfieldTinyMCE


TinyMCE 6.x, Copyright (c) 2023 Ephox Corporation DBA Tiny Technologies, Inc.
https://www.tiny.cloud/docs/tinymce/6/


TinyMCE settings (these are also Field settings)
------------------------------------------------

- `$plugins: string` Space-separated string of plugins to enable
- `$toolbar: string` Space-separated string of tools to show in toolbar
- `$contextmenu: string` Space-separated string of tools to show in context menu
- `$removed_menuitems: string` Space-separated string of tools to remove from menubar
- `$invalid_styles: string` Space-separated string of invalid inline styles
- `$menubar: string` Space-separated list of top-level menubar items
- `$height: int` Height of editor in pixels

Field/Inputfield settings
-------------------------

- `$inlineMode: int` Use inline mode? 0=Regular editor, 1=Inline editor, 2=Fixed height inline editor
- `$lazyMode: int` Use lazy-loading mode? 0=Off, 1=Lazy, 2=Extra lazy
- `$toggles: array` Markup toggles, see self::toggle* constants
- `$features: array` General features: toolbar, menubar, statusbar, stickybars, spellcheck, purifier, imgUpload, imgResize, pasteFilter
- `$headlines: array` Allowed headline types
- `$settingsFile: string` Location of optional custom-settings.json settings file (URL relative to PW root URL)
- `$settingsField: string` Alternate field to inherit settings from rather than configure settings with this instance.
- `$settingsJSON: string` JSON with custom settings that override the defaults
- `$styleFormatsCSS: string` Style formats as CSS to parse and apply to style_formats and content_style
- `$extPlugins: array` Additional plugins to enable for this field (URL paths from customPluginOptions)

Module settings
---------------

- `$content_css: string` Basename of content CSS file to use or "custom" to use custom URL (default=wire)
- `$content_css_url: string` Applies only if $content_css has value "custom"
- `$skin: string` Skin to use (default=oxide)
- `$skin_url: string` URL to skin
- `$extPluginOpts: string` Newline separated URL paths (relative to PW root) of extra plugin .js files
- `$defaultsFile: string` Location of optional defaults.json file that merges with defaults.json (URL relative to PW root URL)
- `$defaultsJSON: string` JSON that merges with the defaults.json for all instances
- `$optionals: array` Names of optional settings that can be configured per-field
- `$debugMode: bool|int` Makes InputfieldTinyMCE.js use verbose console.log() messages (default=false)
- `$extraCSS: string` Extra CSS for editor, applies to all editors (appended to TinyMCE content_style setting)
- `$pasteFilter: string` Rule string of elements and attributes allowed during filtered paste
- `$imageFields: array` Names of fields allowed for drag-drop in images
There are also `$lang_name=packname` settings in multi-lang sites where "name" is lang name and "packname" is lang pack name

Runtime settings
----------------

- `$configName: string` Name of configuration set to use (default=blank)
- `$readonly: bool` Are we in read-only mode? Automatically set during renderValue mode. This is a read-only property. (default=false)
- `$initialized: bool` Is the editor initialized? This is a read-only property. (default=false)
- `$external_plugins: array` URLs of external plugins, this is also a TinyMCE setting
- [`getModuleConfigInputfields(InputfieldWrapper $inputfields): void`](method-___getmoduleconfiginputfields.md)

Methods:
- [`getModuleInfo(): array`](method-getmoduleinfo.md)
- [`__construct()`](method-__construct.md)
- [`init()`](method-init.md)
- [`useFeature(string $name): bool`](method-usefeature.md)
- [`mcePath(bool $getUrl = false): string`](method-mcepath.md)
- [`setConfigName(string $configName): $this`](method-setconfigname.md)
- [`getConfigName(): string`](method-getconfigname.md)
- [`configurable(bool $set = null): bool`](method-configurable.md)
- [`get($key): array|mixed|string|null`](method-get.md)
- [`set($key, $value): self`](method-set.md)
- [`getExtraStyles(): string`](method-getextrastyles.md)
- [`renderReadyOnce()`](method-renderreadyonce.md)
- [`renderReady(?Inputfield $parent = null, bool $renderValueMode = false): bool`](method-renderready.md)
- [`render(): string`](method-___render.md) (hookable)
- [`renderNormal(): string`](method-rendernormal.md)
- [`renderInline(): string`](method-renderinline.md)
- [`renderInitScript(): string`](method-renderinitscript.md)
- [`renderValue(): string`](method-___rendervalue.md) (hookable)
- [`processInput(WireInputData $input): $this`](method-___processinput.md) (hookable)
- [`getSettingNames(array|string $types): string[]`](method-getsettingnames.md)
- [`addPlugin(string $file)`](method-addplugin.md)
- [`removePlugin(string $file): bool`](method-removeplugin.md)
- [`getDirectionality(): string`](method-getdirectionality.md)
- [`helper(string $name): InputfieldTinyMCEClass`](method-helper.md)
- [`getConfigInputfields(): InputfieldWrapper`](method-___getconfiginputfields.md) (hookable)
- [`getModuleConfigInputfields(InputfieldWrapper $inputfields)`](method-___getmoduleconfiginputfields.md) (hookable)

Constants:
- [`mceVersion`](const-mceversion.md)
- [`defaultPasteFilter`](const-defaultpastefilter.md)

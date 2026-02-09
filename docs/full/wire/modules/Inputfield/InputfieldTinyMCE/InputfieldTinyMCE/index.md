# InputfieldTinyMCE

Source: `wire/modules/Inputfield/InputfieldTinyMCE/InputfieldTinyMCE.module.php`

Inherits: `InputfieldTextarea`
Implements: `ConfigurableModule`

InputfieldTinyMCE


TinyMCE 6.x, Copyright (c) 2023 Ephox Corporation DBA Tiny Technologies, Inc.
https://www.tiny.cloud/docs/tinymce/6/


TinyMCE settings (these are also Field settings)
------------------------------------------------

- $plugins: string Space-separated string of plugins to enable
- $toolbar: string Space-separated string of tools to show in toolbar
- $contextmenu: string Space-separated string of tools to show in context menu
- $removed_menuitems: string Space-separated string of tools to remove from menubar
- $invalid_styles: string Space-separated string of invalid inline styles
- $menubar: string Space-separated list of top-level menubar items
- $height: int Height of editor in pixels

Field/Inputfield settings
-------------------------

- $inlineMode: int Use inline mode? 0=Regular editor, 1=Inline editor, 2=Fixed height inline editor
- $lazyMode: int Use lazy-loading mode? 0=Off, 1=Lazy, 2=Extra lazy
- $toggles: array Markup toggles, see self::toggle* constants
- $features: array General features: toolbar, menubar, statusbar, stickybars, spellcheck, purifier, imgUpload, imgResize, pasteFilter
- $headlines: array Allowed headline types
- $settingsFile: string Location of optional custom-settings.json settings file (URL relative to PW root URL)
- $settingsField: string Alternate field to inherit settings from rather than configure settings with this instance.
- $settingsJSON: string JSON with custom settings that override the defaults
- $styleFormatsCSS: string Style formats as CSS to parse and apply to style_formats and content_style
- $extPlugins: array Additional plugins to enable for this field (URL paths from customPluginOptions)

Module settings
---------------

- $content_css: string Basename of content CSS file to use or "custom" to use custom URL (default=wire)
- $content_css_url: string Applies only if $content_css has value "custom"
- $skin: string Skin to use (default=oxide)
- $skin_url: string URL to skin
- $extPluginOpts: string Newline separated URL paths (relative to PW root) of extra plugin .js files
- $defaultsFile: string Location of optional defaults.json file that merges with defaults.json (URL relative to PW root URL)
- $defaultsJSON: string JSON that merges with the defaults.json for all instances
- $optionals: array Names of optional settings that can be configured per-field
- $debugMode: bool|int Makes InputfieldTinyMCE.js use verbose console.log() messages (default=false)
- $extraCSS: string Extra CSS for editor, applies to all editors (appended to TinyMCE content_style setting)
- $pasteFilter: string Rule string of elements and attributes allowed during filtered paste
- $imageFields: array Names of fields allowed for drag-drop in images
There are also `$lang_name=packname` settings in multi-lang sites where "name" is lang name and "packname" is lang pack name

Runtime settings
----------------

- $configName: string Name of configuration set to use (default=blank)
- $readonly: bool Are we in read-only mode? Automatically set during renderValue mode. This is a read-only property. (default=false)
- $initialized: bool Is the editor initialized? This is a read-only property. (default=false)
- $external_plugins: array URLs of external plugins, this is also a TinyMCE setting
- [getModuleConfigInputfields(InputfieldWrapper $inputfields): void](method-___getmoduleconfiginputfields.md)

Methods:
Method: [getModuleInfo()](method-getmoduleinfo.md)
Method: [__construct()](method-__construct.md)
Method: [init()](method-init.md)
Method: [useFeature()](method-usefeature.md)
Method: [mcePath()](method-mcepath.md)
Method: [setConfigName()](method-setconfigname.md)
Method: [getConfigName()](method-getconfigname.md)
Method: [configurable()](method-configurable.md)
Method: [get()](method-get.md)
Method: [set()](method-set.md)
Method: [getExtraStyles()](method-getextrastyles.md)
Method: [renderReadyOnce()](method-renderreadyonce.md)
Method: [renderReady()](method-renderready.md)
Method: [render()](method-___render.md) (hookable)
Method: [renderNormal()](method-rendernormal.md)
Method: [renderInline()](method-renderinline.md)
Method: [renderInitScript()](method-renderinitscript.md)
Method: [renderValue()](method-___rendervalue.md) (hookable)
Method: [processInput()](method-___processinput.md) (hookable)
Method: [getSettingNames()](method-getsettingnames.md)
Method: [addPlugin()](method-addplugin.md)
Method: [removePlugin()](method-removeplugin.md)
Method: [getDirectionality()](method-getdirectionality.md)
Method: [helper()](method-helper.md)
Method: [getConfigInputfields()](method-___getconfiginputfields.md) (hookable)
Method: [getModuleConfigInputfields()](method-___getmoduleconfiginputfields.md) (hookable)

Constants:
Const: [mceVersion](const-mceversion.md)
Const: [defaultPasteFilter](const-defaultpastefilter.md)

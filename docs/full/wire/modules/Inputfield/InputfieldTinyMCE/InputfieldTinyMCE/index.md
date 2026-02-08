# InputfieldTinyMCE

Source: `wire/modules/Inputfield/InputfieldTinyMCE/InputfieldTinyMCE.module.php`

InputfieldTinyMCE

ProcessWire 3.x, Copyright 2024 by Ryan Cramer
https://processwire.com

TinyMCE 6.x, Copyright (c) 2023 Ephox Corporation DBA Tiny Technologies, Inc.
https://www.tiny.cloud/docs/tinymce/6/


TinyMCE settings (these are also Field settings)
------------------------------------------------

@property string $plugins Space-separated string of plugins to enable

@property string $toolbar Space-separated string of tools to show in toolbar

@property string $contextmenu Space-separated string of tools to show in context menu

@property string $removed_menuitems Space-separated string of tools to remove from menubar

@property string $invalid_styles Space-separated string of invalid inline styles

@property string $menubar Space-separated list of top-level menubar items

@property int $height Height of editor in pixels

Field/Inputfield settings
-------------------------

@property int $inlineMode Use inline mode? 0=Regular editor, 1=Inline editor, 2=Fixed height inline editor

@property int $lazyMode Use lazy-loading mode? 0=Off, 1=Lazy, 2=Extra lazy

@property array $toggles Markup toggles, see self::toggle* constants

@property array $features General features: toolbar, menubar, statusbar, stickybars, spellcheck, purifier, imgUpload, imgResize, pasteFilter

@property array $headlines Allowed headline types

@property string $settingsFile Location of optional custom-settings.json settings file (URL relative to PW root URL)

@property string $settingsField Alternate field to inherit settings from rather than configure settings with this instance.

@property string $settingsJSON JSON with custom settings that override the defaults

@property string $styleFormatsCSS Style formats as CSS to parse and apply to style_formats and content_style

@property array $extPlugins Additional plugins to enable for this field (URL paths from customPluginOptions)

Module settings
---------------

@property string $content_css Basename of content CSS file to use or "custom" to use custom URL (default=wire)

@property string $content_css_url Applies only if $content_css has value "custom"

@property string $skin Skin to use (default=oxide)

@property string $skin_url URL to skin

@property string $extPluginOpts Newline separated URL paths (relative to PW root) of extra plugin .js files

@property string $defaultsFile Location of optional defaults.json file that merges with defaults.json (URL relative to PW root URL)

@property string $defaultsJSON JSON that merges with the defaults.json for all instances

@property array $optionals Names of optional settings that can be configured per-field

@property bool|int $debugMode Makes InputfieldTinyMCE.js use verbose console.log() messages (default=false)

@property string $extraCSS Extra CSS for editor, applies to all editors (appended to TinyMCE content_style setting)

@property string $pasteFilter Rule string of elements and attributes allowed during filtered paste

@property array $imageFields Names of fields allowed for drag-drop in images
There are also `$lang_name=packname` settings in multi-lang sites where "name" is lang name and "packname" is lang pack name

Runtime settings
----------------

@property string $configName Name of configuration set to use (default=blank)

@property-read bool $readonly Are we in read-only mode? Automatically set during renderValue mode. This is a read-only property. (default=false)

@property-read bool $initialized Is the editor initialized? This is a read-only property. (default=false)

@property array $external_plugins URLs of external plugins, this is also a TinyMCE setting

@method void getModuleConfigInputfields(InputfieldWrapper $inputfields)

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

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

## getModuleInfo()

Get module info

@return array

## mceVersion

TinyMCE version

## defaultPasteFilter

Default configuration for filtered paste

## __construct()

Construct

## init()

Init Inputfield

Module settings have already been populated at this point.

## useFeature()

Use the named feature?

@param string $name

@return bool

## mcePath()

Return path or URL to TinyMCE files

@param bool $getUrl

@return string

## setConfigName()

Set configuration name used to store settings in ProcessWire.config JS

i.e. ProcessWire.config.InputfieldTinyMCE.settings.[configName].[settingName]

@param string $configName

@return $this

## getConfigName()

Get configuration name used to store settings in ProcessWire.config JS

i.e. ProcessWire.config.InputfieldTinyMCE.settings.[configName].[settingName]

@return string

## configurable()

Get or set configurable state

- True if Inputfield is configurable (default state).
- False if it is required that another field be used ($settingsField) to pull settings from.
- Note this is completely unrelated to the $configName property.

@param bool $set

@return bool

## get()

Get

@param $key

@return array|mixed|string|null

## set()

Set

@param $key

@param $value

@return self

## getExtraStyles()

Get styles to add in <head>

@return string

## renderReadyOnce()

Render ready that only needs one call for entire request

## renderReady()

Render ready

@param Inputfield|null $parent

@param bool $renderValueMode

@return bool

## ___render()

Render Inputfield

@return string

## renderNormal()

Render normal/classic editor

@return string

## renderInline()

Render inline editor

@return string

## renderInitScript()

Render script to init editor

@return string

## ___renderValue()

Render non-editable value

@return string

## ___processInput()

Process input

@param WireInputData $input

@return $this

## getSettingNames()

Get all configurable setting names

@param array|string $types Types to get, one or more of: 'tinymce', 'field', 'module', 'optionals'

@return string[]

@throws WireException if given unknown setting type

## addPlugin()

Add an external plugin .js file

@param string $file File must be .js file relative to PW installation root, i.e. /site/templates/mce/myplugin.js

@throws WireException

## removePlugin()

Remove an external plugin .js file

@param string $file File must be .js file relative to PW installation root, i.e. /site/templates/mce/myplugin.js

@return bool

## getDirectionality()

Get directionality, either 'ltr' or 'rtl'

@return string

## helper()

Get helper

@param string $name

@return InputfieldTinyMCEClass

## ___getConfigInputfields()

Get Inputfield configuration settings

@return InputfieldWrapper

## ___getModuleConfigInputfields()

Module config

@param InputfieldWrapper $inputfields

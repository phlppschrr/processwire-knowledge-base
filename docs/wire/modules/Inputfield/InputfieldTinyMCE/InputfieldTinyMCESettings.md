# InputfieldTinyMCESettings

Source: `wire/modules/Inputfield/InputfieldTinyMCE/InputfieldTinyMCESettings.php`

InputfieldTinyMCETools

Helper for managing TinyMCE settings and defaults

ProcessWire 3.x, Copyright 2023 by Ryan Cramer
https://processwire.com

## other

@method array prepareSettingsForOutput(array $settings)

## getSettings()

Get settings from Inputfield vary from the $defaults

@param array|null $defaults Default settings Default settings or omit to pull automatically

@param string $cacheKey Optionally cache with this key

@return array

## getDefaults()

Default settings for ProcessWire.config.InputfieldTinyMCE

This should have no field-specific settings (no dynamic values)

@property string $key

@return array

## getOriginalDefaults()

Get original defaults from source JSON, prior to being overriden by module default settings

@param string $key

@return array|mixed|null

## getAddDefaults()

Get 'add_' or 'replace_' default settings

@return array|mixed

## applyPlugins()

Apply plugins settings

@param array $settings

@param array $defaults

## applySkin()

Apply skin or skin_url directly to given settings/defaults

@param array $settings

@param array $defaults

## getAlignClasses()

Get image alignment classes

@return array

## getFromSettingsFile()

Get settings from custom settings file

@return array

## getFromSettingsJSON()

Get settings from custom JSON

@return array

## getContentCssUrl()

Get content_css URL

@param string $content_css

@return string

## ___prepareSettingsForOutput()

Prepare given settings ready for output

This converts relative URLs to absolute, etc.

@param array $settings

@return array

## getLanguagePackCode()

Get language pack code

@return string

## getLanguageSettings()

Get language pack settings

@return array

## applyAddSettings()

Apply 'add_*' settings in $addSettings, plus merge all $addSettings into given $settings

This updates the $settings and $addSettings variables directly

@param array $settings

@param array $addSettings

@param array $defaults

## mergeSetting()

Merge two setting values into one that combines them

@param string|array|mixed $value

@param string|array|mixed $addValue

@return string|array|mixed

## mergeSettings()

Merge all settings in given array and combine those with "add_" prefix

@param array $settings1

@param array $settings2 Optionally specify this to merge/combine with those in $settings1

@return array

## applyRenderReadySettings()

Determine which settings go where and apply to Inputfield

@param array $addSettings Optionally add this settings on top of those that would otherwise be used

## applySettingsField()

Apply settings settings to $this->inputfield to inherit from another field

This is called from the main InputfieldTinyMCE class.

@param string $fieldName Field name or 'fieldName:id' string

@return bool|Field Returns false or field inherited from

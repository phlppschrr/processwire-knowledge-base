# AdminThemeFramework

Source: `wire/core/AdminThemeFramework.php`

AdminTheme Framework

The methods in this class may eventually be merged to AdminTheme.php,
but are isolated to this class during development.

This file is licensed under the MIT license.
https://processwire.com/about/license/mit/

ProcessWire 3.x, Copyright 2022 by Ryan Cramer
https://processwire.com

## other

@property bool $isSuperuser

@property bool $isEditor

@property bool $isLoggedIn

@property bool|string $isModal

@property bool|int $useAsLogin

@property string $browserTitle Optional custom browser title for this request (3.0.217+)

@method array getUserNavArray()

@method array getPrimaryNavArray()

@method string renderFile($basename, array $vars = [])

## __construct()

Construct

## get()

Override get() method from WireData to support additional properties

@param string $key

@return bool|int|mixed|null|string

## init()

Initialize and attach hooks

Note: descending classes should call this after API ready

## includeInitFile()

Include the admin theme init file

## _()

Perform a translation, based on text from shared admin file: /wire/templates-admin/default.php

@param string $text

@return string

## getHeadline()

Get the current page headline

@return string

## getPageTitle()

Get navigation title for the given page, return blank if page should not be shown

@param Page $p

@return string

## getPageIcon()

Get icon used by the given page

@param Page $p

@return mixed|null|string

## getAddNewActions()

Get “Add New” button actions

- Returns array of arrays, each with 'url', 'label' and 'icon' properties.
- Returns empty array if Add New button should not be displayed.

@return array

## getAddNewLabel()

Get the translated “Add New” label that’s used in a couple spots

@return string

## getBodyClass()

Get the classes that will be used in the <body class=''> tag

@return string

## getHeadJS()

Get Javascript that must be present in the document <head>

@return string

## allowPageInNav()

Allow the given Page to appear in admin theme navigation?

@param Page $p Page to test

@param PageArray|array $children Children of page, if applicable (optional)

@param string|null $permission Specify required permission (optional)

@return bool

## ___getPrimaryNavArray()

Return nav array of primary navigation

@return array

## moduleToNavArray()

Get navigation array from a Process module

@param array|Module|string $module Module info array or Module object or string

@param Page $p Page upon which the Process module is contained

@return array

## pageToNavArray()

Get a navigation array the given Page, or null if page not allowed in nav

@param Page $p

@return array|null

## ___getUserNavArray()

Get navigation items for the “user” menu

This is hookable so that something else could add stuff to it.
See the method body for details on format used.

Supported properties/attributes as of 3.0.248:

- url (href)
- title (label text)
- target (html attr)
- icon (name of icon)
- permission (required permission)
- id (html attr)
- class (html attr)
- onclick (html attr)
- data-* (html attr)

@return array

## getBrowserTitle()

Get the browser <title>

@return string

## testNotices()

Test all notice types

@return bool

## renderNotices()

Render runtime notices div#notices

@param Notices|bool $notices Notices object or specify boolean true to return array of all available $options

@param array $options See defaults in method

@return string|array Returns string unless you specify true for $notices argument, then it returns an array.

## renderIcon()

Render markup for a font-awesome icon

@param string $icon Name of icon to render, excluding the “fa-” prefix

@param bool $fw Specify true to make fixed width (default=false).

@return string

## renderNavIcon()

Render markup for a font-awesome icon that precedes a navigation label

This is the same as renderIcon() except that fixed-width is assumed and a "nav-nav-icon"
class is added to it.

@param string $icon Name of icon to render, excluding the “fa-” prefix

@return string

## renderExtraMarkup()

Render an extra markup region

@param string $for

@return mixed|string

## ___renderFile()

Render a admin theme template file

This method is only used if it is hooked


@param string $file Full path and filename

@param array $vars Associative array of variables to populate in rendered file

@return string Returns blank string when $echo is true

@since 3.0.196

## includeFile()

Include an admin theme file

@param string $basename

@param array $vars

@since 3.0.196

## setCustomTemplatePath()

Set custom path for admin theme templates

This is for modules to optionally set a custom template path. If not set then the default
in /site/templates/AdminTheme[Class]/ is used.

@param string $path

@since 3.0.196

## getModuleConfigInputfields()

Module Configuration

@param InputfieldWrapper $inputfields

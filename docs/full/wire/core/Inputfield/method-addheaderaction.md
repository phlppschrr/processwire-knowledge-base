# $inputfield->addHeaderAction(array $settings = array()): array

Source: `wire/core/Inputfield.php`

Add header action

This adds a clickable icon to the right side of the Inputfield header.
There are three types of actions: 'click', 'toggle' and 'link'. The 'click'
action simply triggers your JS event whenever it is clicked. The 'toggle' action
has an on/off state, and you can specify the JS event to trigger for each.
This function will automatically figure out whether you want a `click`,
`toggle` or 'link' action based on what you provide in the $settings argument.
Below is a summary of these settings:

Settings for 'click' or 'link' type actions
-------------------------------------------
- `icon` (string): Name of font-awesome icon to use.
- `tooltip` (string): Optional tooltip text to display when icon hovered.
- `event` (string): Event name to trigger in JS when clicked ('click' actions only).
- `href` (string): URL to open ('link' actions only).
- `modal` (bool): Specify true to open link in modal ('link' actions only).
- `target` (string): Optional target attribute i.e. '_blank'.

Settings for 'toggle' (on/off) type actions
-------------------------------------------
- `on` (bool): Start with the 'on' state? (default=false)
- `onIcon` (string): Name of font-awesome icon to show for on state.
- `onEvent` (string): JS event name to trigger when toggled on.
- `onTooltip` (string): Tooltip text to show when on icon is hovered.
- `offIcon` (string): Name of font-awesome icon to show for off state.
- `offEvent` (string): JS event name to trigger when toggled off.
- `offTooltip` (string): Tooltip text to show when off icon is hovered.

Other/optional settings (applies to all types)
----------------------------------------------
- `name` (string): Name of this action (-_a-zA-Z0-9).
- `parent` (string): Name of parent action, if this action is part of a menu.
- `overIcon` (string): Name of font-awesome icon to show when hovered.
- `overEvent` (string): JS event name to trigger when mouse is over the icon.
- `downIcon` (string): Icon to display when mouse is down on the action icon (3.0.241+).
- `downEvent` (string): JS event name to trigger when mouse is down on the icon (3.0.241+).
- `cursor` (string): CSS cursor name to show when mouse is over the icon.
- `setAll` (array): Set all of the header actions in one call, replaces any existing.
   Note: to get all actions, call the method and omit the $settings argument.

Settings for dropdown menu actions (3.0.241+)
---------------------------------------------
 Note that menu type actions also require jQuery UI and /wire/templates-admin/scripts/main.js,
 both of which are already present in PW’s admin themes (AdminThemeUikit recommended).
 Requires ProcessWire 3.0.241 or newer.
 - `icon` (string): Icon name to use for dropdown toggle, i.e. 'fa-wrench'.
 - `tooltip` (string): Optional tooltip to describe what the dropdown is for.
 - `menuAction` (string): Action that toggles the menu to show, one of 'click' or 'hover' (default).
 - `menuItems` (array): Definition of menu items, each with one or more of the following properties.
    - `label` (string): Label text for the menu item (required).
    - `icon` (string): Icon name for the menu item, if desired.
    - `callback` (function|null): JS callback to execute item is clicked (not applicable in PHP).*
    - `event` (string): JS event name to trigger when item is clicked.
    - `tooltip` (string): Tooltip text to show when hovering menu item (title attribute).
    - `href` (string): URL to go to when menu item clicked.
    - `target` (string): Target attribute when href is used (i.e. "_blank").
    - `modal` (bool): Open href in modal window instead?
    - `active` (function|bool): Callback function that returns true if menu item active, or false.*
       if disabled. You can also directly specify true or false for this option.
    - NOTE 1: All `menuItems` properties above are optional, except for 'label'.
    - NOTE 2: To use `callback` or `active` as functions, you must define your menu in JS instead.
    - NOTE 3: For examples see the addHeaderAction() method in /wire/templates-admin/scripts/inputfields.js

## Arguments

- `$settings` (optional) `array` Specify array containing the appropriate settings above.

## Return value

array Returns all currently added actions.

## Since

3.0.240

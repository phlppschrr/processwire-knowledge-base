# admin

Source: `wire/core/admin.php`

Controller for ProcessWire Admin

This file is designed for inclusion by /site/templates/admin.php template and all the variables
it references are from your template namespace.


@var Config $config

@var User $user

@var Modules $modules

@var Pages $pages

@var Page $page

@var ProcessWire $wire

@var WireInput $input

@var Sanitizer $sanitizer

@var Session $session

@var Notices $notices

@var AdminTheme $adminTheme

## Methods
- [`_hookSessionRedirectModal(HookEvent $event)`](method-_hooksessionredirectmodal.md) Ensures a modal GET variable is retained through redirects, when appropriate
- [`_checkForHttpHostError(Config $config)`](method-_checkforhttphosterror.md) Check if the current HTTP host is recognized and generate error if not
- [`_checkForTwoFactorAuth(Session $session)`](method-_checkfortwofactorauth.md) Check if two factor authentication is being required and display warning with link to configure
- [`_checkForMaxInputVars(WireInput $input)`](method-_checkformaxinputvars.md) Check if POST request exceeds PHP’s max_input_vars
- [`_setupForDemoMode(Page $page, ProcessWire $wire)`](method-_setupfordemomode.md) Setup for demo mode

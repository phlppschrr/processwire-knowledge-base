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

Methods:
- [`_hookSessionRedirectModal(HookEvent $event)`](method-_hooksessionredirectmodal.md)
- [`_checkForHttpHostError(Config $config)`](method-_checkforhttphosterror.md)
- [`_checkForTwoFactorAuth(Session $session)`](method-_checkfortwofactorauth.md)
- [`_checkForMaxInputVars(WireInput $input)`](method-_checkformaxinputvars.md)
- [`_setupForDemoMode(Page $page, ProcessWire $wire)`](method-_setupfordemomode.md)

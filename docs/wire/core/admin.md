# admin

Source: `wire/core/admin.php`

Controller for ProcessWire Admin

This file is designed for inclusion by /site/templates/admin.php template and all the variables
it references are from your template namespace.

Copyright 2024 by Ryan Cramer

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

## _hookSessionRedirectModal()

Ensures a modal GET variable is retained through redirects, when appropriate

@param HookEvent $event

## _checkForHttpHostError()

Check if the current HTTP host is recognized and generate error if not

@param Config $config

## _checkForTwoFactorAuth()

Check if two factor authentication is being required and display warning with link to configure

@param Session $session

## _checkForMaxInputVars()

Check if POST request exceeds PHP’s max_input_vars

@param WireInput $input

## _setupForDemoMode()

Setup for demo mode

@param Page $page

@param ProcessWire $wire

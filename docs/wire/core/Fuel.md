# Fuel

Source: `wire/core/Fuel.php`

ProcessWire Fuel

Fuel maintains a single instance each of multiple objects used throughout the application.
The objects contained in fuel provide access to the ProcessWire API. For instance, $pages,
$users, $fields, and so on. The fuel is required to keep the system running, so to speak.

This file is licensed under the MIT license
https://processwire.com/about/license/mit/

ProcessWire 3.x, Copyright 2020 by Ryan Cramer
https://processwire.com

## other

@property ProcessWire $wire

@property Database $db

@property WireDatabasePDO $database

@property Session $session

@property Notices $notices

@property Sanitizer $sanitizer

@property Fields $fields

@property Fieldtypes $fieldtypes

@property Fieldgroups $fieldgroups

@property Templates $templates

@property Pages $pages

@property Page $page

@property Process $process

@property Modules $modules

@property Permissions $permissions

@property Roles $roles

@property Users $users

@property User $user

@property WireCache $cache

@property WireInput $input

@property Languages $languages If LanguageSupport installed

@property Config $config

@property Fuel $fuel

@property WireProfilerInterface $profiler

@property WireFileTools $files

@property WireMailTools $mail

@property WireDateTime $datetime

## set()

@param string $key API variable name to set - should be valid PHP variable name.

@param object|mixed $value Value for the API variable.

@param bool $lock Whether to prevent this API variable from being overwritten in the future.

@return $this

@throws WireException When you try to set a previously locked API variable, a WireException will be thrown.

## remove()

Remove an API variable from the Fuel

@param $key

@return bool Returns true on success

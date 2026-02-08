# API Variables Map

Source: https://processwire.com/docs/start/variables/

## Summary

ProcessWire provides various API variables to every template file. These variables provide full access to all site content. This page provides an introduction on how to use them.API variables can be accessed in a few different ways. The most common way is as a variable. Here are a few different ways you might access the same $page API variable (as an example):$page the most common access as a variable.page() accessing as a function can be very convenient, when available.wire('page') This works anywhere, and with any version of ProcessWire.wire()->page This works anywhere too, and is more IDE friendly.$this->page This is how you might access it from within a Wire-derived class.$this->wire('page') A slightly more efficient way you can access from within a Wire-derived class.$this->wire()->page Like the above, but more IDE friendly.$pages->wire()->page API variables can also access all other API variables, by way of their wire() method. In this example, we are accessing the $page API variable from the $pages API variable. So if you have any one API variable, then you actually have them all.Accessing API variables as a function rather than a variable can be more convenient when the variable version may be out of scope, or if your IDE highlights API variables as undefined. So whenever we refer to an API variable, make note that access it however you'd like.This is just an introduction to some of ProcessWire's API variables. Once you are familiar with these, you'll want to use ProcessWire's full API reference instead.Some of ProcessWire’s most common API variables$pageThe $page variable is provided to every template, and it contains all the fields specific to the page being viewed. This includes…Learn more →$pagesWhile the $page variable holds the current page, the $pages variable is where you can get at all the other pages in your site. It…Learn more →$inputThe $input variable is your connection to GET, POST and COOKIE variables, URL segments, page (pagination) numbers, and more.Learn more →$sanitizerThe $sanitizer functions are provided to fill the most common data sanitization needs with sites developed in ProcessWire. Always…Learn more →$sessionThis API variable provides access to read/write of session variables, login and logout of users, redirects, and more.Learn more →$fields$fields is an API variable that contains all the custom page fields in your site. It provides the API functions available in the…Learn more →$userThe $user API variable is your connection to the current user viewing the page.Learn more →$logThe $log API variable enables you to create, manage and filter log entries. Log files are stored in /site/assets/logs/.Learn more →$templatesThe $templates API variable provides access to all of your site’s templates. Use the $templates API variable to retrieve, modify…Learn more →$configThe $config API variable contains all the settings specific to your site configuration. This includes URLs and paths, database…Learn more →

## Variables

- $page (../../core/wire/core/Page/index.md)
- $pages (../../core/wire/core/Pages/index.md)
- $modules (../../core/wire/core/Modules/index.md)
- $user (../../core/wire/core/User/index.md)
- $input (../../core/wire/core/WireInput/index.md)
- $sanitizer (../../core/wire/core/Sanitizer/index.md)
- $session (../../core/wire/core/Session/index.md)
- $log (../../core/wire/core/WireLog/index.md)
- $users (../../core/wire/core/Users/index.md)
- $permissions (../../core/wire/core/Permissions/index.md)
- $roles (../../core/wire/core/Roles/index.md)
- $cache (../../core/wire/core/WireCache/index.md)
- $datetime (../../core/wire/core/WireDateTime/index.md)
- $files (../../core/wire/core/WireFileTools/index.md)
- $mail (../../core/wire/core/WireMailTools/index.md)
- $config (../../core/wire/core/Config/index.md)
- $database (../../core/wire/core/WireDatabasePDO/index.md)
- $fields (../../core/wire/core/Fields/index.md)
- $templates (../../core/wire/core/Templates/index.md)
- $languages
- $classLoader (../../core/wire/core/WireClassLoader/index.md)
- $urls (../../core/wire/core/Paths/index.md)
- $adminTheme (../../core/wire/core/AdminTheme/index.md)
- $fieldgroups (../../core/wire/core/Fieldgroups/index.md)
- $fieldtypes (../../core/wire/core/Fieldtypes/index.md)
- $fuel (../../core/wire/core/Fuel/index.md)
- $hooks (../../core/wire/core/WireHooks/index.md)
- $notices (../../core/wire/core/Notices/index.md)
- $pagesVersions
- $process (../../core/wire/core/Process/index.md)
- $profiler (../../core/wire/core/WireProfilerInterface/index.md)
- $shutdown (../../core/wire/core/WireShutdown/index.md)
- $wire (../../core/wire/core/ProcessWire/index.md)

# FunctionsAPI

Source: `wire/core/FunctionsAPI.php`

ProcessWire functions API maps function names to common API variables

=
Provides an alternative to the API variables by providing functions of the same
name, with these benefits:

- They are always in scope whether inside a function or outside of it.
- They are self documenting with your IDE, unlike API $variables.
- They cannot be accidentally overwritten the way variables can be.
- They provider greater contrast between what are API-calls and variables.
- In some cases it makes for shorter API calls.
- Some of the functions provide arguments for useful shortcuts.

These functions always refer to the current ProcessWire instance, so are intended
primarily for front-end usage in template files (not for modules).

If these functions are not working for you, you can enable them by setting
`$config->useFunctionsAPI=true;` in your /site/config.php file.

Regardless of whether the Functions API is enabled or not, you can also access
any of these functions by prefixing the word `wire` to them and using the format
`wireFunction()` i.e. `wirePages()`, `wireUser()`, etc.
Or, if you do not

Methods:
Method: [pages()](method-pages.md)
Method: [page()](method-page.md)
Method: [pageId()](method-pageid.md)
Method: [config()](method-config.md)
Method: [modules()](method-modules.md)
Method: [user()](method-user.md)
Method: [users()](method-users.md)
Method: [session()](method-session.md)
Method: [fields()](method-fields.md)
Method: [templates()](method-templates.md)
Method: [database()](method-database.md)
Method: [permissions()](method-permissions.md)
Method: [roles()](method-roles.md)
Method: [sanitizer()](method-sanitizer.md)
Method: [datetime()](method-datetime.md)
Method: [files()](method-files.md)
Method: [cache()](method-cache.md)
Method: [languages()](method-languages.md)
Method: [input()](method-input.md)
Method: [urls()](method-urls.md)
Method: [paths()](method-paths.md)
Method: [region()](method-region.md)
Method: [setting()](method-setting.md)

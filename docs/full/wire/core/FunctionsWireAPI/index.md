# FunctionsWireAPI

Source: `wire/core/FunctionsWireAPI.php`

ProcessWire functions API maps function names to common API variables

Provides an alternative to the API variables by providing functions of the same
name, with these benefits:

- They are always in scope
- Makes life simpler in an IDE that recognizes phpdoc, as it can more easily
  recognize the types an return values.
- In some cases it makes for shorter API calls.

The primary drawback is that the function calls are not mapped to a specific
instance, so in a multi-instance environment it's possible these function calls
may not be referring to the correct ProcessWire instance. For this reason, we
think these functions are primarily useful for front-end/website usages, and
not as useful for back-end and module development.

Shorter versions of these functions (without the leading "wire") can be found in
FunctionsAPI.php file, which is used only if $config->useFunctionsAPI is true.
The functions in this file are always available regardless of that setting.

Methods:
Method: [_wirePagesAPI()](method-_wirepagesapi.md)
Method: [_wireDataAPI()](method-_wiredataapi.md)
Method: [wirePages()](method-wirepages.md)
Method: [wirePage()](method-wirepage.md)
Method: [wirePageId()](method-wirepageid.md)
Method: [wireConfig()](method-wireconfig.md)
Method: [wireModules()](method-wiremodules.md)
Method: [wireUser()](method-wireuser.md)
Method: [wireUsers()](method-wireusers.md)
Method: [wireSession()](method-wiresession.md)
Method: [wireFields()](method-wirefields.md)
Method: [wireTemplates()](method-wiretemplates.md)
Method: [wireDatabase()](method-wiredatabase.md)
Method: [wirePermissions()](method-wirepermissions.md)
Method: [wireRoles()](method-wireroles.md)
Method: [wireSanitizer()](method-wiresanitizer.md)
Method: [wireDatetime()](method-wiredatetime.md)
Method: [wireFiles()](method-wirefiles.md)
Method: [wireCache()](method-wirecache.md)
Method: [wireLanguages()](method-wirelanguages.md)
Method: [wireInput()](method-wireinput.md)
Method: [wireInputGet()](method-wireinputget.md)
Method: [wireInputPost()](method-wireinputpost.md)
Method: [wireInputCookie()](method-wireinputcookie.md)
Method: [wireLog()](method-wirelog.md)
Method: [wireProfiler()](method-wireprofiler.md)
Method: [wireUrls()](method-wireurls.md)
Method: [wirePaths()](method-wirepaths.md)
Method: [wireSetting()](method-wiresetting.md)
Method: [_wireFunctionsAPI()](method-_wirefunctionsapi.md)

# FileCompiler

Source: `wire/core/FileCompiler.php`

FileCompiler

ProcessWire 3.x, Copyright 2023 by Ryan Cramer
https://processwire.com

@todo determine whether we should make storage in dedicated table rather than using wire('cache').

@todo handle race conditions for multiple requests attempting to compile the same file(s).

Groups:
Group: [other](group-other.md)

Methods:
Method: [__construct()](method-__construct.md)
Method: [wired()](method-wired.md)
Method: [init()](method-init.md)
Method: [mkdir()](method-mkdir.md)
Method: [chmod()](method-chmod.md)
Method: [initTargetPath()](method-inittargetpath.md)
Method: [initRawPHP()](method-initrawphp.md)
Method: [allowCompile()](method-allowcompile.md)
Method: [___compile()](method-___compile.md)
Method: [___compileData()](method-___compiledata.md)
Method: [compileComments()](method-compilecomments.md)
Method: [compileIncludes()](method-compileincludes.md)
Method: [compileIncludesValidLineOpen()](method-compileincludesvalidlineopen.md)
Method: [compileIncludesFileMatchType()](method-compileincludesfilematchtype.md)
Method: [compileNamespace()](method-compilenamespace.md)
Method: [copyAllNewerFiles()](method-copyallnewerfiles.md)
Method: [getNumCacheFiles()](method-getnumcachefiles.md)
Method: [clearCache()](method-clearcache.md)
Method: [maintenance()](method-maintenance.md)
Method: [_maintenance()](method-_maintenance.md)
Method: [optionsToString()](method-optionstostring.md)
Method: [addExclusion()](method-addexclusion.md)
Method: [touch()](method-touch.md)

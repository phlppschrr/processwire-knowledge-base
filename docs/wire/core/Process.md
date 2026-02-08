# Process

Source: `wire/core/Process.php`

ProcessWire Process

Process is the base Module class for each part of ProcessWire's web admin.

Process modules are self contained applications that run in the ProcessWire admin.
Applicable only to Process modules that are using external output/view files.
See the `Module` interface for full details on these methods.
Please be sure to see the `Module` interface for full details on methods you can specify in a Process module.

ProcessWire 3.x, Copyright 2022 by Ryan Cramer
https://processwire.com

This file is licensed under the MIT license
https://processwire.com/about/license/mit/

## other

@method string|array execute()

@method string|array executeUnknown() Called when urlSegment matches no execute[Method], only if implemented.

@method Process headline(string $headline)

@method Process browserTitle(string $title)

@method Process breadcrumb(string $href, string $label)

@method void install()

@method void uninstall()

@method void upgrade($fromVersion, $toVersion)

@method void ready()

@method void setConfigData(array $data)

@method void executed($methodName) Hook called after a method has been executed in the Process

## __construct()

Construct

## ___execute()

Execute this Process and return the output. You may have any number of execute[name] methods, triggered by URL segments.

When any execute() method returns a string, it us used as the actual output.
When the method returns an associative array, it is considered an array of variables
to send to the output view layer. Returned array must not be empty, otherwise it cannot
be identified as an associative array.

This execute() method is called when no URL segments are present. You may have any
number of execute() methods, i.e. `executeFoo()` would be called for the URL `./foo/`
and `executeBarBaz()` would be called for the URL `./bar-baz/`.

@return string|array

## ___executed()

Hookable method automatically called after execute() method has finished.


@param string $method Name of method that was executed

## ___headline()

Set the current primary headline to appear in the admin interface

~~~~~
$this->headline("Hello World");
~~~~~

@param string $headline

@return $this

## ___browserTitle()

Set the current browser title tag

~~~~~
$this->browserTitle("Hello World");
~~~~~

@param string $title

@return $this

## ___breadcrumb()

Add a breadcrumb

~~~~~
$this->breadcrumb("../", "Widgets");
~~~~~

@param string $href URL of breadcrumb

@param string $label Label for breadcrumb

@return $this

## ___install()

Per the Module interface, Install the module

By default a permission equal to the name of the class is installed, unless overridden with
the 'permission' property in your module information array.

See the `Module` interface and the `install` method there for more details.

## ___uninstall()

Uninstall this Process

Note that the Modules class handles removal of any Permissions that the Process may have installed.

See the `Module` interface and the `uninstall` method there for more details.

## ___upgrade()

Called when module version changes

See the `Module` interface and the `upgrade` method there for more details.


@param int|string $fromVersion Previous version

@param int|string $toVersion New version

@throws WireException if upgrade fails

## ___installPage()

Install a dedicated page for this Process module and assign it this Process

To be called by Process module's ___install() method.


@param string $name Desired name of page, or omit (or blank) to use module name

@param Page|string|int|null Parent for the page, with one of the following:
	- name of parent, relative to admin root, i.e. "setup"
	- Page object of parent
	- path to parent
	- parent ID
	- Or omit and admin root is assumed

@param string $title Omit or blank to pull title from module information

@param string|Template Template to use for page (omit to assume 'admin')

@param array $extras Any extra properties to assign (like status)

@return Page Returns the page that was created

@throws WireException if page can't be created

## ___uninstallPage()

Uninstall (trash) dedicated pages for this Process module

If there is more than one page using this Process, it will trash them all.

To be called by the Process module's ___uninstall() method.


@return int Number of pages trashed

## setViewFile()

Set the file to use for the output view, if different from default.

- The default view file for the execute() method would be: ./views/execute.php
- The default view file for an executeFooBar() method would be: ./views/execute-foo-bar.php
- To specify your own view file independently of these defaults, use this method.


@param string $file File must be relative to the module's home directory.

@return $this

@throws WireException if file doesn't exist

## getViewFile()

If a view file has been set, this returns the full path to it.


@return string Blank if no view file set, full path and file if set.

## setViewVars()

Set a variable that will be passed to the output view.

You can also do this by having your execute() method(s) return an associative array of
variables to send to the view file.


@param string|array $key Property to set, or array of `[property => value]` to set (leaving 2nd argument as null)

@param mixed|null $value Value to set

@return $this

@throws WireException if given an invalid type for $key

## getViewVars()

Get all variables set for the output view


@return array associative

## getProcessPage()

Return the Page that this process lives on

@return Page|NullPage

## getAfterLoginUrl()

URL to redirect to after non-authenticated user is logged-in, or false if module does not support

When supported, module should gather any input GET vars and URL segments that it recognizes,
sanitize them, and return a URL for that request. ProcessLogin will redirect to the returned URL
after user has successfully authenticated.

If module does not support this, or only needs to support an integer 'id' GET var, then this
method can return false.

@param Page $page Requested page

@return bool|string

@sine 3.0.167

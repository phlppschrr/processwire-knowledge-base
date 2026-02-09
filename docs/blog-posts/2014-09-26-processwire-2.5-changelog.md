# ProcessWire 2.5 Changelog

Source: https://processwire.com/blog/posts/processwire-2.5-changelog/

## Sections


## ProcessWire 2.5 Changelog

26 September 2014 by Ryan Cramer [ 0 Comments](/blog/posts/processwire-2.5-changelog/#comments)


## What's new in ProcessWire 2.5?

[](http://www.avoine.fi) Special thanks to [Avoine](https://www.avoine.fi/) for being a major sponsor of ProcessWire 2.5!


### Featured Additions

- New PageTable Fieldtype provides a great replacement for repeaters.
- New PageLister module provides an amazing new admin search engine that can find any property from any page. See the new "Find" option on your Pages menu, which uses PageLister. The main search engine also utilizes PageLister, as does the Users list. Coming soon is PageListerPro, which enables you to not just find pages but modify/manipulate those pages and create your own custom PageListers.
- Add new admin theme: Admin Theme Reno, by Tom Reno (Renobird). To install go to: Modules > Core > Admin.
- Major enhancements to Modules screen with identification of new modules, filtering by module type, and installation from ZIP upload or remote URL.
- New WireMail module type and `wireMail()` function enables you to install 3rd party modules to handle sending of email.
- Major enhancements to selectors (see selectors and find pages section).
- Major updates to multi-language support (see multi-language support section).
- New site profiles, including a new responsive default site profile, multi-language profile and blank profile.
- Major updates to ProcessWire's installer, including the ability to select site profiles for installation.
- CKEditor has been added to the core as the new rich text editor (and TinyMCE has been dropped).


## **All Additions and Enhancements**

This list includes only major additions and enhancements. Minor additions/enhancements and bug fixes have been excluded as the list is plenty long as-is.


### Adding Pages

- Add support for adding pages in 1 step (from the admin). To enable, edit the template used by the parent page you want to support 1-step adding of children. In 'Family' tab, specify a single (1) template allowed for children. Then specify the 'Name Format' to use for children (per the instruction presented with the field). Save. Now pages will be added in 1-step.
- Updates to ProcessPageAdd: Made it so that there are separate Save and Publish buttons for when the option is there. Previously it just published pages that were publishable (i.e. pages with only a title field). Now it gives you the option. The other update here is that if you add a page with a name that already exists, it will automatically adjust the name to be unique (and give you a warning) rather than making you adjust the name yourself.


### Admin Theme and UI

- Numerous updates and optimizations to default admin theme.
- Default admin theme template and field dropdowns converted to ajax for faster load times (default admin theme only).
- Added new warning messages alerting superuser when their index.php or .htaccess files are out of date.
- Update ProcessPageList to have a trash button (appears after you click the 'move' button).
- Addition of Tom Reno's (Renobird) Reno Admin Theme!


### API Additions

- Add new `wireMail()` function for sending email. Add more new WireMail module type. Now you can install external modules like WireMailSmtp and WireMailSwiftMailer to delegate email sending to other servers.
- Add new `wireZipFile()` function (which creates a ZIP file) to accompany the existing `wireUnzipFile()` function.
- Update `wireSendFile()` function to support much larger file downloads.
- Convert any remaining unzip functions in the core to use ZipArchive (by way of the wireUnzipFile core function).
- Add `wirePopulateStringTags()` function. Given a string $str and values $vars, replace tags in the string with the values. See the function phpdoc definition for full details.
- Addition of `$cache` API variable that provides simple string caching functions similar to that provided by the MarkupCache module. This new $cache API variable uses the database rather than the file system and is now preferred over MarkupCache. Though MarkupCache will continue to remain in the core indefinitely (meaning, no need to convert existing usages of MarkupCache).
- Add WireDatabaseBackup class, which supports creating backups and restoring them. Can be accessed directly via `$database->backup()`.
- Added new `$page->hasChildren()` method, which works exactly the same as $page->numChildren() except that it returns only number of visible children. We've never quite liked the existing $page->numVisibleChildren or $page->numChildren(true) from the API perspective, so $page->hasChildren() is something we're happier with. Though the old methods/properties will continue to work too.
- Added new `$page->editUrl` (or $page->editURL if you prefer) property that returns the URL to the page editor for the current page.
- Update `$pages->save($page, $options)` to accept the 'adjustName' option. When true, the $pages->save() will adjust the 'name' property (if necessary) to ensure it is unique.
- Improved the logic of page corrupted detection. Now it takes into account which field was corrupted (by being set when output formatting was ON). If the corrupted field won't be saved as part of the $pages->save(), then it won't prevent the page from saving.
- New wireTemplateFile() function, providing a simpler alternative to using the TemplateFile class.
- New wireIncludeFile() function, providing a simpler and sometimes safer alternative to PHP's include() function. More details can be found towards the end of [Functions.php](https://github.com/ryancramerdesign/ProcessWire/blob/master/wire/core/Functions.php).


### Config

- Add a new `$config->ignoreTemplateFileRegex` option where you can specify a name format of any template files that should be ignored when scanning for new templates. The default is for it to ignore templates that begin with an underscore. This does not affect existing templates already in the system, only new ones that you may add. This config option can be overridden in /site/config.php like any other.
- Refactor of /wire/config.php for more comments and organization to make it easy to understand all the various config options that can be overridden in /site/config.php.
- New `$config->external` runtime variable is set to TRUE when ProcessWire is externally bootstrapped.
- New `$config->cli` runtime variable is set to TRUE when ProcessWire is running as a shell script/CLI mode.


### Drop TinyMCE/Add CKEditor

- Dropped TinyMCE from the core. If you'd like to continue using it, we are now maintaining it as a 3rd party module in the modules directory. Install in ProcessWire 2.5 by going to Modules > New > Install from directory. Type in "InputfieldTinyMCE" and install.
- Added CKEditor to the core (replacement for TinyMCE).


### Fields

- Add InputfieldSelector and FieldtypeSelector as new core modules. These enable you to build a page selection selector string interactively. Special thanks to Avoine for sponsoring this feature.
- Update to support fast removal of fields from the database. Previously it would iterate through every page using a field and delete the data individually. This is necessary for fields like FieldtypeFile, but not necessary for most. So it's been updated to perform the same task in a single query without loading all the pages, when it can. If it's dealing with less than 200 pages, or if the Fieldtype defines a deletePageField method, then it continues to use the old/slow method, as I don't think there is any way around that.
- New field export/import options available in Setup > Fields. Lets you copy and paste fields across sites.
- Checkbox fields now have no header when it isn't necessary.
- Update ProcessField so that it now has the option of remembering field settings across field type changes.


### Files and Images

- Major enhancements, optimizations and fixes to the image resizing methods thanks to Horst!
- Add support for extended pagefile paths. Extended pagefile paths limit the number of directories per level (in /site/assets/files/...) to under 2k per directory. To enable, set `$config->pagefileExtendedPaths = true;` in your /site/config.php file. This setting only affects pagefile paths for newly created pages from this point forward. Existing directories will remain as-is, to avoid breaking links. Please consider this feature as "beta" in ProcessWire 2.5.
- Add to support for image suffixes (thanks again to Horst).
- Add support for translating uploaded filenames so that non-ASCII chars get translated to ASCII equivlants rather than just underscores. Also adds support for translation of cyrillic characters in filenames to ASCII equivalents.
- Add memory check to ImageSizer so that it doesn't attept to resize images when there isn't adequate memory to do so. Thanks to Horst.
- Upgrades to file and image fields, including: 1) the ability to define whether the file/image field should behave as a single item or an array of items separately from the max files setting; 2) addition of a new "rendered string" option for output (i.e. you could have your image field output an <img> tag rather than a Pageimage object); 3) Support for "default" values--if a page's value is empty for your file/image field, you can specify a page it should inherit the value from instead; 4) The ability to specify any text formatters for the description field–previously you could only choose entity encoding–now you can choose any textformatter module; 5) image fields now have the option to specify a minimum width/height (in addition to the existing maximum width/height)–when specified, images not meeting the minimum will be refused at upload time.
- Add basic SVG support to Pageimage & InputfieldImage classes.
- New overwrite mode option for files and images.


### Modules

- Update Modules screen to support filtering by module category. Also, add a list of recently found modules, isolated from the other lists (on the New tab).
- Upgrade module dependencies to support version dependencies. Now your module's "requires" string or array may specify the version in addition to the module, i.e. `HelloWorld>=1.0.1`. You can also now use "PHP" or "ProcessWire" as version dependencies to specify that your module requires a particular version of PHP or ProcessWire. Example: `PHP>=5.4.0, ProcessWire>=2.4.1, HelloWorld>1.0.0`. Versions for modules may be specified as version strings (like shown here) or integers, but integers are preferable since they are how we specify module versions in getModuleInfo() functions. But when specifying a PHP or ProcessWire version, you should always use the 3 part version string (i.e. 2.4.1).
- Addition of new WireAction and PageAction base class for action modules. This will enable actions to be shared among Lister, Triggers and anything else that wants to perform actions upon pages in bulk quantities or upon events.
- The Module interface no longer requires init(). It also lets you use a YourModuleName.info.php or YourModuleName.info.json file instead of a `getModuleInfo()` method, if you prefer to keep your info separate from the module itself. See /wire/core/Module.php for more details about that. In addition, all modules now support the 'permission' property for their module info. When specified, the given permission name will be required of the user before PW will instantiate the module. Lastly, a new 'permissions' property was added to the module info. It is an associative array of `array('permission-name' => 'description')`. When given in module info (like getModuleInfo method), PW will automatically create and install the given permissions when the module is installed, and automatically remove them when the module is uninstalled.
- Modules now support icons with an `icon` property in their getModuleInfo() that refers to a font-awesome icon name (minus the "fa-" part). When specified the icon will be used in navigation and anywhere else that it makes sense.
- Update wire/core/Modules.php boot/load methods to better account for module dependencies in load order. Previously, module dependencies only affected order of init() calls for autoload modules (and of course, whether it would let you install a module). Now dependencies also affect `include()` and` __construct()` order. If you have a module that literally extends another (in the PHP OO sense), then use a ModuleName.info.json or ModuleName.info.php file rather than a getModuleInfo() method in your module, so that PW can discover the dependencies without actually loading the module file.
- Added a `created` date to the modules table.
- Added new and/or updated `$modules->getModuleInfo($moduleName)` and `$modules->getModuleInfoVerbose($moduleName)` API methods. Both return an array of module information. The "verbose" version includes additional information such as module summary text and more.
- Update ProcessModule to support installation by ZIP upload, or you can paste in a URL to a zip file (in addition to the existing installation from modules directory).


### Multi-Language Support

- Add multi-language support to file and image descriptions. This is enabled by default when using multi-language support. To disable it, see the new checkbox in your file/image field settings. *Special thanks to StarDesign / Beat Beer for sponsoring this addition.*
- Add `$page->setLanguageValue($language, $fieldName, $value);` and `$page->getLanguageValue($language, $fieldName);` to provide a common interface for setting/getting values in languages, beyond those already provided (which aren't all identical). This provides a new standardized way of getting/setting any language field value, regardless of the current user's language.
- Upgrades to Language translation system. Now it gives you a list of translatable files (separated by site and core) rather than asking you to figure it out yourself. It also comes with a Download ZIP button so you can easily copy all your translation files to somewhere else. In addition, translation files are now fully separated by site and core, enabling you to manage your language packs separately from your site's own translation files.
- Add new multi-language site profile to core.
- Rewrite of LanguageTabs module to increase performance.


### New Site Profiles

- New default/responsive site profile in beginner and intermediate editions
- New blank site profile
- New multi-language site profile (based on default site profile)
- New Iridium site profile (available separately)


### Process Modules

- Update base Process module to have dedicated methods for settings headline and breadcrumbs: `$this->headline('text');` and `$this->breadcrumb('url', 'text');` Also updated ProcessController to create automatic headline and breadcrumbs for execute[Function] when not supplied by the Process module.
- Process modules can now create pages automatically at installation (and remove them at uninstall) without the Process module needing to have any code for that process. Simplify specify a `page` property in your getModuleInfo, as specified here: /wire/core/Process.php
- Process modules can now [expose their navigation](/blog/posts/processwire-2.5-updates/#process-modules-can-now-feed-navigation-to-the-admin-theme) to the admin theme ([how-to](/blog/posts/processwire-2.5-updates/#how-to-expose-navigation-from-your-process-module)).


### Sanitizer

- Add new Sanitizer method: `$sanitizer->pagePathName($value);`
- Add new MarkupHTMLPurifier module to the core. Previously this was maintained as 3rd party module. It is now used by InputfieldCKEditor and can be used anywhere you'd like it. See $sanitizer->purify() method described below.
- Add new `$sanitizer->purify($html)` method that runs any markup you give it through HTML Purifier.
- Add new `$sanitizer->removeEntities($str)`, which is the opposite of `$sanitizer->entities()` in that it removes entities rather than adds them.
- Add new `$sanitizer->entities1($str)` method, which adds entity encoding to the string only if it hasn't already been added.


### Selectors and Finding Pages

- Add support to Pages/PageFinder for pagination of limit=1 queries. Previously if you called `$pages->find("some selector, limit=1");` the information used for pagination was not included unless limit was some number greater than 1. Now pagination info is included even with limit=1.
- Add several PageFinder optimizations and add support for @field.subfield grouping in selectors (database selectors only at present). This allows you to specify the same field twice in a selector and specify that it must match the same exact page reference. For instance, `categories.active=1, categories.featured=1` will match pages that at least one one category that's active=1 and at least one category that's featured=1. Whereas, `@categories.active=1, @categories.featured=1` will match pages that have at least one category that is BOTH featured AND active.
- Update to support subselectors in selector strings. These can be used on the 'id' property of any field that maps to a page. It can also be used on the 'parent' property. Subselectors are specified between [square brackets]. Example: `$pages->find("template=product, categories.id=[title%=electronics, active=1, include=hidden], include=all");`
- Update PageFinder to support matching of runtime values from API variables. For instance, you could have a selector string include something like `user.name=karen` and that would mean the selector would only match when the current user name was karen. This can be included in any call as part of a larger selector string sent to `$pages->find()` (or anything that uses DB-driven selectors with PageFinder).
- Update selector strings to support parsing of values from API variables (user, session, page). Now you can compose selectors like this (for example): `template=product, modified_users_id=[user.id], sort=-modified, limit=1`. The portion in [brackets] gets resolved to the actual value at runtime. So that selector sent to `$pages->find()` would return the last page that the current user modified. You may also use the session or page API variables in the same manner in selectors. Special thanks to Avoine for sponsoring this feature.
- Update PageFinder to support alternate count method to get page total. This new method can be faster in some queries and is worth trying if you've got a slow query. To use it, specify in your selector `$pages->find("get_total=count")`. You can also now disable get total counting with limit=n finds by specifying `get_total=0`. Note that total counting is already disabled if you don't specify a limit so it's not necessary to specify get_total=0 if you aren't applying any limit=n in the query.
- Update PageFinder to support OR-group selectors. To use, surround a selector string in parenthesis, within another selector string. Example: `template=product, in_stock>0, (featured_from<=today, featured_to>=today), (highlighted=1)` –that selector would find all "product" pages that were in stock, and were either fell in a featured date range, or had a highlighted checkbox checked. This is something you couldn't previously do with selectors. You can also name your OR conditions if you want to have different combinations of them by specifying `foo=(selector), bar=(another selector), foo=(yet another selector), bar=(and another)`, replacing "foo" and "bar" with names of your choice (this is not a field name, just a means of grouping). In that selector, at least one of the "foo" named selectors would have to match, and at least one of the "bar" named selectors would have to match.


### Session

- Added 2 new hooks to the Session class for login/logout success.
- `$session->get()` and `$session->set()` now optionally support namespaces. This isolates any of the session variables get or set to a namespace that you define. The namespace can also be any ProcessWire object. Usage is: `$session->set($namespace, $property, $value);` and `$session->get($namespace, $property);`
- Updates to SessionCSRF to prevent "this request appears to be forged" message from appearing when it doesn't need to.


### Templates

- Update in Setup > Templates > [edit template]. When you click the trash icon for a field, it now marks it for deletion with a strikethrough, rather than removing it from the list. This makes it easier to notice mistakenly removed fields.
- Addition of a 'modified' date to templates, which reflects the last modified date of the template or its file.
- New system toggles available on the "Advanced" tab of the Template editor screen.
- New template export/import options available in Setup > Templates. Lets you copy and paste templates and fieldgroups across sites.
- Add new "Files" tab on the template edit screen which allows you to override and/or add to `$config->prependTemplateFile` and `$config->appendTemplateFile` settings.


### Updates (Other)

- Boot optimizations for faster execution of ProcessWire requests.
- The "user-admin" permission has now been made independent in that it requires no other permissions (on templates or otherwise) in order to use it.
- Update the download method in WireHttp to use CURL when allow_url_fopen is disabled in PHP.

*ProcessWire 2.5 also includes numerous bug fixes, optimizations and various minor enhancements not mentioned above.*

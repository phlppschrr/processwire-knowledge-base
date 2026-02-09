# ProcessWire 3 master and changelog

Source: https://processwire.com/blog/posts/pw3-changelog/

## Sections


## ProcessWire 3 master and changelog

30 September 2016 by Ryan Cramer [ 6 Comments](/blog/posts/pw3-changelog/#comments)


## What’s new in ProcessWire 3?

Last week we called it a soft launch, but this week we'll say ProcessWire 3 is now released and considered our new master, version 3.0.35. This post is a changelog of sorts, where we will cover all that's new in ProcessWire 3!


### System upgrades

**Namespaces** Technically, one of the biggest difference between 2.x and 3.x is that 3.x uses PHP namespaces. [More](/blog/posts/processwire-2.6.20-and-surprise-processwire-3.0-alpha-1/#what-benefits-will-using-namespaces-bring)

**Support for compiled modules and template files** In order to ease the transition to namespaces for modules and template files, ProcessWire is able to automatically compile non-namespaces modules or template files into a format that makes them recognize namespaces. [More](/blog/posts/processwire-3.0-alpha-2-and-2.6.22-rc1/#processwire-3.0-alpha-2)

**Front-end editing** Built-in, front-end editing capabilities come with ProcessWire 3.x, opening a whole new path for page edits. [More](/api/modules/front-end-editing/)

**Field rendering template files** ProcessWire 3.x also adds support for a new kind of template file. You can now have template files for any field in ProcessWire, and those template files can be used to render output for any given field. Read more [here](/blog/posts/more-repeaters-repeater-matrix-and-new-field-rendering/#processwire-3.0.5-introduces-field-rendering-with-template-files) and [here](/blog/posts/processwire-3.0.7-expands-field-rendering-page-path-history-and-more/#field-rendering-with-template-files).

**Multi-instance support** ProcessWire 3.x lets you boot multiple copies of ProcessWire at the same time, which opens new possibilities for sharing data among multiple installations. [How to use multi-instance](/blog/posts/multi-instance-pw3/)


### New API variables

**[$files](/api/ref/files/) ** Provides several great new API methods for files and directories, including rendering, manipulation, zipping/unzipping, and compilation.

**[$datetime](/api/ref/datetime/) ** Provides several useful API methods for working with dates and times.

**[$mail](/api/ref/mail/) ** A new API variable that serves as an interface to WireMail.

**[$classLoader](/api/ref/class-loader/) ** Enables you to connect PHP namespaces with file system paths for autoloading purposes.


### New $page and $pages API methods

**New $pages->findOne() method** ProcessWire 3.x adds a new [findOne()](../../../full/wire/core/Pages/method-findone.md) method that behaves as kind of a hybrid between the $pages->find() and $pages->get() methods. [More](/blog/posts/merry-christmas-heres-processwire-3.0.3-and-2.7.3-and-some-more/#new-pages-gt-findone-selector-api-method)

**New $pages->getPath() and $pages->getByPath() methods** The [getPath()](../../../full/wire/core/Pages/method-getpath.md) method enables you to get the path to a page without actually loading it, making it a nice optimization for several instances. And the [getByPath()](../../../full/wire/core/Pages/method-getbypath.md) method enables you to retrieve a Page object when you only know the path. Of course you can already do that with any page finding method that accepts a selector, but the difference is that getByPath() is very task focused and can do it a lot more quickly, and with a few extras as well. [More](/blog/posts/processwire-3.0.6-brings-pages-upgrades-and-link-abstraction/#new-optimized-pages-api-methods)

**New $pages->touch() method** The [touch()](../../../full/wire/core/Pages/method-___touch.md) method works very much like the unix "touch" command. Given a $page, it quickly updates that page's modification time (in the database) to now. [More](/blog/posts/processwire-3.0.6-brings-pages-upgrades-and-link-abstraction/#pages-gt-touch)

**New $pages->findMany() method** The [findMany()](../../../full/wire/core/Pages/method-findmany.md) method enables you to find thousands upon thousands of pages at once, and even iterate them without running out of memory! [More](/blog/posts/find-and-iterate-many-pages-at-once/)

**New $page->index() API method** This new [index()](../../../full/wire/core/Page/method-index.md) method (also accessible as a property) tells you the position of any page relative to its siblings. [More](/blog/posts/pw-3.0.24/#new-page-gt-index-api-method)

**API-side loading, sorting and filtering via $page methods** Multi-value fields (where supported) can now be filtered or sorted before they are loaded simply by calling them as a method on $page rather than as a property. [More](/blog/posts/fieldtype-pagination/#api-side-loading-sorting-and-filtering)


### Field upgrades

**Major image field upgrades** Image fields got a major upgrade in 3.x thanks to a redesign by Renobird and development help from LostKobrakai. The design was originally introduced in [this post](/blog/posts/a-preview-of-coming-attractions-to-processwires-image-tools/) by Renobird, and the results now appear in the current 3.x version with more info and screencasts [here](/blog/posts/major-images-field-upgrade/) and [here](/blog/posts/more-images-upgrades/).

**New link abstraction features** Full page link abstraction is now built into the core Textarea field, making it possible to move or rename linked pages and have any internal links to them get updated automatically. [More](/blog/posts/processwire-3.0.6-brings-pages-upgrades-and-link-abstraction/#new-link-abstraction-features)

**Repeater upgrades** Repeaters have a ton of upgrades in 3.x, making them far more useful and efficient than before. Read more [here](/blog/posts/processwire-3.0.4-repeaters-revisited-preview-of-profields-matrix/#major-upgrades-to-repeater-fields) and [here](/blog/posts/more-repeaters-repeater-matrix-and-new-field-rendering/#repeater-upgrades-continued-in-pw-3.0.5) and [here](/blog/posts/pw-3.0.23/#new-option-for-repeaters).

**Repeater Matrix support** In combination with some of the Repeater upgrades mentioned above, 3.x also supports the [ProFields Repeater Matrix](/api/modules/profields/repeater-matrix/) Fieldtype, which is opens up a whole new landscape of editing possibilities. [More](/blog/posts/processwire-3.0.4-repeaters-revisited-preview-of-profields-matrix/#new-profields-repeater-matrix-field)

**Enhanced password fields** Passwords fields received major upgrades in UI and configurable security options. [More](/blog/posts/upgrades-optimizations-pw-3.0.22/#major-enhancements-to-our-password-field)

**Paginated Fieldtypes** New support for paginated fieldtypes is a massive upgrade for scalability of multi-value fields. The [ProFields Table](/api/modules/profields/table/) Fieldtype is the first example to support this. [More](/blog/posts/fieldtype-pagination/)

**Text lengths and runtime character/word counters** Support for minimum length requirements was added to text-based types. Support for maximum length was also added on Textarea types. In addition, you now have the option of showing a runtime character (or word) counter with text types. [More](/blog/posts/pw-3.0.32/#core-updates-in-this-version)


### Page tree and editor upgrades

**Smarter and faster page tree** The page tree now remembers where you left it. This also enables it to load the page list much faster than before. [More](/blog/posts/processwire-3.0.8-brings-smarter-faster-page-tree/#page-tree-upgrades)

**New page view options** You now have a lot more options when it comes to viewing a page on the front-end. Our "view" link is now a drop-down letting you choose to view it in the same window, in a modal, in a panel or in a new window. [More](/blog/posts/pw-3.0.15/#new-page-view-options)

**Panel support** In addition to the common modal windows that you see in ProcessWire, we now support [panels](/blog/posts/pw-3.0.15/#processwire-panels) and are using them in our [page list quick tree](/blog/posts/pw-3.0.15/#new-quick-tree-page-list-panel) and the new [debug tools panel](/blog/posts/pw-3.0.15/#new-debug-tools-panel). Panels are also an option when [viewing a page](/blog/posts/pw-3.0.15/#new-page-view-options).

**Image resizing upgrades** Thanks to the work of Horst, we added support for new *ImageSizerEngine* modules and bundled the new *ImageMagick* resizing engine as a faster alternative to the built in GD resizing engine. [More](/blog/posts/processwire-3.0.10-expands-image-resize-options/)

**Dropdown button actions** Now our submit buttons come with dropdown actions, which add convenience and save time. More [here](/blog/posts/processwire-3.0.9-adds-new-long-click-and-save-actions/#new-page-edit-save-actions) and [here](/blog/posts/processwire-3.0.13-selector-upgrades-and-new-form-builder-version/#enhancements-to-dropdown-submit-buttons), as well as a new "Save and edit next" action [here](/blog/posts/pw-3.0.24/#new-save-and-edit-next-button-action-in-page-editor).


### Performance and optimization

**Improvements to sub-selectors** The speed at which sub-selectors operate has now been [greatly improved](/blog/posts/processwire-3.0.6-brings-pages-upgrades-and-link-abstraction/#speed-improvements). Basically, they are now hundreds of times faster than before. 3.x also now supports [nested sub-selectors](/blog/posts/processwire-3.0.6-brings-pages-upgrades-and-link-abstraction/#support-for-nested-sub-selectors).

**Exponentially faster forms** With a few bottlenecks removed, our editor forms (InputfieldForm) are now exponentially faster! [More](/blog/posts/upgrades-optimizations-pw-3.0.22/#major-optimizations-to-inputfield-forms)

**Major performance upgrades to Page traversal methods** The Page traversal methods like $page->next(), $page->nextAll(), $page->nextUntil(), and all the equivalent prev() versions, received major upgrades making them not only simpler to use but a whole lot faster! [More](/blog/posts/pw-3.0.24/#upgrades-to-page-traversal-methods)

**Enhanced page finding selectors** Page finding selectors got a whole lot more powerful with support for `a.b.c` and `a.b.c.d` (and so on) type selectors! [More](/blog/posts/pw-3.0.25/)

**Control over when to use sessions** Now you have the ability to implement a function that controls when sessions are allowed using your own provided logic. [More](/blog/posts/multi-instance-pw3/#more-session-control)


### Multi-language upgrades

**Language pack CSV import/export ** You can now export an entire language pack (group of translation files) to a single CSV file. You can also import translations from the CSV file. [More](/blog/posts/pw-3.0.23/#language-translation-file-csv-export-import)

**Extended page names** We added support for extended page names enable you to have URLs containing almost any UTF-8 characters. This is great for multi-language sites too. [More](/blog/posts/hello-%E5%81%A5%E5%BA%B7%E9%95%B7%E5%A3%BD%C2%B7%E7%B9%81%E6%A6%AE%E6%98%8C%E7%9B%9B/)

**Multi-language page history** The PagePathHistory module now supports multi-language URLs. [More](/blog/posts/processwire-3.0.7-expands-field-rendering-page-path-history-and-more/#page-path-history-now-multi-language)

**Multi-language template toggle** Now you have the ability to toggle multi-language features on/off on a per-template basis. [More](/blog/posts/processwire-3.0.21-and-2.8.21/#multi-language-toggle)

**New phrase search for language translation** When you need to translate some text, but don't know what file it appears in, this new search engine makes life a lot easier! [More](/blog/posts/pw-3.0.23/#new-phrase-search-for-language-translation)

**Change all language tabs at once** Now you can long-click on any language tab (in the page editor) and it will change all fields to focus that language tab. [More](/blog/posts/pw-3.0.23/#new-long-click-support-for-language-tabs)

**Multi-language placeholder attributes** Text fields now support multiple languages when it comes to placeholder values.

**Translation dropdown submit buttons** Now when translating files, you can choose to save and exit, save and edit next, or save and continue editing (as before).


### Composer and Packagist support

**ProcessWire 3 and Composer** PW3 now comes with a default composer.json file and a custom PSR-4 compliant autoloader. [More](/blog/posts/composer-google-calendars-and-processwire/)

**ProcessWire now on Packagist** ProcessWire can now be installed with Composer via the Packagist service. [More](/blog/posts/hello-pw3/#processwire-3.x-now-on-packagist)

**Modules can now use Composer** In addition to other libraries you might install with Composer, ProcessWire Modules can now be installed and maintained via Composer, where supported. [More](/blog/posts/composer-google-calendars-and-processwire/)


### Code hosting upgrades

**New GitHub repositories** The ProcessWire code is now hosted in a new more official GitHub repository called [processwire/processwire](https://github.com/processwire/processwire) (changed from [ryancramerdesign/ProcessWire](https://github.com/ryancramerdesign/ProcessWire)). We also have the [processwire-legacy](https://github.com/processwire/processwire-legacy) repository which hosts ProcessWire 2.8. [More](/blog/posts/hello-pw3/#new-github-repositories)

**Improved issue and request management** We now have an issue and request management team, lead by Francesco Schwarz ([@isellsoap](https://github.com/isellsoap)), new repositories for managing [issues](https://github.com/processwire/processwire-issues) and [requests](https://github.com/processwire/processwire-requests), new issue templates, and more. [More](/blog/posts/hello-pw3/#new-github-repositories)


### And more…

- Nice improvements to the ~= text finding operator. [More](/blog/posts/merry-christmas-heres-processwire-3.0.3-and-2.7.3-and-some-more/#improvements-to-the-operator-in-page-finding-operations)
- Install support for utf8mb4 charset and InnoDB engine (database). [More](/blog/posts/pw-3.0.15/#support-for-utf8mb4-and-innodb)
- New long-click modal actions. [More](/blog/posts/processwire-3.0.9-adds-new-long-click-and-save-actions/#new-long-click-modal-actions%C2%A0)
- You can now use selector arrays in addition to selector strings. [More](/blog/posts/processwire-3.0.13-selector-upgrades-and-new-form-builder-version/#selector-engine-array-support)
- New options for required fields. [More](/blog/posts/processwire-3.0.14-updates-file-compiler-fields-and-more/#required-fields-in-processwire)
- New 3.x comprehensive API reference documentation. [More](/blog/posts/processwire-3.x-api-reference/)
- Some useful $config improvements. [More](/blog/posts/hello-pw3/#config-improvements)
- Hundreds of big fixes and optimizations!


### What about ProcessWire 2.8?

ProcessWire version 2.8, hosted in our new [processwire-legacy](https://github.com/processwire/processwire-legacy) repository, is by-and-large exactly the same as ProcessWire 3 except for the following exclusions:

- namespaces
- multi-instance*
- Composer support*
- Packagist

*May still work but we aren't officially supporting it in 2.8. If you need any of the above items we recommend sticking with ProcessWire 3.


### ProcessWire Upgrade module updated for PW3

With ProcessWire 3 now out, the [ProcessWire Upgrade](http://modules.processwire.com/modules/process-wire-upgrade/) module has also received a version upgrade that supports upgrading to ProcessWire 3 (or ProcessWire 2.8). We've used this for a few of our PW3 site upgrades, including the [demo.processwire.com](http://demo.processwire.com) site, and it works quite well.

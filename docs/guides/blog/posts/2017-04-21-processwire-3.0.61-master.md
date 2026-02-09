# ProcessWire 3.0.61 master

Source: https://processwire.com/blog/posts/processwire-3.0.61-master/

## Sections


## New ProcessWire 3.x master version

21 April 2017 by Ryan Cramer [ 3 Comments](/blog/posts/processwire-3.0.61-master/#comments)


## ProcessWire 3.0.61

This week we've merged the dev branch to the master branch for ProcessWire version 3.0.61 master. This replaces the existing master version 3.0.42. What's the difference between 3.0.42 and 3.0.61? Quite a lot! In fact, we might usually call this a major version and just name it ProcessWire 3.1, but we're saving that version number for when we get at least the new Regular site profile included (and perhaps the new admin theme), after Uikit 3.0 is out of beta. In this post, we'll cover some of what's new with ProcessWire 3.0.61 relative to the previous master version…


### API methods

- Add new [$pages->findIDs()](../../../full/wire/core/Pages/method-findids.md) method. Like $pages->find() except returns array of IDs rather than Page objects. This is a faster method to use when you only need to know the matching page IDs.
- Add new [$pages->sort()](../../../full/wire/core/Pages/method-___sort.md) method.
- Add new [$pages->insertBefore()](../../../full/wire/core/Pages/method-___insertbefore.md) and [$pages->insertAfter()](../../../full/wire/core/Pages/method-___insertafter.md) methods.
- Update [$page->editUrl(true)](../../../full/wire/core/Page/method-editurl.md) method to force return of edit URL with scheme and hostname.
- The beginnings of page import/export functions are included, but currently a work in progress.
- Add an [Inputfield::val()](../../../full/wire/core/Inputfield/method-val.md) method for consistency with jQuery. This method is a shortcut for getting or setting the value attribute of Inputfield objects
- Add [$languages->setLocale()](../../../full/wire/modules/LanguageSupport/Languages/method-setlocale.md) and [$languages->getLocale()](../../../full/wire/modules/LanguageSupport/Languages/method-getlocale.md) methods.
- Add new [Inputfield::hasField](../../../full/wire/core/Inputfield/index.md) property.
- Expand upon the [$page->url()](../../../full/wire/core/Page/method-url.md) method to include an $options argument that adds many new capabilities.
- Improvements to the region() aka wireRegion() function calls.
- Improvements to the [$pages->findMany()](../../../full/wire/core/Pages/method-findmany.md) method.
- Add new hook: [Inputfield::renderReadyHook ](../../../full/wire/core/Inputfield/method-___renderreadyhook.md)– called when before an Inputfield is rendered.


### Selectors

- Add support for negative "limit" and "start" values in selectors, where negative values reference the end of the set rather than the beginning.
- Add support for "eq=n" (or alias "index=n") selectors (both WireArray and PageFinder) for pulling a specific n'th item, can also specify "first" or "last" for "n".
- Improved "custom (field=value)" selector support added to InputfieldSelector module.
- Major code refactoring and optimization in the Selectors class.


### Admin and UI

- Add support for Pages > Tree navigation: drill down through the page tree within the top navigation dropdowns. This works in AdminThemeDefault and AdminThemeUikit but not in AdminThemeReno (which just shows the first level, per its nav setup).
- Update CKEditor version to 4.6.2 – this is a relatively major upgrade that changes the default look/feel of the CKEditor theme.
- Add the Vex library for nicer looking Javascript alert and confirm boxes, which we use to confirm "clone" and "delete all" operations in repeaters, and will use elsewhere.
- Add a “Publish and Add Another” option to the Submit button options in the “page add” process. Applies when selected page template contains only a title.
- Added drag/drop protection so that if you accidentally drag/drop a file outside of the specified drop zone, it gets ignored, rather than loading the file in the browser.
- Updated admin themes to use current logo (via Pete).
- Upgrades to the "details" and "input" configuration screens of Page fields.
- Improvements to the usability of our dropdown submit buttons (like in the page editor).
- Add new Admin Theme Framework support, which is currently being developed independently via the AdminThemeUikit module.
- Improvements to touch device support.


### Repeaters

- Add support for repeater depth.
- Add new repeater item “clone” feature.
- Add support for maximum items.
- Add support for minimum items.
- Add double-click trash icon to “delete all” feature.
- Add support for “accordion mode” where only one repeater item is open at a time.
- Add open all/close all function. It's kind of hidden–to use it, double click the "on/off" toggle icon that appears next to the trash icon.
- All of the above also apply to ProFields [Repeater Matrix](/api/modules/profields/repeater-matrix/).


### Optimizations

- Make each page's parent page lazy loading for Page objects, so that it doesn't load the parent Page until a [$page->parent()](../../../full/wire/core/Page/method-parent.md) call is requested.
- Upgrades and optimizations to the FileCompiler class.
- Optimization to reduce overhead during Page saving operations.
- Numerous optimizations to our hooks system.


### Other

- Add support for markup regions, a simple new template file output strategy that bridges the gap between direct and delayed output. This is perhaps one of the biggest additions to this new master version, and we've got a documentation page in the works, coming next week!
- Updates to support multiple template selections for Page fields.
- Add option to exclude files from FileCompiler directly via include() and require() function calls. See [3.0.43 blog post](/blog/posts/processwire-3.0.43-core-updates/) for details.
- Numerous core modules updated to support customization by AdminTheme modules.
- Improved support for language locale settings on front-end.
- Add support for load-time filtering of Page fields (FieldtypePage).
- Add detection and warning for problematic locale settings (appears on superuser login).
- Updated HTML Purifier to latest version 4.9.2.
- Updated Font Awesome icons to latest version 4.7.
- Numerous code documentation improvements.
- Hundreds of bug fixes and other minor adjustments.
- Pull requests from @LostKobrakai, @adrianbj, @gmclelland, @rolandtoth, @owzim, @notanotherdotcom, @derixithy, @jofalk, and others. Thanks for your contributions!

As you can see there is quite a lot in ProcessWire 3.0.61! We hope that you enjoy using this new version and please let us know how it works for you. Thanks for reading, hope you have a great weekend, and hope to see you at the next issue of [ProcessWire Weekly](http://weekly.pw) soon.

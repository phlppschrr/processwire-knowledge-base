# Page Edit Lock Fields module

Source: https://processwire.com/blog/posts/page-edit-lock-fields/

## Sections


## Page Edit Lock Fields module

10 November 2023 by Ryan Cramer [ 0 Comments](/blog/posts/page-edit-lock-fields/#comments)

A new open source module that enables you to lock page fields or properties from editing on a page-by-page basis.

ProcessWire comes with a page-lock feature, where you can lock an entire page from being edited. The Page Edit Lock Fields module expands upon that feature by making it more granular, providing the ability to lock fields individually on any page.

While ProcessWire also provides the ability to lock fields independent of pages, this module enables you to lock fields directly on pages and in the page editor, when and where you are most likely to want to do so.

After clicking and holding (long-click) the "Title" label, this dialog box pops up asking if we want to lock the field. The same action works to unlock a field.


### Table of contents


## About Page Edit Lock Fields


### Solving the biggest downsides of page and field locks

The core page-lock feature locks the entire page, making it completely uneditable. That may be exactly what you want in some cases. But if it’s not, then you likely will just skip using page-lock completely, and miss its benefits.

The core also provides the ability to lock a field across all pages (or all pages using a particular template) using the field visibility settings. Again, this may also be what you want in some cases, but what it adds in field level granularity, it lacks in page level granularity.

The Page Edit Lock Fields module removes these downsides, enabling you to lock any field in the page individually. So you could (for instance) lock the Title field but leave the Body field editable, on just a specific page.

The module also goes beyond fields and enables you to lock native page properties such as the name, template, parent and status properties of the page. You can also lock the “Delete/trash page” option. These options are not available with page or field locks in the core.


### Why would you want to lock a page, or fields on a page?

There are lots of potential reasons and use cases, but the original thinking was to prevent changes in cases where it might break something in the site or have some other kind of negative consequence. Selectors query fields and properties of a page, and if an expected value is not present, something may break.

Sometimes we need to be able to count on things having a particular value, and if that value changes, then things break. Being able to lock down a page gives us greater assurance that we can count on it being the way we left it.

For instance, you may have code in your template files that depends on a page having a particular name, template or parent. If another user changes one of them sometime in the future, the code logic fails. An API call such as `$pages->get('/foo/');` or `$page->child('name=foo');` no longer works if the page name is changed.

To future-proof such calls, developers often use IDs instead of paths or names in queries like this, i.e. `$pages->get(1234);` The problem is that using IDs like this reduces code clarity and readability. Wouldn’t it be nice if we could use the name instead, and know that it wouldn’t be changed?

Another use case is that locks serve as a way to designate content as final. For example, final content might be content that would have to be approved by someone before being modified.

Locking a field is also a good way to prevent both intentional and accidental changes to it.


### What you can and can’t lock

This module lets you lock any fields on a page, plus a few native properties found on the “Settings” tab of the page editor. These native properties include: Name, Template, Parent and Status.

For fields that have multiple inputs (such as Repeater, File/Image, Table, Combo) this module lets you lock the entire field as a whole. But it does not enable you to individually lock specific subfields within a multi-input field.

You cannot lock entire fieldsets (InputfieldFieldset) or tabs (InputfieldFieldsetTab), but you can lock fields individually within them.


## Installation and configuration

This module is installed like any other module. You place its files in `/site/modules/PageEditLockFields/`, then go to Modules > Refresh in your admin, then click “Install” for this module. Following that you can configure and start using the module.


### Configuration

Once installed, you will be on the module configuration screen. From here you can specify how you want it to work and who you want to be able to lock and unlock fields on a page. Following are descriptions of the configurable options on this screen:


### 1. Toggles

These are features that you can turn on/off. I recommend starting with the default settings that the module provides. Then adjust them as you find necessary.

**Enable long-click of field label/header to toggle lock/unlock.** This provides a convenient and fast way to lock or unlock fields on-the-fly, simply by clicking and holding the header for the field until a dialog box pops up asking if you want to lock (or unlock) the field. Technically this feature is not required since you can still lock or unlock fields from the Settings tab. But I recommend keeping it enabled unless you find it conflicts with something else.

**Show a note in locked fields explaining that they are locked.** This makes it immediately obvious to users that a field is not editable. Without it, users may not understand why they can't edit the field. Though see the next toggle, which provides an alternative to this.

**Pop up an alert if user clicks a locked field, to let them know it's locked.** This is an alternative to the previous toggle, though both can be used. When a user clicks in a locked field (presumably because they want to edit it), it will pop up an alert box letting them know it's locked.

**Always collapse/minimize locked fields?** When enabled, locking a field will also collapse/close/minimize it. In this state the user must click the field header to open it. This is a good option to use if you want to reduce the visibility of locked fields.


### 2. Users that can lock/unlock

By default, users with “page-lock” permission on a page are allowed to lock and unlock fields. But it may be that you want to limit this ability to just a specifc superuser or two, such as the site developer. If that’s the case, select the users you want to limit to on the module configuration screen.


### 3. Render inputs for fields when locked?

When a field is locked, ProcessWire just renders its value rather than its inputs. Usually this is ideal. But in some cases, you may still want the field's inputs to be rendered, even if the locked status prevents them from being saved. One case would be if the value-only output isn't adequate for showing everything you need. Another case would be if you are using show-if or required-if field dependencies that depend on inputs being present to compare against. Only use this setting if you absolutely need it, as rendering the inputs for a locked field is likely to create confusion. As a result, if you use this, you'll definitely want to enable the locked note and/or pop-up alerts in the Toggles field mentioned earlier.


### 4. Current field locks

The module configuration screen also gives you a summary of all locks currently on the site in case you ever need help tracking down where they are. Initially this list will be empty, since there are no locks at installation time.


## Usage notes


### Locked field checkboxes on Settings tab of the page editor

Once up and running in the page editor, the “Settings” tab will now have a “Locked fields” setting where you can check boxes for any fields/properties that you want to lock. Check the box to lock, or uncheck to unlock. This is an alternative to the long-click lock/unlock action. Your lock settings apply once the page is saved.


### Long click to lock or unlock

As a convenience, you can also lock/unlock fields by clicking a field header and holding your mouse button down until a confirmation dialog box comes up. It will confirm that you want to lock (or unlock) the field. This convenient feature is just for desktop browser environments and it can optionally be disabled in the module settings.


### Status and parent locks

If you lock the page’s status, then it also prevents the status from being changed in the page-list inline actions. Likewise, If you lock the page’s parent, then it also prevents the page from being moved to a different parent in the page-list.


### Editor environments

Field locks are for the admin environment and they do not affect your ability to modify fields from the API. Should you have another module installed that allows edits to pages, please note that this module will not apply. When it comes to front-end editing, this module also works with the core PageFrontEdit module in that it prevents edits to fields that are locked. However, you must still be in the admin page editor to lock/unlock fields, or see alerts/labels about locked fields.


### Field dependencies

Locked fields can affect the behavior of any field dependencies watching locked fields. These field dependencies include the "show-if" and "require-if" settings configurable with each Inputfield. Since locked fields no longer have an input present, dependencies checking for the presence or non-presence of a value will not function. The same is true of locked fields outside of this module. But this module provides a way around it. You can use the “Render inputs for fields when locked” setting in the module configuration to force the locked field involved in the dependency to render its inputs, rather than just its value. Following that, it should again work with field dependencies.


### Cloning and deleting pages

When you clone a page, its field locks are also cloned. And when you delete a page, the relevant entries in the locks table will also be deleted. But if you just trash a page, the locks will remain, as the page is still in a state where it can be restored.


### Preventing URL changes

If you want to prevent a page’s url/path from ever changing due to edits in the admin, lock its name and parent, but also lock the same properties from its parents as well.


### Access control

While this module may make a field non-editable, it's also worth mentioning that this is not a security related module, and using locked fields is not suggested as a replacement for proper access control settings.


## API

It is not necessary to use the module’s API, as all features are provided interactively. However, should you want it, here is its public API. The following examples assume you have a copy of the module populated to a `$pelf` variable like this:

```
$pelf = $modules->get('PageEditLockFields');
```


### Get all locks for a Page

Returns array of locked field names. The $page can be a Page object or Page ID integer.

```
$locks = $pelf->getLocks($page);
```


### Get all locks across all pages

Returns array of arrays with page lock info. Each array contains the properties: "id" (string), "path" (string) and "fields" (array of field names).

```
$locks = $pelf->getAllLocks();
foreach($locks as $pageId => $lock) {
  $fieldNames = implode(', ', $lock['fields']);
  echo "<li>Page $lock[path] fields: $fieldNames</li>";
}
```


### Check if a field is locked

This example checks if the 'title' field is locked on $page. The $page can be a Page object or Page ID integer, while the 'title' can be a Field object, name, or ID.

```
if($pelf->isLocked($page, 'title')) {
  // the "title" field on $page is locked
}
```


### Lock a field on a page

The following example locks the title field on $page. The $page can be a Page object or Page ID integer, while the 'title' can be a Field object, name, or ID.

```
$pelf->addLock($page, 'title');
```


### Unlock a field on a page

This example removes the lock for the 'title' field on $page. The $page can be a Page object or Page ID integer, while the 'title' can be a Field object, name, or ID.

```
$pelf->removeLock($page, 'title');
```


### Add multiple field locks at once

Here we add locks for the title, name and status fields on $page. The $page can be a Page object or Page ID integer.

```
$pelf->addLocks($page, [ 'title', 'name', 'status' ]);
```


### Remove all locks for a given page

This removes all field locks for a $page, regardless of field or property. The $page can be a Page object or Page ID integer.

```
$pelf->removeAllLocksForPage($page);
```


### Remove all locks for a given field

This removes all field locks for a $field, regardless of page. The $field can be a field ID, name or Field object.

```
$pelf->removeAllLocksForField($field);
```


## Download

The Page Edit Lock Fields module is available for download from the ProcessWire [PageEditLockFields modules directory page](/modules/page-edit-lock-fields/) or the [PageEditLockFields GitHub page](https://github.com/ryancramerdesign/PageEditLockFields).

Please note this initial release version is a beta test version so test all features thoroughly in a development environment before using in production. If you run into any errors, please report them in the module's [issues page](https://github.com/ryancramerdesign/PageEditLockFields/issues). Thanks for reading!

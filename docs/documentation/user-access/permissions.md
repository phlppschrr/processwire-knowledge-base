# Permissions for access control in ProcessWire CMS

Source: https://processwire.com/docs/user-access/permissions/

## Sections


## Permissions for access control in ProcessWire

Permissions represent a granular permission to access something or to perform some action. This page outlines permissions recognized by the core.

Your system may also have permissions beyond those mentioned here. Any given module may install its own permissions, and likewise you may add your own custom permissions. This page only documents permissions commonly used by the core.


## Permissions overview


### What are permissions?

Permissions in ProcessWire are objects of type Permission (a type of Page object). They each represent permission to access something, or to perform some action. Each permission has a name, and most are self describing. For instance, the page-edit permission is the foundation of providing page editing access.

Permissions are assigned to Roles, and one or more Roles are assigned to each User. Users gain the permissions assigned to their Roles. In many cases permissions can also have a Page context, which is defined with the template used by the Page (Setup > Templates > [template] > Access [tab]). Meaning, the User may have a permission (like page-edit), but it doesn't become applicable to a particular Page unless enabled for the Template used by that Page.


### How do you create a permission?

ProcessWire comes with several permissions that it recognizes (described on this page), but you can also create your own permissions and name them whatever you would like.

Permissions in ProcessWire are pages, and thus can be created like any other pages. But because they are a unique type of page, there is a path you should take to create them. Specifically, in your admin, go to Acess > Permissions > Add New. Enter the name of the permission you want to create in the "name" field, and describe the purpose of the permission in the "title" field.

You can also create permissions from the API:

```
$permission = $permissions->add('permission-name');
$permission->title = 'Description of what this permission does';
$permission->save();
```

After creating a permission, you can easily assign it to any Role from the admin (Access > Roles). In your site or application, you can easily check if the current user has that permission with a single API call, described in the next section.


### How are permissions used from the API?

Whether from the core, a module, or the front-end of your site/application, most permission checking is performed from a single method call on the $user API variable:

```
if($user->hasPermission('permission-name')) {
  // user has this permission in one of their roles
} else {
  // user does not have this permission
}
```

To check if a user has a permission within the context of a particular page, simply add the $page as a second argument to the call:

```
if($user->hasPermission('permission-name', $page)) {
  // user has this permission, for this $page
}
```

A user may have multiple roles. As a result, when providing a $page context like the example above, ProcessWire confirms that the user has that permission in the same role that is defined with the template used by the given $page. Because context is specific to pages, context is primarily applicable to permissions that start with "page", like page-edit, page-view, page-create, page-sort, and so on.


## Default core permissions

These permissions come pre-installed with every copy of ProcessWire.


### page-add

Indicates whether a user has permission to add child pages to a given parent page. This is a symbolic runtime permission and thus does not exist in your list of permissions, but you may occasionally see reference to it. The permission becomes available only if a role already has page-edit permission, and "add" permission is specifically assigned to a role in the template access settings. Since this is a runtime-only permission, you should not attempt to create this permission.


### page-create

Indicates whether a user has permission to create pages of a certain type (template). This is a symbolic runtime permission and thus does not exist in your list of permissions, but you may occasionally see reference to it. The permission becomes available only if a role already has page-edit permission, and "create" permission is specifically assigned to a role in the template access settings. Since this is a runtime-only permission, you should not attempt to create this permission.


### page-delete

Enables a user to remove a page they have edit access to edit. For non-superusers, removing a page implies moving it to the trash. As a result, superusers can recover pages deleted by non-superusers. *Also requires page-edit permission.*


### page-edit

Pre-requisite for having the ability to use the admin for listing or editing pages. A user with this permission (via one of their roles) does not actually have edit access to any pages until they also have edit access assigned at the template level (Access tab). You should enable this permission for any roles that you intend to have any kind of editing or admin access.


### page-edit-front

This permission is available in ProcessWire 3.0 and newer and is installed by the *PageFrontEdit* core module. It enables editing of fields you designate on the front-end of your site. Non-superusers must have this permission in order to make edits on the front-end. Such users must also have page-edit permission. When this permission is assigned to a role, users with that role can make front-edit edits to any pages they already have edit access to edit. Alternatively, this permission can instead be assigned to a role on a per-template basis from the Access tab of a template edit screen, enabling you to provide front-end editing for some instances and not others. For more information on how to implement front-end editing, see our documentation on [front-end editing](/docs/front-end/front-end-editing/).


### page-lister

Enables a user to access the Page Lister. In a default ProcessWire installation, Lister is located at Pages > Find. This permission is also a pre-requisite for [other page-lister permissions](/docs/user-access/permissions/#page-lister-name) used by ListerPro.


### page-lock

Enables user to lock or unlock a page. When a page is locked, no edits may be performed on it until the page is first unlocked. A page can be locked or unlocked from the page editor Settings tab > Status field, or directly in the Page List/Lister inline page actions. *Also requires page-edit permission.*


### page-move

Enables user to change the parent of a page (if the page template family settings allow it to exist in another parent). Parent can be changed from the page editor Settings tab > Parent field, or from the inline drag-and-drop "move" action in Page List. *Also requires page-edit permission.*


### page-sort

Enables user to change the sort order of child pages, or change the predefined sort order (if defined with the page). Note that this permission should be assigned on the page that has the children you want sortable, rather than on the child pages. *Also requires page-edit permission.*


### page-template

Enables user to change the template used by a page. This is performed in the page editor Settings tab > Template field. *Also requires page-edit permission.*


### page-view

Enables a user role to view pages. All roles are required to have this permission. View access is instead assigned with each template (Access tab).


### profile-edit

Enables a user to edit their profile and change their password. This permission is intended for administrative users, as the profile editor is part of the ProcessWire admin.


## Optional core permissions

*These permissions are not installed by default, but are recognized by the core and can be installed from Access > Permissions > Add New.*


### page-clone

This permission is available only if the core ProcessPageClone module is installed. A user with this permission is allowed to clone (duplicate) pages. The clone option appears as a "copy" action for each page in the PageList or Lister modules.


### page-clone-tree

This permission is available only if the core ProcessPageClone module is installed. A user with this permission is allowed to clone (duplicate) a entire tree of pages. Also requires page-clone permission.


### page-edit-created

When combined with page-edit permission, this optional permission limits a user to editing only pages that they created. Unlike other permissions, this permission reduces access by reducing the scope of the page-edit permission. Read more in: [Limiting edit access with page-edit-created permission](https://processwire.com/blog/posts/language-access-control-and-more-special-permissions/#limit-edits-to-pages-user-created-page-edit-created).


### page-edit-images

Use the image editor to manipulate (crop, resize, etc.) images. When not installed, the permission is delegated to page-edit permission instead. Meaning, adding this permission just adds another level of granularity so that you can control access to the image editing tools within image fields.


### page-edit-trash-created

This optional permission lets a user trash pages that they created, so long as they are still editable to them. If the user already has page-delete permission to a page, then page-edit-trash-created permission is not necessary and does nothing. As a result, this permission is only useful in cases where a user does not have page-delete permission, but you still want them to be able to only trash pages they specifically created. Once a page has been trashed, only the superuser can restore or permanenty delete it. *Requires ProcessWire 3.0.31 or newer (or 2.8.31+).*


### page-hide

Enables user to hide or un-hide a page. When a page is hidden, it is not visible in front-end navigation and does not appear in $pages->find() API calls unless "include=hidden", "include=unpublished" or "include=all" is specified in the selector. A page can be hidden or un-hidden from the page editor Settings tab > Status field, or directly in the Page List/Lister inline page actions. When this permission is not installed, page-hide permission is inclusive of page-edit permission. *Also requires page-edit permission and ProcessWire 2.6.15 or newer. *


### page-lister-[name]

Replace "[name]" with the name of Lister and this enables you to assign access to that specific Lister. *Requires ProcessWire 2.6 or newer, the ListerPro module, and page-lister permission as a pre-requisite.*


### page-publish

When installed, a user must have this permission in order to publish any content on the site. Without this permission a user may only edit and/or create unpublished pages, where allowed. Use this permission in instances where you want certain user roles to be able to create (or edit) unpublished pages for someone else's approval. User roles without this permission cannot make edits to existing published content or publish new content.


### page-rename

Change the name of published pages the user is allowed to edit.


## User admin permissions


### user-admin

Enables a user to administer all other users in the system (except superusers). Enables access to the Access > Users section of the admin. *Also requires page-edit permission. *When a ProcessWire 2.6.10+ system also has user-admin-all permission installed, the behavior of this permission is changed. See the following permissions for more details.


### user-admin-all

When installed, this permission takes over the behavior of the user-admin permission, reducing the user-admin permission to just being able to edit "guest" users. The user-admin-all permission is primarily useful when combined with a user-admin-[role] permission, as described next. Users that you want to have this permission must also have page-edit and user-admin permission. Requires ProcessWire 2.6.10 or newer. See also [discussion and examples of user-admin permissions](https://processwire.com/blog/posts/new-user-admin-permissions-automatic-version-change-detection-and-more-2.6.10/#new-user-admin-permissions).


### user-admin-[role]

Enables editing of all users with the given [role]. Replace "[role]" with the name of the role you want to provide edit access to. Also requires page-edit and user-admin permission. Requires ProcessWire 2.6.10 or newer. See also [discussion and examples of user-admin permissions](https://processwire.com/blog/posts/new-user-admin-permissions-automatic-version-change-detection-and-more-2.6.10/#new-user-admin-permissions).


## Multi-language page edit permissions

Multi-language page edit permissions are primarily useful for limiting language access for translator-specific roles. If no multi-language page edit permissions are installed, users with edit access to a given page may edit it in any of the available languages (the default behavior).

*Multi-language page-edit permissions require page-edit permission, ProcessWire core 2.6.3 or newer, and core modules: LanguageSupport and LanguageSupportFields, plus one or more multi-language fields*. For more details, please see: [Language Page Edit Permissions](https://processwire.com/blog/posts/language-access-control-and-more-special-permissions/#language-page-edit-permissions).


### page-edit-lang-default

Enables access to edit fields on a page in the "default" language. This permission is also required to create and/or delete pages, since pages must exist in the default language before they can in other languages. Applicable to a multi-language environment with multi-language fields.


### More about page-edit-lang-default

In ProcessWire, the one required language is "default", and this can refer to whatever language you want it to. Because the default language is always named "default", the corresponding permission is always named page-edit-lang-default. Though note that this permission is not required, but if using these permissions, there's a good chance you'll want it.

As always in a ProcessWire multi-language site, a page must be active in the default language before it can be active in other languages. The default language is the foundation of the page. As a result, a user must have page-edit-lang-default permission if they need to be able to create new pages or delete existing pages (see also page-edit-lang-none permission).

If a user just needs to translate existing pages, then they don't need page-edit-lang-default permission, unless they are translating from one language into the default language.


### page-edit-lang-[name]

Provides edit access to fields in a named language. Replace "[name]" with the name of the language. Applicable to a multi-language environment with multi-language fields.


### More about page-edit-lang-[name]

Once you add a language page-edit permission to your system, all multi-language fields in that language are locked for edits unless the user has the corresponding page-edit-lang-name permission in one of their roles. Meaning, you'll likely want to update the permissions on your user roles (checking the new permission boxes) after adding language page-edit permissions.

If you have a language in your system, but don't have a corresponding page-edit-lang-name permission added, then the language remains editable by everyone that already has edit access to the page and field. As a result, you only need to create page-edit-lang-name permissions for languages that you want to place limits upon… though we'd assume in many cases that would be all languages in your system.


### page-edit-lang-none

Provides edit access to non-multi-language fields in the page editor. Applicable to a multi-language environment with multi-language fields.


### More about page-edit-lang-none

When present, this permission refers to all non-multi-language fields in the page editor. If you have this permission in your system, and a user does *not* have it, then their edit access will be limited to multi-language fields only, in the language(s) they have access to.

This permission is useful when you want to create user role(s) for the purpose of translating pages in one language to another. The translator need only focus on the fields that need translation. All of the non-multi-language fields are simply not shown in the page editor to users that don't have this permission.

If using this permission, be sure to add it to the user roles that DO need edit access to all of the page fields. Otherwise those fields will be invisible to them as well.

Also note that when this permission is present in your system, a user must have it in order to create or delete pages (just like with the page-edit-lang-default permission). That's because when a user doesn't have this permission, they don't have access to modify non-multi-language fields like Template and Parent, among others. Chances are, this behavior is exactly what you'd want for a translation-only role.


### lang-edit

In ProcessWire 2.6.23 (2.7) and newer you can add this permission to give users access to the language tools in Setup > Languages. This is largely useful for performing translations of static files like when creating language packs, or when [translating phrases in your site template files](http://processwire.com/docs/multi-language-support/code-i18n/#translatable-strings). If you want to limit access to only a specific language, install the page-edit-lang-[name] permissions as described above, and ProcessWire will also consider these for access to language pages in Setup > Languages.

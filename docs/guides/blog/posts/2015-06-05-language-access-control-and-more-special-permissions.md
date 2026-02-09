# Permissions part 2: access control for languages and more special permissions (2.6.3)

Source: https://processwire.com/blog/posts/language-access-control-and-more-special-permissions/

## Sections


## Permissions part 2: access control for languages and more special permissions (2.6.3)

5 June 2015 by Ryan Cramer [ 3 Comments](/blog/posts/language-access-control-and-more-special-permissions/#comments)

**ProcessWire 2.6.3 is now committed to the dev branch.** This week we added yet more field permission control–this time limiting edit access to fields by language. We also added a new page-rename permission. While we're at it, this post also describes the other special permissions you can use: page-publish and page-edit-created.

If you are interested in field permissions, be sure to read last week's post too: [Field permissions, overrides and more](/blog/posts/field-permissions-overrides-and-more-2.6.2/).


## **Language Page Edit Permissions**

When a user has access to edit a multi-language field on a page, they have access to edit that field in any language that you have defined on your system. In some cases, you may want to limit what language(s) a user can edit fields in. That's where language page-edit permissions come into play.

For instance, lets say that you hired someone to translate English to German, and you didn't want them making changes to fields in languages other than German. You likely want them to be able to see the English value, but not to change it. Enter language page-edit permissions…


### What are language page-edit permissions?

They are special `page-edit` permissions that you create in your system, and then assign to roles that you want to have edit access to fields in each language.

These permissions follow the naming format of `page-edit-lang-name` where `name` is replaced by the language name the permission corresponds to. For example, our testing system has English (default), Spanish (es) and German (de). The corresponding permissions are:

- `page-edit-lang-default` (for English)
- `page-edit-lang-es` (for Spanish)
- `page-edit-lang-de` (for German)

What the permission will be named in other systems depends entirely on the names of the languages you are using (though `page-edit-lang-default` will likely be found in most installations).

Language page-edit permissions build upon ProcessWire's existing access control system by extending it and adding language specificity. These permissions affect all multi-language fields in the system that the user would have edit access to. They do not give a user edit access to something that they didn't have before. Instead, their presence removes access per-language for users that don't have the related `page-edit-lang-name` permission(s).

There are also two predefined permissions that you can add: `page-edit-lang-default` (corresponding to your default language) and `page-edit-lang-none` (corresponding to non-multi-language fields), which we will discuss more further down.


### Prerequisites

The `page-edit-lang-name` permissions do not become applicable unless a user already has edit access to a given page and field. These permissions build upon the existing access control system in ProcessWire while adding language-specific granularity. There would be no reason to assign a `page-edit-lang-default` permission to a role, if the role did not also already have `page-edit` permission. As such, the prerequisites are:

- User must have `page-edit` permission via one of their roles.
- Role(s) with `page-edit` permission must be assigned to one or more templates (via the Access tab).
- You should have all of PW's multi-language modules installed (LanguageSupport, LanguageSupportFields, LanguageSupportPageNames, LanguageTabs).
- You should be using one or more multi-language fields or language alternate fields.

If you've enabled Access control (PW 2.6.2+) on any fields you intend for the user/role to edit, then you should also make sure the relevant role is checked on the Field's access tab.


### Permission behavior

Once you add a language page-edit permission to your system, all multi-language fields in that language are locked for edits unless the user has the corresponding `page-edit-lang-name` permission in one of their roles. Meaning, you'll likely want to update the permissions on your user roles (checking the new permission boxes) after adding language page-edit permissions.

If you have a language in your system, but don't have a corresponding `page-edit-lang-name` permission added, then the language remains editable by everyone that already has edit access to the page and field. As a result, you only need to create `page-edit-lang-name` permissions for languages that you want to place limits upon… though we'd assume in many cases that would be all languages in your system.


### The most common permission: page-edit-lang-default

In ProcessWire, the one required language is "default", and this can refer to whatever language you want it to. Because the default language is always named "default", the corresponding permission is always named `page-edit-lang-default`. Though note that this permission is not required, but if using these permissions, there's a good chance you'll want it.

As always in a ProcessWire multi-language site, a page must be active in the default language before it can be active in other languages. The default language is the foundation of the page. As a result, a user must have `page-edit-lang-default` permission if they need to be able to create new pages or delete existing pages (see also `page-edit-lang-none` permission).

If a user just needs to translate existing pages, then they don't need `page-edit-lang-default` permission, unless they are translating from one language into the default language.


### Another special permission: page-edit-lang-none

When present, this permission refers to all non-multi-language fields in the page editor. If you have this permission in your system, and a user does *not* have it, then their edit access will be limited to multi-language fields only, in the language(s) they have access to.

This permission is useful when you want to create user role(s) for the purpose of translating pages in one language to another. The translator need only focus on the fields that need translation. All of the non-multi-language fields are simply not shown in the page editor to users that don't have this permission.

If using this permission, be sure to add it to the user roles that DO need edit access to all of the page fields. Otherwise those fields will be invisible to them as well.

Also note that when this permission is present in your system, a user must have it in order to create or delete pages (just like with the `page-edit-lang-default` permission). That's because when a user doesn't have this permission, they don't have access to modify non-multi-language fields like Template and Parent, among others. Chances are, this behavior is exactly what you'd want for a translation-only role.


### How to setup language page-edit permissions

Many multi-language environments don't need this level of access control for multi-language fields, so they are not enabled by default. To enable them, you need to create the permissions you intend to use. ProcessWire provides the tools to make this easy.


### Step 1

Lets say that you have 3 languages in your system: English (default), Spanish (es), and German (de); and you wanted to setup language page-edit permissions for all of them.

You would login to your ProcessWire admin with a superuser account and go to Access > Permissions > Add New. You would add the following permissions:


### Step 2:

*Skip this if you don't have existing roles with page edit access.*

Now that those permissions are added, non-superuser roles in your system with page-edit access can no longer edit multi-language fields. As a result, you will need to go and edit those roles to add the new permissions you added, at least if you want those roles to maintain the same page edit capability.


### Step 3a:

Now lets say that you wanted to create a new role for the purpose of translating English fields to German. You will want this role to only have edit access to fields in German (de). Create a new role (Access > Roles > Add New) and name it something like "german-translator" (or whatever you'd like, the name does not matter). After creating it, you'll be asked what permissions you would like the role to have. Check the boxes for `page-edit` and `page-edit-lang-de`. Save.


### Step 3b:

Before your new permissions do anything useful for the *german-translator* role, they must be assigned to one or more templates. Access is inherited through the page tree until it is overridden by a page using a template that defines access. If you aren't already defining access in any templates, then the access defined on your home template is inherited through to your entire site. As a result, if you want your *german-translator* role to be able to translate any page on the site into German, then this would be a good place to add edit access for *german-translator:*

- Go to Setup > Templates > home > Access
- Check the "Edit" checkbox for "german-translator" and save


### Step 4:

Create a new user account (Access > Users > Add New) and assign the *german-translator* role to it. We also recommend that you set the user's language to be German while you are at it. Login to the admin with this new user you've created and observe how the edit permission works. Try translating a page for testing purposes.

Note that any other languages that aren't editable still appear in the editor, and look like they are editable. If you make any changes to them, the changes are not saved. However, they remain editable on the client-side only. This is to make the translators job easier when it comes to copy/paste or comparing translated text to the original.


### Step 5: (optional)

You may have noticed in step 4 that your *german-translator* user can edit non-multi-language fields. Perhaps you don't want them to be able to do that, since those fields need no translation. If this is your need, proceed with creating the following new permission (Access > Permissions > Add New):

- **Title:** Edit non-multi-language fields
- **Name:** `page-edit-lang-none`

Do not assign this permission to your *german-translator* role. The mere presence of this permission in your system will automatically revoke edit access from all non-superuser roles to all non-multi-language fields. In the case of our *german-translator*, this means that they now only see translatable multi-language fields in the page editor, and can only edit those fields in German (de) – our desired outcome.

If you have other page editor roles in your system that *do* need access to edit these non-multi-language fields, then you should go ahead and add those roles and enable the `page-edit-lang-none` permission for them.

Now login with your *german-translator* account again and observe the page editor behavior with your `page-edit-lang-none` permission in the system.

You could also achieve step 5 by using field-level permissions individually, field-by-field (via Setup > Fields > any_field > Access). But using the page-edit-lang-none permission provides a quick short-cut that can potentially save you a lot of time.


## **New page-rename permission**

ProcessWire 2.6.3 adds support for a new permission called `page-rename`. This permission grants access to change the "name" field of a page, and its presence in your system prevents users [without the permission] from renaming published pages. This permission can be used on any ProcessWire installation, multi-language or not. Like the new language permissions mentioned above, it is not installed by default and its behavior only becomes active once you create it. When the permission is not present in your system, everything works as it always has.


### Why limit page name changes?

Normally when a user has access to edit a page, they also have access to change its name. Yet, changing the name of a published page is often undesirable, as it changes the URL that the page is accessed at. Changing a name can potentially break internal and/or external links to the page (though the core *PagePathHistory* module is helpful here, when installed). Further, if the page has children (or perhaps thousands of them) a name change likewise changes the URLs for all of them as well–not good.

In my own sites, I often make API calls that refer to a page's path (for readability), like `$pages->get('/products/')->children();` or the like… I definitely don't want the name to change, because it could break functionality in the site.

For these reasons, support for the `page-rename` permission was added. Now you have a really simple means of preventing non-superusers from changing the name of published pages.


### How to use the page-rename permission

To take advantage of the page-rename permission, you just need to add it in your ProcessWire admin at Access > Permissions > Add New:

- **Title:** Change the name of published pages
- **Name:** `page-rename`

When present in your system, any users that lack the page-rename permission will not be able to change the name of published pages.

**What about unpublished pages?** Users that can edit a page can still change the names of unpublished pages. Likewise, if a user is creating a new page, they can set and change the name as much as they'd like, until the page is published.

Superuser can always rename pages, but if you've got other roles that you want to be able to rename pages, then simply add the page-rename permission to their applicable role(s).


## **What other “special” permissions are there?**

If you read all of the above, then I know what you are thinking, *“what other special permissions can I add in ProcessWire?”* While not specific to ProcessWire 2.6.3, or even ProcessWire 2.6, these are the other special permissions that ProcessWire has supported for a long time:


### Publish pages: page-publish

When installed, a user must have this permission before they can publish pages (or edit already published pages). If the user is allowed to create pages, then they can continue to do so… they just can't publish them. This permission is useful in an environment where new pages need to be approved before they are added to the site.


### Limit edits to pages user created: page-edit-created

This permission is a bit unique in that it actually reduces access (to roles that have it) rather than adding access. When a user has this permission (combined with page-edit permission) they can only edit pages that they created. This permission is useful in environments where there are multiple authors submitting articles or posts, and you may not want one author modifying another's content.

Lets say that we have two users: Hanna and Ryan. Both have a role called "author", which has `page-edit` and `page-edit-created` permission. Both Hanna and Ryan create a new blog post. Hanna cannot edit Ryan's post, and Ryan cannot edit Hanna's post. Yet both can edit their own posts.


### How do you create a special permission?

All of the permissions mentioned in this post are special permissions, in that they don't become active unless you create them yourself. This is really easy to do: just go to Access > Permissions > Add New and make sure the permission "name" is consistent with the permission names we've described here. Be careful when adding special permissions, especially on production sites, as they change the access control behavior, as described in this post.

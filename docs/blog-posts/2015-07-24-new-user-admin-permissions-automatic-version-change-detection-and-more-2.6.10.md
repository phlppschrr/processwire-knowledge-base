# New user-admin permissions, automatic version change detection, and more (2.6.10)

Source: https://processwire.com/blog/posts/new-user-admin-permissions-automatic-version-change-detection-and-more-2.6.10/

## Sections


## New user-admin permissions, automatic version change detection, and more

24 July 2015 by Ryan Cramer [ 1 Comment](/blog/posts/new-user-admin-permissions-automatic-version-change-detection-and-more-2.6.10/#comments)


## ProcessWire 2.6.10

The biggest update this week is support for the new user-admin granular permissions. If you have an authenticated user-driven site and lots of users and roles to manage, this may be a lifesaver. Or if you don't, then you can ignore it, as it's not something you have to consider unless you add the new optional user-admin-all permission. In either case, we hope you'll read about it, as it could be really handy when you need it.

This week also brings much improved detection of core and module version changes, improvements to the permissions view (when editing a role), a new capability to re-label the page "name" field, several minor bug fixes and tweaks, and more… all the details are below. Thanks for reading!


### Core version changes now bring new automation

As many of you know, we put out a new version of ProcessWire just about every single week, and usually on Friday. It very often happens that after upgrading, people encounter a JS error somewhere, an odd CSS style, or a mis-labeled version somewhere, and inquire about it (in fact, I often do it myself).

It's almost always the result of caching, whether PW's modules cache or your browser cache, and can be cleared up by clicking to Modules > Refresh in the admin. That triggers ProcessWire to rebuild its cache of module information, including module versions. The module versions are used for cache-busting JS and CSS files, which is why doing a Modules > Refresh typically clears up such issues.

As of this week, ProcessWire's core SystemUpdater module now detects core version changes automatically, and handles refreshing the modules cache for you. This should hopefully reduce confusion through core upgrades, and eliminate cached assets from previous core versions showing up, regardless of whether you reset PW's modules cache (in fact, there's no need to do it anymore following a core upgrade).


### New managed module versions by the core

Previously when you did a Modules > Refresh, ProcessWire would pick up on any new module versions, though nothing much happened beyond that. If a module needed to detect when its version changed, it had to keep track of it by some internal means. The core now keeps track of this, and has the capability to notify the module when its version has changed.

In order to support this, the module simply needs to implement this method:

```
public function ___upgrade($fromVersion, $toVersion) {
  // any code you want to handle an upgrade
}
```

This accompanies the existing `___install()` and `___uninstall()` methods that module developers are already familiar with. Rather than calling the `___upgrade()` method at the time the version change is detected, the method is instead called the next time the module is loaded. For instance, if it was detected that the ProcessPageEdit module version changed, its upgrade method wouldn't be called until the next time you edited a page. This ensures that modules aren't loaded outside of their normal context.

If your module version changes occurred at some time other than during a core upgrade, you would still have to do a Modules > Refresh before ProcessWire would detect them. This would be applicable mainly to modules in /site/modules/, as the module versions in the core /wire/modules/ typically accompany a core version change. However, stay tuned, we've got more coming on this.


### New user-admin permissions

Lately there have been requests for expanded capabilities with the `user-admin` permission. Specifically, some have requested the ability to have roles that can manage some users and not others. I think it makes a lot of sense. This week we've added that capability. Here's how it works:

When you add the new optional permission `user-admin-all` to your site's permissions (Access > Permissions > Add New) a user must have that permission (in addition to user-admin permission) in order to edit "all" users in the site (superusers excluded, as before). That user-admin-all permission basically duplicates the behavior of the existing user-admin permission. If a user has user-admin permission, but not user-admin-all permission, they are limited only to editing users with nothing but the "guest" role, and they can't assign any new roles to those users.

You don't need to assign the user-admin-all permission to any roles if you don't want to. The presence of the user-admin-all permission is basically your way of telling ProcessWire that you intend to add more `user-admin-[role]` permissions for granular user management by role. Here's an example to describe how it works…

Lets say you've got these user roles in your system (under Access > Roles):

- **members:** Users that can view members-only content after logging in
- **members-manager:** Users that can add, edit, and delete members users
- **authors:** Users that can create members-only content on the site

Previously it would not have been possible to have a members-manager role with the permissions as described above, because once a user had user-admin permission, they could manage both members and authors (and any other users). In our case, we only want them to be able to manage members and not authors or users in other roles.

As of ProcessWire 2.6.10, you can now handle this easily by doing the following:

The user-admin-all permission that you added might still be useful if you have a need to have non-superusers that can edit users with any role (other than superuser). It would duplicate the behavior of the user-admin permission in a system that has no user-admin-all permission.


### Improved permissions view (in Access > Roles)

As we support more optional permissions and access control scenarios like the one described above, the permissions field in the role editor gets to be a bit busy and cumbersome. So we put in a few small tweaks to it this week that make it easier to look at an manage. Specifically, related permissions are now grouped together and have a visual hierarchy to clarify which permissions are pre-requisites of another. For instance, user-admin is a pre-requisite of user-admin-all, and any other role-specific permissions you might add. ListerPro uses a similar permission hierarchy as well.


### New page name label configurable in template settings

This week I was working on a project where we are using ProcessWire's built-in page name field to represent unique product IDs. We've configured the name field to appear on the Content tab (rather than the Settings tab*), so it is seen as not just a page name for the URL, but a unique product ID, as part of the overall page's content.

The above is all well and good, but the client kept getting confused by the terminology "Name", and didn't understand why it didn't instead say "Product ID". And I thought the question made a lot of sense. "Why on earth don't we support re-labeling of the name field by template?" I thought, seems like we should. I couldn't come up with a good answer, so went ahead and added support for it. You'll now see it when editing a template (Setup > Templates > any-template) on the Advanced tab, right next to the existing tab re-labeling fields.

*Showing the "name" field on the Content tab is similar to the behavior you already see when editing Users, Roles, Permissions and Languages. But you can actually do this with any template. The name field can be moved to the Content tab from Setup > Templates > [template] > System [tab]. You'll only see that System tab if you first enable $config->advanced = true; in your /site/config.php file. Just remember to turn advanced mode back off once you are done making the adjustment, as it's not something you usually want to keep on.


### Wrapping up

There are also some pending updates for the [Reno admin theme](https://github.com/Renobird/AdminThemeReno) that I meant to get into the core this week, but will be coming next week instead. Hope that you all have a great weekend and week, and remember to tune into the [ProcessWire weekly](http://www.flamingruby.com) tomorrow morning, or [subscribe](/contact/subscribe/) and we'll email it to you next week.

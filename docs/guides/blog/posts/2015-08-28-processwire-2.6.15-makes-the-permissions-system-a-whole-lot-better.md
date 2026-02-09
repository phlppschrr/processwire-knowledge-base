# ProcessWire 2.6.15 makes the permissions system a whole lot better

Source: https://processwire.com/blog/posts/processwire-2.6.15-makes-the-permissions-system-a-whole-lot-better/

## Sections


## ProcessWire 2.6.15 makes the permissions system a whole lot better

28 August 2015 by Ryan Cramer [ 1 Comment](/blog/posts/processwire-2.6.15-makes-the-permissions-system-a-whole-lot-better/#comments)


## ProcessWire 2.6.15

The focus of this week has been on ProcessWire's permissions system. We've taken what we already had, and made it a whole lot better, while also making it simpler. Here's what we've done:


### Major enhancements to template access control

As you might already know, access control for pages is handled in templates (template editor "Access" tab). You've always been able to assign View, Edit, Create and Add page permissions, to any role, in a template where you enabled access control. When you enabled "Edit" (page-edit) permission for a role, the user would also gain any of the other edit-related permissions assigned in that same role. I'm talking about permissions like page-sort, page-template, page-publish or any number of other permissions related to page editing. But if you wanted to have a single role that could (for example) publish pages of one type, and not another, you were out of luck… you would have needed multiple roles for that. And that can start to get complicated, quickly.

With ProcessWire 2.6.15, we've made it simpler, more powerful, and more flexible. You can now add or revoke any of those permissions, from any role, directly in the template access settings. Here's how it works: when editing access control settings for a template (Setup > Templates > Access) ProcessWire figures out all the roles that have edit access to it, and then looks at what permissions each role has, and doesn't have. For any permissions that the role doesn't already have, you have the option to add it, specific to that template. Such a permission will apply only when requested in the context of a page using that template. For any permission the role already has, you have the option to revoke that permission, specific to that template.

Within the context of the sites I'm working on, I've found it convenient to create an "editor" role and just give the role page-edit permission, nothing more. Then I go and edit a template's access settings, check the box to enable "Edit" permission for my "editor" role, and then selectively add any other permissions I want it to have for that particular template. For instance, I want my "editor" role to have page-move permission for pages using the "basic-page" template, but not for pages using the "blog-post" template. Of course, that's just a simple example, but hopefully communicates a little bit about potential here.

Here's a screenshot of the template editor where permissions can be added and revoked.


### New control over access inherit behavior

Also related to the template editor, we have a new setting that you can apply in template access control settings. This one is a simple on/off toggle, but an incredibly useful one. As you might know, access control settings inherit through the page tree until a page using another access controlled template overrides it. This allows for a lot of flexibility, as you can make an entire section of pages inherit the access control behavior of a specific parent page.

This is particularly useful when it comes to "view" permission, as you can delegate entire branches of your site tree as either viewable, or not viewable, to any given role. You only have to manage access for the template used by the root page of the tree. The edit permissions (edit, create, add) inherit in the same way, and often that's exactly what you want…

But what if it isn't? For instance, lets say you want to have a role that can view any page, but can only edit the homepage. As soon as you make the homepage editable, all the child pages also become editable. (Perhaps making the entire site editable if there are no other access controlled templates.) You would have to ensure that all the children are using access controlled templates in order to prevent the edit permissions on the homepage from inheriting to the children and further. I'm using the homepage here as an example, but the same would apply to any page in your site using an access controlled template, that doesn't have access controlled children.

ProcessWire 2.6.15 introduces a new toggle in the template settings that makes this a whole lot simpler. It lets you tell ProcessWire whether or not you want edit permissions to inherit beyond pages using that template. To use our homepage example again, now you can edit your "home" template and tell it not to allow edit permissions to inherit beyond the homepage. This enables you to easily make a single page editable (like the homepage) without having to worry about what else you are making editable. This inherit setting applies to any edit-related permission, whether one of the predefined edit/add/create permissions, or any others you have specifically added (per the previous section in this post).


### Major enhancements to the role editor

A few weeks back, we introduced some enhancements to the role editor that made it a lot easier to navigate permissions attached to a role. But after using it for a little while, I felt it was definitely a nice improvement, but just didn't go far enough. Also, I didn't like having to check a permission (like page-edit) and then save, before I could reveal the other permissions below it… I was really after something that worked like the page tree, and this wasn't it. Further, there just wasn't enough information. I wanted to know where the permissions were applied (in terms of templates), rather than having to find out myself by navigating through each access controlled template. Even more so after the other permission upgrades added this week.

Now the permissions field in the role editor solves all of this. Not only is the hierarchy easier to understand, but it's a lot more page-tree like, in that you can click a permission and see child permissions appear immediately. Further, it tells you exactly where a given permission is applied (in terms of templates) and whether it's being added or revoked (per the other updates this week). It also makes it clear to you when a permission you are adding will override a permission you've added or revoked to a template. All in all, I think you'll find this makes role configuration a whole lot simpler and less ambiguous.


### New optional permissions…

A new optional permission was added this week: [page-hide](../../docs/user-access/permissions.md#page-hide). Add this permission to your system if you'd like the ability to control whether a given role can hide/unhide a page or not. Without this permission, any user with edit access can hide or unhide a page. When the permission is installed, a user will have to have the permission before they will be able to hide or unhide a page they already have edit access to. This new permission works a lot like the recently introduced [page-lock](../../docs/user-access/permissions.md#page-lock) permission.

As I was doing a lot of testing with the permissions system this week, I discovered the recently introduced [page-edit-created](../../docs/user-access/permissions.md#page-edit-created) (optional permission) was not working as intended. That's been fixed in 2.6.15.

Stay tuned, as we'll be adding a few more optional core permissions in the coming weeks. Specifically, we're trying to account for scenarios that some of you are currently using hooks for. For instance, one of the next ones on the to-do list is page-delete-created, which limits the [page-delete](../../docs/user-access/permissions.md#page-delete) permission to apply only to pages a user created.


### Plus a much simpler way to install optional permissions

ProcessWire now supports a lot of useful optional permissions that are recognized by the core, but not installed by default. And we're going to be expanding that list as time goes on. Currently the optional permissions are largely secrets for readers of this blog. We thought there needed to be a way to make them much more visible, and much easier to install. So this week we've introduced a 1-click installer for them, right in the core. To access it, simply go to Access > Permissions > Add New. Now you have the choice of installing one of the pre-defined optional permissions, or creating your own custom permission.


### New permissions documentation and reference section

With all the new activity around permissions, we needed a lot better documentation for them. Actually, we needed that long before this week. So I spent some time this week building that out, and you'll find it [here](../../docs/user-access/permissions.md). This section is also now thoroughly linked everywhere applicable in the PW core, so if there's ever any question about what a permission does or how permissions work, we've now got you covered much better than before.

Hope that you all have a great weekend and week ahead. Remember to catch up with the latest ProcessWire news with the [ProcessWire Weekly](http://weekly.pw), published every Saturday.

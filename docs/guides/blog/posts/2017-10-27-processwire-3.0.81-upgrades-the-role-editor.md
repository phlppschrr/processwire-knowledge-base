# ProcessWire 3.0.81 upgrades the Role editor

Source: https://processwire.com/blog/posts/processwire-3.0.81-upgrades-the-role-editor/

## Sections


## ProcessWire 3.0.81 upgrades the Role editor

27 October 2017 by Ryan Cramer [ 4 Comments](/blog/posts/processwire-3.0.81-upgrades-the-role-editor/#comments)


## ProcessWire 3.0.81

This week's new version on the development branch makes major improvements to the Role editor, simplifying the setup of access control in ProcessWire. Previously you could just assign permissions to a Role in the Role editor, and you couldn't specify what template(s) those permissions would apply to. That could only be done in the Template editor's “Access” tab. So setting up page access control involved a dance between the Role editor and the Template editor. And this makes sense in many scenarios, but in others it could add confusion or increase the amount of time it took to setup a Role.

This week we upgraded the Role editor so that not only can you assign permissions to a Role, but you can also specify what templates those permissions apply to. Meaning, you can setup everything on one screen, which can save a lot of time and make things a lot more clear.

When you edit a role, it looks much like before except that some permissions (page-view, page-edit, page-add, page-create) have the list of access controlled templates ready for you to add the permission to. Just that is quite an upgrade relative to before. But ProcessWire 3.0.81 also supports the ability to add or revoke *any* page-edit related permission for a Role on a per-template basis.

For instance, maybe you want a Role to be able to delete one type of page and not another. Or maybe you want a Role to be able to publish some types of pages and not others. The capability was already in the core (in the Template “Access” tab), but a little cumbersome to configure and keep track of. You could also accomplish the same thing by creating multiple roles with different access settings, and then assign those multiple roles to a user. While quite powerful, this too was a bit cumbersome to setup and difficult to keep track of. Now you can do it all from the Role editor on a single screen, making things a lot simpler. However, note that a template must have access control enabled (an on/off toggle that must be “on”) before the template would appear as an option in the Role editor.


### How it works

When you check the checkbox next to a page editing related permission, that enables the permission for templates that the user has page-edit permission to. This is essentially how the Role editor worked before. But now there is a new option: click the icon in the right column to reveal a list of templates that you can assign the permission to (or click it again to collapse). Rather than enabling the permission for all templates, you can selectively enable it for specific templates that you choose here. Alternatively, if you've checked the permission box that enables it for all editable templates (the default) then you have the option of revoking the permission from specific templates. See the screenshot above for examples of each.

If you've just added a new template to your site, then chances are you'll still want to use the Template editor Access tab to do this kind of configuration. But for nearly any other case, I think you may find this new Role editor adds clarity and saves time. I hope that you enjoy using it and please let me know how it works for you. Have a great weekend and enjoy the [ProcessWire Weekly](http://weekly.pw).

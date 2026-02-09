# ProcessWire 3.0.115 and 3.0.116 core updates

Source: https://processwire.com/blog/posts/processwire-3.0.115-and-3.0.116-core-updates/

## Sections


## ProcessWire 3.0.115 and 3.0.116 core updates

5 October 2018 by Ryan Cramer [ 2 Comments](/blog/posts/processwire-3.0.115-and-3.0.116-core-updates/#comments)


## ProcessWire 3.0.115 and 3.0.116

This week we look at the two newest development branch versions, as there was no post last week. I couldn't type very well this time last week due to a cat bite, but all is well now. We didn't have a blog post for the 3.0.114 core updates, but there was a brief update on that version in the forum [here](/talk/topic/20017-pw-30114-%E2%80%93%C2%A0core-updates/), if you haven't already seen it. In this post, we'll cover what's new for 3.0.115 and 3.0.116, which includes quite a lot.


### New $page traversal methods

`$page->findOne()` This is like the $page->find() method except that it returns a single matching descendant page rather than all matching pages. You might already be familiar with $pages->findOne(); and this version on $page works exactly the same except that its results are limited to pages beneath it (children, grandchildren, etc.) [API reference page](../../../full/wire/core/Page/method-findone.md)

`$page->numDescendants()` This is similar to the $page->numChildren() method except that the count includes not just children, but all descendants: grandchildren, great-grandchildren, etc. This can also be accessed as the property $page->numDescendants. See the optional arguments to this method if you want to get a filtered count of descendants. The arguments work just like those of $page->numChildren(). [API reference page](../../../full/wire/core/Page/method-numdescendants.md)

`$page->descendants()` and `$page->descendant()` These are actually alias methods that simply map to $page->find() and $page->findOne(), but I liked the clarity of their naming that corresponds with the new numDescendants() method. So if there are cases where this naming adds readability to your code, the option is now there.


### Page list customization

You can now customize what is represented by the children count number that appears in the page list. In this past, this number has always represented the number of direct children that a page has. But now you can also customize it to represent a count of descendants, both children and descendants, or the page ID. In this screenshot below, it is showing “children/descendants” count:

[](//d1juguve2xwkcy.cloudfront.net/assets/files/1156/screen_shot_2018-10-05_at_2_56_03_pm.png)

The configuration setting can be found in the *ProcessPageList* module configuration screen:


### Who likes emptying the trash?

Lots of improvements to the trash emptying process have been added this week. First off, the empty trash process screen has been improved and simplified. It now also lets you specify a max time limit (in seconds) for emptying trash (useful for those instances where you might have thousands of pages in the trash).

After you empty the trash, it'll give you more information about how it went, including the amount of time it took per page. This can help you to estimate how much time it might need when you've got a lot of trash, and whether you should go grab lunch right now, or maybe just a coffee…

…or take a cruise around the world, or go on sabbatical… or get a new computer. Rest assured, my computer is just old and slow. Another user has reported an empty trash rate of hundreds of pages per second on a more modern computer. Your "pages per second" rate of emptying trash will depend on how fast your computer/server is, how much data is connected with each of the trashed pages, and whether there are also files that go along with it, etc.

This all follows a fairly major refactoring of the *PagesTrash* class in the core. A lot of improvements have been made to the underlying code. It is now more efficient and reliable, more verbose in it's reporting, and a lot faster in some cases. Though if you've got 400k+ pages in the trash like I do, it might still take awhile. :)


### Two-factor authentication improvements

Having two-factor authentication is a great security improvement, but not unless people actually use it. You can now configure the *ProcessLogin* module so that it bugs users of specified roles to enable two-factor authentication. Here's how you configure it:

It will let them use the admin, but they'll be constantly reminded and annoyed that they need to enable two-factor authentication by feeding obnoxious advertisements to them until they enable it. Not everyone understands the importance of two-factor authentication, but nobody likes being constantly reminded and distracted, so sometimes they need a little push in the right direction:

Don't want to enable two-factor authentication now? That's okay, go about your business, we'll be waiting right here at the top of the screen.

Unfortunately, in our user testing here, we discovered that 83% of users were clicking the ads rather than the "Enable two factor authentication link", and then going off in to playing games, ordering enhancement pills, and gambling on other websites; completely forgetting what they were doing in ProcessWire. So we had to remove the ads, and instead just prompt them to enable two-factor authentication. So here's what it actually looks like below. Of course I was kidding about the ads, but thanks for putting up with my terrible sense of humor.

Prior to this update, users on your system may have not even known about the two-factor authentication option (if you installed it) unless they went to their user profile screen for some other reason. So if you enable two-factor authentication for your admin, this feature is a good way to ensure that it actually gets used and increases the security of your admin.


### Profile screen password dialog/prompt

Some fields on the user profile screen require that the user enter their current password before they can save their changes. This ensures that if someone else comes across your desk, and you are logged in, they can't go change your password, email address, or two-factor authentication settings (as examples) without a password to verify that they are in fact you.

This has worked pretty well, but I found that for some users it wasn't always clear. When they click the submit button, it focuses the "current password" field, but sometimes people thought that it was also asking them to change their password, since they enter their current password in the same field where you set or change your password. So I thought some additional clarity was needed here. This was corrected by moving the required current password to a dialog/prompt window that appears when click the submit button, after making changes to any field that requires this confirmation.

There were also several bug fixes, both in 3.0.115 and 3.0.116, as well as some other updates. The [ProcessWire Weekly #229](https://weekly.pw/issue/229/) did a great job of covering some of these from 3.0.115 last week, so if you haven't read that post yet be sure to read it at [ProcessWire Weekly](http://weekly.pw). Thanks for reading, see you next week and have a great weekend!

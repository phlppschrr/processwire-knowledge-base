# Continuing work on new admin theme framework

Source: https://processwire.com/blog/posts/continuing-work-on-new-admin-theme-framework/

## Sections


## Continuing work on new admin theme framework

17 February 2017 by Ryan Cramer [ 18 Comments](/blog/posts/continuing-work-on-new-admin-theme-framework/#comments)

[Last week](/blog/posts/working-towards-a-new-admin-theme/) we looked at progress on a new admin theme framework for ProcessWire. This week we’ll do the same, as development continues to move forward and we have a lot more screenshots to share.


### Progress and features (design not literal)

Like last week, I wanted to mention that this is not meant to demonstrate design, but rather, progress and features. What you see here is essentially the stock Uikit framework theme. As some of you mentioned last week, it may be too minimal for your tastes. I agree. And it's pretty monotone too. But this minimalism is helpful for us at this stage in the development, so please don’t take any design aspects to literally, as the admin theme(s) that eventually result from this will likely look quite different. We are in kind of a blueprint stage right now.

Speaking of minimalism, I noticed that the light borders around fields are very obvious on one of my computers (Macbook Pro), and nearly invisible on another (older Mac desktop). So I’m not positive that you’ll be seeing these screenshots as intended, as it seems to depend on the screen. If some of the features are too light to see on your screen, I apologize. We’ll try to increase contrast from the default styles before the next post that includes screenshots.


### Oops

Before you continue, note I've got an extra “user” icon present in the masthead top navigation of all these screenshots and didn't realize it until now. It's that one next to the Access link. That's not supposed to be there, so please ignore that. :)

Click the screenshots to view them at full resolution.


### Standard/border style

In this first screenshot, we have the default Inputfield style which uses borders around each Inputfield, just like the current Default and Reno admin themes. (Depending on your screen, you may not be able to see those borders very easily). Also note the addition of CKEditor 4.6, which includes a new skin that many prefer (and certainly works better with our admin theme updates). You’ll find CKEditor 4.6 on the core dev branch now.

[](//d1juguve2xwkcy.cloudfront.net/assets/files/1075/1pw-edit-standard.png)


### Standard/border style with vertical offset option

This next screenshot is the same thing, except with a vertical offset enabled. This provides a vertical whitespace between the borders of each Inputfield. This is something that can be enabled with a $config setting in ProcessWire (for all Inputfields) or individually for any given Inputfield.

[](//d1juguve2xwkcy.cloudfront.net/assets/files/1075/2pw-edit-standard-offset.png)


### Uikit “card” style

Next we’ve got the same view as screenshot #1, except that this uses the Uikit “card” style for Inputfields. It softens up the borders and gives fields some depth in many cases. I find this card view to be pretty nice, especially when getting into fieldsets and other kinds of nested Inputfields. For the purposes of this blog post, the card style seems to be a little easier to see, given how light the borders are. So I'll stick to using this card style for the remaining screenshots.

[](//d1juguve2xwkcy.cloudfront.net/assets/files/1075/3pw-edit-cards.png)


### Card style with vertical offset option

Here is the card view again, but with the vertical offset option enabled again, like in screenshot #2.

[](//d1juguve2xwkcy.cloudfront.net/assets/files/1075/4pw-edit-cards-offset.png)


### Turn off borders per field

A feature that we demonstrated in last week’s screenshots was the ability to turn off borders completely. You’ll now have a field setting where you can specify that you want any particular field to have no border, as you’ll see with the “Body” field below. This field is an obvious example of one that doesn’t really benefit from a border because it already has the border provided by CKEditor.

[](//d1juguve2xwkcy.cloudfront.net/assets/files/1075/5page-edit-noborder1.png)

In this next screenshot, we’ve gone a little further with turning off borders and also turned them off for the Title and Date fields as well.

[](//d1juguve2xwkcy.cloudfront.net/assets/files/1075/6page-edit-noborder2.png)


### Uikit color options

When using ProcessWire with this Uikit-based admin theme framework, you can also differentiate fields with color. A field can be specified as Primary, Secondary, Success, Warning or Danger (which are Uikit color names). In the example below, these are the assignments present:

- Date: Secondary
- Body: Warning
- Images: Danger
- Categories: Primary

These colors are defined by the Uikit theme, so what color they actually represent depends on the Uikit theme that is in use. The screenshot demonstrates the default colors.

You’ll also see the open comments field, which is already using these color assignments by itself in order to differentiate pending (blue) comments from approved (green) and spam (not shown) comments. We imagine that most of the time you won't need to use these color options, but they will definitely be handy for certain cases where you need to call attention to a particular field. For instance, we'll be using the Danger color to highlight Inputfields that have an error that needs resolution.

[](//d1juguve2xwkcy.cloudfront.net/assets/files/1075/7page-edit-colors.png)


### Language tabs

Here's a look at text fields with multi-language tabs.

[](//d1juguve2xwkcy.cloudfront.net/assets/files/1075/screen_shot_2017-02-17_at_2_30_45_pm.png)


### Modules

Here is a screen from the Modules section of the admin.

[](//d1juguve2xwkcy.cloudfront.net/assets/files/1075/8modules-new.png)


### Fields editor

Here’s the Setup > Fields list screen.

[](//d1juguve2xwkcy.cloudfront.net/assets/files/1075/9fields-list.png)

Lastly, here’s a really large screenshot that shows the Input tab of the Field editor when editing a CKEditor field.

[](//d1juguve2xwkcy.cloudfront.net/assets/files/1075/10field-edit.png)

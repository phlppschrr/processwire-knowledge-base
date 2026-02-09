# ProcessWire, Form Builder and CSS frameworks (2.5.23)

Source: https://processwire.com/blog/posts/processwire-form-builder-and-css-frameworks-2.5.23/

## Sections


## ProcessWire, Form Builder and CSS frameworks (2.5.23)

20 March 2015 by Ryan Cramer [ 7 Comments](/blog/posts/processwire-form-builder-and-css-frameworks-2.5.23/#comments)

This week there were several updates to the core, but nothing that is necessarily eye candy or things I think you'd be interested in reading about here. Lots of little fixes, tweaks and adjustments. Even if they aren't interesting to read about, they are quite important as we prepare for ProcessWire 2.6. Like I mentioned last week, these updates will likely continue over the coming weeks, but we'll also be bringing in some excellent PRs that I think you will enjoy.

While the updates to the core may have been a little less exciting this week, a whole lot of interesting stuff did happen. It's been my goal to update all of the Pro modules (and many of the other non-core modules I maintain) for ProcessWire 2.6. Recently there have been major updates for ProFields and ListerPro, and this week it was Form Builder that got major updates. Even if you aren't using Form Builder, you might be interested in what some of these developments could mean for the ProcessWire core. Form Builder now has a few tricks that you may see in ProcessWire 3.0.


### Form Builder gets a major upgrade

A regular request for Form Builder has been "how do I make it output a form for [Bootstrap, Foundation, Uikit and so on]." My response has always been that those frameworks don't have the level of features necessary to accommodate all that our Inputfields system needs (which is used by both FormBuilder and the core), unless you stick to the basic input types. This is still true. But as the CSS frameworks continue to mature, and as we use them more and more, it's become clear that it doesn't have to be an either/or proposition.

It turns out that they can be used together, and quite smoothly. Our Inputfields system and the CSS frameworks are actually accomplishing quite different things for the most part. I setup a test case with Uikit, and I was so thrilled with the result that I couldn't wait to get it built into Form Builder and add more frameworks to it.

An hour ago I posted Form Builder 0.2.5 beta to the support board. This version offers native Bootstrap, Uikit, Foundation (or any CSS framework) forms, while still being able to benefit from the configuration potential, field dependencies, column widths and more of ProcessWire Inputfield forms. You can now create forms for any of these frameworks in Form Builder and they will "just work", and they look great.


### What about jQuery UI?

jQuery UI had been a big part of ProcessWire's admin, FormBuilder and Inputfield forms in the past. That started to change in ProcessWire 2.4, and has continued into 2.5. As it is right now, our main use of jQuery UI is specific to sortable lists and native widgets like AsmSelect and Date/Time pickers. If your form doesn't happen to use a field that requires these things (and most don't), then it simply isn't loaded. Actually, this has always been the case, but in Form Builder we continued to rely on jQuery UI's CSS themes as our primary method of styling forms… and this is no longer the case.

As of the latest version of FormBuilder, Inputfields are now completely independent of jQuery CSS classes and styles (except those that require it, which are few and far between). Does this mean we're trying to get away from jQuery UI in ProcessWire? No. Speaking in terms of the ProcessWire core, for the things we use jQuery UI for, it's great, and the most powerful thing out there. This despite some very interesting, and often prettier JS tools in some of the CSS frameworks. But it's also true that we are getting to the point where we could easily replace jQuery UI with something else if the reasons were strong enough to do so in the future.


### Supported frameworks and features

- **Admin** (default or Reno): This duplicates the look of the ProcessWire admin.
- **Legacy** (for backwards compatibility): These are the old jQuery UI themed forms, for those that want to continue using them.
- **Bootstrap:** Support for both stacked and horizontal forms, configurable column widths, configurable submit button sizes and type, configurable input sizes, configurable responsive breakpoints.
- **Foundation:** Support for both stacked and horizontal forms, configurable column widths, configurable submit button size, type, and style, configurable responsive breakpoints.
- **Uikit:** Support for Uikit themes (default: almost-flat, normal, gradient, or custom), support for both stacked and horizontal forms, configurable input sizes, configurable button size and type, and configurable responsive breakpoints.
- **Plus:** frameworks are supported by plugins to Form Builder, meaning we'll be adding more and you can too.

For Bootstrap, Foundation and Uikit, you can also configure FormBuilder to use your own copy of the framework, or use a copy that comes with FormBuilder for your convenience.


### New direct embed method

If you are already using one of the supported CSS frameworks mentioned above, then another benefit you'll see is that direct embedding of a form (rather than being isolated in an iframe) becomes a much simpler proposition. CSS conflicts between FormBuilder and your own site become much less likely. As a result, we've introduced a new embed method (replacing the previous embed method C) that makes the API side of this very simple:

```
// prepare a form for output
$form = $forms->render('your-form');

// in your document <head>
echo $form->styles;
echo $form->scripts;

// somewhere in your document <body>
echo $form;
```


### What does this all mean for ProcessWire's core?

What affects ProcessWire's core affects Form Builder, and what affects Form Builder affects ProcessWire's core. They are both using the same Inputfields form system. So all of this means that future ProcessWire admin themes will be able to support CSS frameworks in the same way. Is there a need for that in the admin? I'm not so sure about that, but it's nice to have the option. It's nice to be independent of these things, but it's also nice to be able to use them sometimes too.

One thing I learned this week is that I'm glad we never standardized on an existing CSS framework. In fact, we've really avoided being dependent on any other project as much as possible with ProcessWire. Had we standardized on one CSS framework or another in the past, that would have greatly reduced our ability to support any CSS framework with tools like Form Builder. Hope that you enjoy these updates to Form Builder and related updates to the core.


### Screenshots

These are all screenshots of the same exact form, but with the framework switched for each screenshot.


## Uikit stacked form


## UIkit horizontal form


## Foundation stacked form


## Foundation horizontal form


## Bootstrap stacked form


## Bootstrap horizontal form


## Admin (Reno) form

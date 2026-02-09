# ProcessWire 3.0.69 plus Login for Facebook module

Source: https://processwire.com/blog/posts/pw-login-for-facebook/

## Sections


## ProcessWire 3.0.69 plus Login for Facebook module

28 July 2017 by Ryan Cramer [ 4 Comments](/blog/posts/pw-login-for-facebook/#comments)


### ProcessWire 3.0.69

This week's version of ProcessWire on the dev branch is 3.0.69 and it includes several minor bug fixes. For more details on that see the [dev branch commit log](https://github.com/processwire/processwire/commits/dev). This week we'll focus on a new module released today, which was actually developed for a friend of mine, but he gave me permission to release it. I'm thinking a lot of people might find this one quite useful.


## ProcessWire Login for Facebook

This is a new module for ProcessWire 3.x (3.0.42 or newer) that enables users to log-in to your ProcessWire site via their Facebook account. Once logged in, you can pull and use data from their Facebook account for output in your ProcessWire site. You can choose to have all Facebook logins map to the same user account, but the default behavior is to have it automatically create new ProcessWire user accounts for each Facebook user.


### Benefits

One of the benefits of using a Facebook login (or other social network logins, except maybe Twitter) is that such an account gives a certain level of legitimacy to a user, in that you know they have gone through the approval process of the social network. Another benefit is that it gives you the potential of accessing more information about the user without them having to manually enter it. Lastly, it saves a lot of time for the user when all they have to do is click once to approve the request (at Facebook) … no need for the user to enter the first name, last name, email, and so on.

This module was made possible thanks to to the direction and sponsorship of Michael Barón. He and I are working on other related modules as well. This module also takes some inspiration from an older module developed by Antti Peisa called FacebookLogin. Below we'll cover more details on how to install and use this module. Note that this module is fully functional but also still considered in beta, so use caution, test, and please let us know how it works for you.


### How it works

This module creates a new page named /login-facebook/, which you can move or rename as needed. When a user accesses this page, it asks them to login to Facebook. If they are already logged in to Facebook, it will ask them to approve access by clicking a button. Upon approval, they are redirected back to your site and are now logged in to ProcessWire with a user having the role “login-facebook”. If the user has not previously done this before, a new account will be created for them. The created account uses the name of their Facebook account. If preferred, you can also configure the module to use the same user for all Facebook logins.


### Installation


### Configuration

The module configuration screen gives you a lot of options, and I think the best way to highlight them is just to show a screenshot:


### Usage

When a user is logged in from Facebook, you can access properties from their Facebook information via the ProcessWire API. The fields that you want to work with are configured from the module configuration screen. As an example, lets say that you wanted to output a welcome message that contains the user's first name and picture, as stored in the Facebook data:

```
$facebook = $modules->get('LoginFacebook');  
echo "<h2>Welcome $facebook->first_name</h2>";
if($facebook->picture_url) {
  echo "<p><img src='$facebook->picture_url'></p>";
}
```

If you want to retrieve all user data, use the `getAll()` method, which returns an associative array of all Facebook data that you've configured for the module to retrieve.

```
$facebook = $modules->get('LoginFacebook');  
$data = $facebook->getAll();
```

In either case, any strings in the returned data are automatically entity encoded when the current page’s output formatting state is enabled.

When making API calls like above, if the user is not logged-in via Facebook, then it will automatically redirect to Facebook to log them in, and return to your page (where the API call exists) once logged in. If you would instead rather check if they are logged in via Facebook before outputting data, use the `isLoggedIn()` method:

```
$facebook = $modules->get('LoginFacebook');  
if($facebook->isLoggedIn()) {
  // user is logged in and Facebook data available
  echo "<h2>Welcome $facebook->first_name</h2>";
} else {
  // user not logged in via Facebook, ask them to login
  echo "<a href='$facebook->url'>Login with Facebook</a>";
}
```

This module also enables you to mirror data from Facebook to ProcessWire fields. This can add convenience, especially in cases where the user might be able to login through either ProcessWire or through Facebook. This ensures the Facebook data is stored in their ProcessWire user profile, even when not logged in via Facebook. This is useful for fields like email and names.

If you want to give this module a try, go ahead and [download it from GitHub](https://github.com/ryancramerdesign/LoginFacebook), and please let us know how it works for you. That's all for this week. Have a great weekend, read the [ProcessWire Weekly](http://weekly.pw), and we'll see you again next week!

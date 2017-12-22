## IntraPy
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

### Description
A python module to help make python apps/bots using the 42 API

### Installation
This python module uses `python-decouple` and `requests`. If you don't have 
them installed or don't know if they are installed, please run `pip install -r requirements.txt`

This module isn't available on `pip` yet. To install it, you will need to 
clone it 

### Usage
To use this module, you will need to create a `settings.ini` file in the root
 directory of your project containing the `UID` and `SECRET` provided by 42's
  API like so:

```
[settings]
APP_UID=XXX
APP_SECRET=XXX
```

This `settings.ini` file will be read by the init() function when called and,
 if the file `.app_token` doesn't exist, it will create it and fill it with 
 the app_token given by the API through `https://api.intra.42.fr/oauth/token`

For more information, See the [wiki pages](https://github.com/Seluj78/IntraPy/wiki)


### Contributing [![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

* Check for open issues or open a fresh issue to start a discussion around a feature idea or a bug.
* Fork [the repository](https://github.com/Seluj78/IntraPy) on GitHub to start making your changes to the **master** branch (or branch off of it).
* Write a test which shows that the bug was fixed or that the feature works as expected.
* Send a pull request and bug the maintainer until it gets merged and published. :) Make sure to add yourself to (AUTHORS)[https://github.com/Seluj78/IntraPy/blob/master/AUTHORS.rst].
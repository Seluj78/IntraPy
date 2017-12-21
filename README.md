### IntraPy
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)
 [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com) 
 
This python module uses `python-decouple` and `requests`. If you don't have 
them installed or don't know if they are installed, please run `pip install -r requirements.txt`

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
 the app_token given by 
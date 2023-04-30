# Application architecture

## High level of structure

```
.
└── {application_name}/
    ├── _config             Settings
    ├── _docs               Docs
    ├── modules             Application modules
    ├── static              Files css/js
    ├── app.py              Main file
    ├── README.md
    ├── requirements.txt    Installation requirements
    └── .env                Environment variables
```

## Module structure

```
.
└── {{application}}/
    ├── modules/
    │   ├── {{module}}/
    │   │   ├── controller/             Module controllers(endpoints)
    │   │   │   └── *_controller.py
    │   │   ├── model/                  Model Classes
    │   │   │   └── *.py
    │   │   ├── repository/             Module repository (database)
    │   │   │   └── *_repository.py
    │   │   ├── service/                Module services
    │   │   │   └── *_service.py
    │   │   └── template/               Module frontend(page, modal, etc.)
    │   │       └── *_pagel.html
    │   └── common/                     Common files for the project
    │       ├── responses.py
    │       └── utilities.py
    └── static/
        ├── assets/                     Project files(images, fonts and files)
        │   └── *.*
        └── {{module}}/                 Module files (css and js)
            ├── js/
            │   └── *.js
            └── css/
                └── *.js
```


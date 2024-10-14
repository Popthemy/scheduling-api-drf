# Implements the following models
> Any field that required the relationship to other models use a Charfield as a placeholder. check the usage of the `AUTH_USER_MODEL`. TO assign any model to user use this instead:

```python 
from django.conf import settings


User = settings.AUTH_USER_MODEL

    user = models.ForeignKey(User, on_delete=models.SET_CASCDE, null=True)

```

- `User`:  Concerns with authentication and authorization.
- `Staff`:  This is the profile for lecturer or non-teaching staff.
- `Student`:This is the profile for Reps or ordinary student.

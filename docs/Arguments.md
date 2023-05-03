# API Documentation - Arguments
# `module NWSh.arguments` - Ask for arguments
> Provides a set of functions to ask for arguments.
## `class NWSh.arguments.Arguments`
> A class to ask for arguments.
#### `def NWSh.arguments.Arguments.ask_argument(name, description, type)`
> Asks for arguments, with a name, a description and a type.\
Note: The type can be `string`, `int`, `float`. Conversion is done automatically.
#### `def NWSh.arguments.Arguments.get_argument(name)`
> Returns the value of the argument with the given name.
> If the argument is not found, returns `None` and prints an error message.
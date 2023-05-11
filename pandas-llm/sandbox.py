# sandbox.py
from RestrictedPython import compile_restricted
from RestrictedPython.Guards import safe_builtins,guarded_iter_unpack_sequence
from  RestrictedPython.Eval import default_guarded_getattr, default_guarded_getitem, default_guarded_getiter
import pandas as pd

class Sandbox:
    def __init__(self):
        self._allowed_imports = {}

    def allow_import(self, module_name):
        try:
            module = __import__(module_name)
            self._allowed_imports[module_name] = module
        except ImportError:
            pass

    def execute(self, code, local_vars = {}):
        allowed_builtins = safe_builtins
        # Add __builtins__, __import__, and allowed imports to the globals
        restricted_globals = {"__builtins__": allowed_builtins}
        restricted_globals.update(self._allowed_imports)

        builtin_mappings = {
            "__import__": __import__,
            "_getattr_": default_guarded_getattr,
            "_getitem_": default_guarded_getitem,
            "_getiter_": default_guarded_getiter,
            "_iter_unpack_sequence_": guarded_iter_unpack_sequence,
            "list": list,
            "set": set,
            "pd": pd,
        }

        series_methods = [
            "sum", "mean", "any", "argmax", "argmin", "count", "cumsum", "cumprod", "diff",
            "dropna", "fillna", "head", "idxmax", "idxmin", "last", "max", "min", "notna",
            "prod", "quantile", "rename", "round", "tail", "to_frame", "to_list", "to_numpy",
            "to_string","unique",  "sort_index", "sort_values", "aggregate"
        ]


        builtin_mappings.update({method: getattr(pd.Series, method) for method in series_methods})

        restricted_globals["__builtins__"].update(builtin_mappings)

        byte_code = compile_restricted(source=code, filename='<inline>', mode='exec')

        # Execute the restricted code
        exec(byte_code, restricted_globals, local_vars)

        return local_vars

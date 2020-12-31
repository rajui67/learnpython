'''
This is an exapmple of name mangling in Python.

In name mangling process, any identifier with two leading underscores and upto one trailing underscore is textually replaced with
 _<classname>__identifier where classname is the name of the current class
'''
import copy


class MangledMembers:
    __candidates = ('Ocean', 'Sea', 'Lake', 'Pond', 'Wetland', 'Puddle',
                    "Python mangles '__candidates' to '_MangledMembers__candidates'")
    __do_not_mangle_me_list__ = [1, 2, 3, 4,
                                 "Python will not mangle this list"]
    __do_not_mangle_me_dict__ = {
        "first": 1, "second": 2, "Other": "Python will not mangle this dict"}

    __python_mangles_this_ = ('identifier name begins with two underscores and ends with one underscore.'
                              "Python mangles '__python_mangles_this_' to '_MangledMembers__python_mangles_this_'")
    _single_underscore_prefix = 'identifier name begins with a single underscore. Python will not mangle this variable'
    single_underscore_suffix_ = 'identifier name ends  with a single underscore. Python will not mangle this variable'

    def __init__(self):
        pass
    
    def __mangled_method(self, message="Python mangles '__mangled_method' to '_MangledMembers__mangled_method'"):
        for key, value in self.locals_copy.items():
            # {'MangledMembers\n' if key.count('MangledMembers)}
            print(f"{'Python mangled this !' if key.count('MangledMembers') else ''}",
                  f'{key}:', value, "\n\n")

    locals_copy = copy.copy(locals())

    # dict expresion to filter out all dunder methods except dunders with mangle in their name
    locals_copy = {k: v for k, v in locals_copy.items() if not (
        k.startswith('__') and k.endswith('__')) or k.count('mangle')}


def main():

    mmi = MangledMembers()
    mmi._MangledMembers__mangled_method()
    for key, value in mmi.locals_copy.items():
        # {'MangledMembers\n' if key.count('MangledMembers)}
        print(f"{'Python mangled this !' if key.count('MangledMembers') else ''}",
              f'{key}:', value, "\n\n")


if __name__ == "__main__":
    main()

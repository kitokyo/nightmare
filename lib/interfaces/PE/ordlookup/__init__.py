import ws2_32

'''
A small module for keeping a database of ordinal to symbol
mappings for DLLs which frequently get linked without symbolic
infoz.
'''

ords = {
    'ws2_32.dll':ws2_32.ord_names,
    'wsock32.dll':ws2_32.ord_names,
}

def ordLookup(libname, ord):
    '''
    Lookup a name for the given ordinal if it's in our
    database.
    '''
    names = ords.get(libname.lower())
    if names == None:
        return 'ord%d' % ord
    name = names.get(ord)
    if name == None:
        return 'ord%d' % ord
    return name



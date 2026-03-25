"""Convert hyphenated key_name values to underscored Python attribute names.

linkml-runtime's _normalize_inlined_as_list looks up attributes by key_name on
already-constructed Python objects, which use underscored names (e.g. role_id
not role-id). The generated code emits the original hyphenated OSCAL names.
"""
import re
import sys

filepath = sys.argv[1]
content = open(filepath).read()
content = re.sub(
    r'key_name="([^"]+)"',
    lambda m: 'key_name="' + m.group(1).replace('-', '_') + '"',
    content,
)
open(filepath, 'w').write(content)

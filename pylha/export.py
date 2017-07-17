import collections
import yaml
import json

# the following is necessary to get pretty representations of
# OrderedDict and defaultdict instances in YAML
def _represent_dict_order(self, data):
    return self.represent_mapping('tag:yaml.org,2002:map', data.items())

yaml.add_representer(collections.OrderedDict, _represent_dict_order)
yaml.add_representer(collections.defaultdict, _represent_dict_order)

def dump(d, fmt='json', stream=None):
    """Serialize structured data into a stream in JSON, YAML, or LHA format.
    If stream is None, return the produced string instead.

    Parameters:
    - fmt: should be 'json' (default), 'yaml', or 'lha'
    - stream: if None, return string
    """
    if fmt == 'json':
        return _dump_json(d, stream=stream)
    elif fmt == 'yaml':
        return yaml.dump(d, stream)
    elif fmt == 'lha':
        s = _dump_lha(d)
        if stream is None:
            return s
        else:
            return stream.write(s)

def _dump_json(d, stream=None):
    if stream is not None:
        return json.dump(d, stream)
    else:
        return json.dumps(d)

def _dump_lha(d):
    s = ""
    for blocktype, blocks in d.items():
        for blockname, block in blocks.items():
            s += '{} {}'.format(blocktype, blockname)
            if 'info' in block:
                s += ' ' + ' '.join(str(e) for e in block['info'])
            s += '\n'
            for value in block['values']:
                s += '    ' + '    '.join(str(e) for e in value)
                s += '\n'
    return s

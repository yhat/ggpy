from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from ..ggplot import ggplot
from ..aes import aes

class geom(object):
    _aes_renames = {}
    DEFAULT_AES = {}
    REQUIRED_AES = {}

    def __init__(self, *args, **kwargs):
        self.layers = [self]
        self.params = kwargs
        self.geom_aes = None
        
        if len(args) > 0:
            if isinstance(args[0], aes):
                self.geom_aes = args[0]

        self.VALID_AES = set()
        self.VALID_AES.update(self.DEFAULT_AES.keys())
        self.VALID_AES.update(self.REQUIRED_AES)
        self.VALID_AES.update(self._aes_renames.keys())

    def __radd__(self, gg):
        if isinstance(gg, ggplot):
            gg.layers += self.layers
            return gg

        self.layers.append(gg)
        return self

    def _rename_parameters(self, params):
        pass

    def _update_data(self, data, _aes):
        if 'mapping' in self.params:
            _aes = self.params['mapping']
            if not 'data' in self.params:
                data = _aes._evaluate_expressions(data)
                data = _aes.handle_identity_values(data)
        if 'data' in self.params:
            data = _aes._evaluate_expressions(self.params['data'])
            data = _aes.handle_identity_values(data)
        
        return (data, _aes)

    def _get_plot_args(self, data, _aes):
        mpl_params = {}
        mpl_params.update(self.DEFAULT_AES)

        # handle the case that the geom has overriding aes passed as an argument
        if self.geom_aes:
            _aes.update(self.geom_aes)

        # for non-continuous values (i.e. shape), need to only pass 1 value
        # into matplotlib. for example instead if ['+', '+', '+', ..., '+'] you'd
        # want to pass in '+'
        for key, value in _aes.items():
            if value not in data:
                mpl_params[key] = value
            elif data[value].nunique()==1:
                mpl_params[key] = data[value].iloc[0]
            else:
                mpl_params[key] = data[value]

        # parameters passed to the geom itself override the aesthetics
        mpl_params.update(self.params)

        items = list(mpl_params.items())
        for key, value in items:
            
            if key not in self.VALID_AES:
                del mpl_params[key]
            elif key in self._aes_renames:
                new_key = self._aes_renames[key]
                mpl_params[new_key] = value
                del mpl_params[key]

        for req in self.REQUIRED_AES:
            if req not in mpl_params:
                raise Exception("%s needed for %s" % (req, str(self)))
            else:
                del mpl_params[req]

        for key, value in self.DEFAULT_PARAMS.items():
            if key not in self.params:
                self.params[key] = value

        return mpl_params

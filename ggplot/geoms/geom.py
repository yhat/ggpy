from ..ggplot import ggplot

class geom(object):
    _aes_renames = {}
    DEFAULT_AES = {}
    REQUIRED_AES = {}

    def __init__(self, **kwargs):
        self.layers = [self]
        self.params = kwargs

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

    def _get_plot_args(self, data, _aes):
        mpl_params = {}
        mpl_params.update(self.DEFAULT_AES)

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

        return mpl_params

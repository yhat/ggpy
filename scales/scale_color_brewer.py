import seaborn as sns


class scale_color_brewer(object):

    def __radd__(self, other):
        if other.__class__.__name__=="ggplot":
            other.scales.append(self)
            return other

        return self

    def apply(self):
        sns.set_palette(sns.color_palette("Paired"))

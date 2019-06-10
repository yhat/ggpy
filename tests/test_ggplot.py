import unittest
import ggplot as gg
import pandas as pd

class TestGgplot(unittest.TestCase):
    def test_init_args_order(self):
        p = gg.ggplot(gg.mtcars, gg.aes(x='mpg'))
        self.assertTrue(isinstance(p.data, pd.DataFrame))
        self.assertTrue(isinstance(p._aes, gg.aes))

    def test_init_args_backwards_order(self):
        p = gg.ggplot(gg.aes(x='mpg'), gg.mtcars)
        self.assertTrue(isinstance(p.data, pd.DataFrame))
        self.assertTrue(isinstance(p._aes, gg.aes))

    # facets
    def test_ndim_2facet_grid(self):
        p = gg.ggplot(gg.aes(x='price'), gg.diamonds) + gg.facet_grid('cut', 'clarity')
        nrow, ncol = p.facets.nrow, p.facets.ncol
        self.assertEqual(nrow, 5)
        self.assertEqual(ncol, 8)

    def test_ndim_2facet_grid_reverse(self):
        p = gg.ggplot(gg.aes(x='price'), gg.diamonds) + gg.facet_grid('clarity', 'cut')
        nrow, ncol = p.facets.nrow, p.facets.ncol
        self.assertEqual(nrow, 8)
        self.assertEqual(ncol, 5)

    def test_ndim_1_facet_grid_row(self):
        p = gg.ggplot(gg.aes(x='price'), gg.diamonds) + gg.facet_grid('clarity')
        nrow, ncol = p.facets.nrow, p.facets.ncol
        self.assertEqual(nrow, 8)
        self.assertEqual(ncol, 1)

    def test_ndim_1_facet_grid_col(self):
        p = gg.ggplot(gg.aes(x='price'), gg.diamonds) + gg.facet_grid(None, 'clarity')
        nrow, ncol = p.facets.nrow, p.facets.ncol
        self.assertEqual(nrow, 1)
        self.assertEqual(ncol, 8)

    def test_ndim_1_facet_wrap(self):
        p = gg.ggplot(gg.aes(x='price'), gg.diamonds) + gg.facet_wrap('clarity')
        nrow, ncol = p.facets.nrow, p.facets.ncol
        self.assertEqual(nrow, 3)
        self.assertEqual(ncol, 3)
        self.assertEqual(p.facets.ndim, 8)

    def test_ndim_1_facet_wrap_subplots(self):
        p = gg.ggplot(gg.aes(x='price'), gg.diamonds) + gg.facet_wrap('clarity')
        fig, subplots = p.make_facets()
        nrow, ncol = subplots.shape
        self.assertEqual(nrow, 3)
        self.assertEqual(ncol, 3)

    def test_ndim_2_facet_wrap(self):
        p = gg.ggplot(gg.aes(x='price'), gg.diamonds) + gg.facet_wrap('cut', 'clarity')
        nrow, ncol = p.facets.nrow, p.facets.ncol
        self.assertEqual(nrow, 7)
        self.assertEqual(ncol, 6)
        self.assertEqual(p.facets.ndim, 40)

    def test_ndim_2_facet_wrap_subplots(self):
        p = gg.ggplot(gg.aes(x='price'), gg.diamonds) + gg.facet_wrap('cut', 'clarity')
        fig, subplots = p.make_facets()
        nrow, ncol = subplots.shape
        self.assertEqual(nrow, 7)
        self.assertEqual(ncol, 6)

    def test_facet_wrap_nrow(self):
        p = gg.ggplot(gg.aes(x='price'), gg.diamonds) + gg.facet_wrap('cut', nrow=2)
        nrow, ncol = p.facets.nrow, p.facets.ncol
        self.assertEqual(nrow, 2)
        self.assertEqual(ncol, 3)

    def test_facet_wrap_ncol(self):
        p = gg.ggplot(gg.aes(x='price'), gg.diamonds) + gg.facet_wrap('cut', ncol=2)
        nrow, ncol = p.facets.nrow, p.facets.ncol
        self.assertEqual(nrow, 3)
        self.assertEqual(ncol, 2)

    # groups
    def test_groups_1_aes(self):
        p = gg.ggplot(gg.aes(x='carat', y='price', color='clarity'), gg.diamonds) + gg.geom_point()
        _, groups = p._construct_plot_data()
        self.assertEqual(len(groups), 8)

    def test_groups_2_aes(self):
        p = gg.ggplot(gg.aes(x='carat', y='price', color='clarity', shape='cut'), gg.diamonds) + gg.geom_point()
        _, groups = p._construct_plot_data()
        self.assertEqual(len(groups), 8*5)

    # labels
    def test_xlab(self):
        p = gg.ggplot(gg.aes(x='mpg'), gg.mtcars) + gg.geom_histogram() + gg.xlab("TEST")
        self.assertEqual(p.xlab, "TEST")

    def test_ylab(self):
        p = gg.ggplot(gg.aes(x='mpg'), gg.mtcars) + gg.geom_histogram() + gg.ylab("TEST")
        self.assertEqual(p.ylab, "TEST")

    def test_ggtitle(self):
        p = gg.ggplot(gg.aes(x='mpg'), gg.mtcars) + gg.geom_histogram() + gg.ggtitle("TEST")
        self.assertEqual(p.title, "TEST")

    # patsy formula
    def test_patsy(self):
        p = gg.ggplot(gg.aes(x='mpg + 100'), gg.mtcars)
        self.assertEqual((p.data['mpg + 100']==(gg.mtcars.mpg + 100)).sum(), 32)

    # scales
    def test_scale_x_log_default10(self):
        p = gg.ggplot(gg.aes(x='mpg'), gg.mtcars) + gg.scale_x_log()
        self.assertEqual(p.scale_x_log, 10)

    def test_scale_x_log_base(self):
        p = gg.ggplot(gg.aes(x='mpg'), gg.mtcars) + gg.scale_x_log(base=100)
        self.assertEqual(p.scale_x_log, 100)

    def test_scale_y_log_default10(self):
        p = gg.ggplot(gg.aes(x='mpg'), gg.mtcars) + gg.scale_y_log()
        self.assertEqual(p.scale_y_log, 10)

    def test_scale_y_log_base(self):
        p = gg.ggplot(gg.aes(x='mpg'), gg.mtcars) + gg.scale_y_log(base=100)
        self.assertEqual(p.scale_y_log, 100)

    def test_scale_alpha_identity(self):
        df = pd.DataFrame({'x': range(10), 'the-alpha': '+' })
        p = gg.ggplot(gg.aes(x='x', alpha='the-alpha'), df) + gg.scale_alpha_identity()
        self.assertTrue((p.data['the-alpha'] == df['the-alpha']).all())

    def test_scale_color_identity(self):
        df = pd.DataFrame({'x': range(10), 'the-color': 'blue' })
        p = gg.ggplot(gg.aes(x='x', color='the-color'), df) + gg.scale_color_identity()
        self.assertTrue((p.data['the-color'] == df['the-color']).all())

    def test_scale_fill_identity(self):
        df = pd.DataFrame({'x': range(10), 'the-fill': '+' })
        p = gg.ggplot(gg.aes(x='x', fill='the-fill'), df) + gg.scale_fill_identity()
        self.assertTrue((p.data['the-fill'] == df['the-fill']).all())

    def test_scale_linetype_identity(self):
        df = pd.DataFrame({'x': range(10), 'the-linetype': '+' })
        p = gg.ggplot(gg.aes(x='x', linetype='the-linetype'), df) + gg.scale_linetype_identity()
        self.assertTrue((p.data['the-linetype'] == df['the-linetype']).all())

    def test_scale_shape_identity(self):
        df = pd.DataFrame({'x': range(10), 'the-shape': '+' })
        p = gg.ggplot(gg.aes(x='x', shape='the-shape'), df) + gg.scale_shape_identity()
        self.assertTrue((p.data['the-shape'] == df['the-shape']).all())

    def test_scale_size_identity(self):
        df = pd.DataFrame({'x': range(10), 'the-size': '+' })
        p = gg.ggplot(gg.aes(x='x', size='the-size'), df) + gg.scale_size_identity()
        self.assertTrue((p.data['the-size'] == df['the-size']).all())

    def test_scale_x_reverse(self):
        df = pd.DataFrame({'x': range(10), 'the-size': '+' })
        p = gg.ggplot(gg.aes(x='x', size='the-size'), df) + gg.scale_x_reverse()
        self.assertTrue(p.scale_x_reverse)

    def test_scale_y_reverse(self):
        df = pd.DataFrame({'x': range(10), 'the-size': '+' })
        p = gg.ggplot(gg.aes(x='x', size='the-size'), df) + gg.scale_y_reverse()
        self.assertTrue(p.scale_y_reverse)


    # TODO legend tests

if __name__ == '__main__':
    unittest.main()

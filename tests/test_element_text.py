from ggplot import *

txt = element_text(
    "Hello!\nThis\nIs\nGreg",
    face="bold",
    hjust=-.2,
    vjust=-.02,
    angle=45,
    color="coral",
    lineheight=1.15,
    family="monospace",
    size=17
)

newTxt = element_text(
    "this is my X!!!!!",
    face="bold",
    color="cyan"
)

myY = element_text("WOO!", face="bold", color="red")

# print ggplot(mtcars, aes(x='mpg')) + geom_histogram() + theme(axis_text=element_text(size=20))
# print ggplot(mtcars, aes(x='mpg')) + geom_histogram() + theme(x_axis_text=element_text(color="orange"), y_axis_text=element_text(color="blue"))
# print ggplot(mtcars, aes(x='mpg')) + geom_histogram() + theme(axis_text=element_text(size=20), x_axis_text=element_text(color="orange"), y_axis_text=element_text(color="blue"))
print ggplot(mtcars, aes(x='mpg')) + geom_histogram() + theme(plot_title=txt, axis_title_x=newTxt, axis_title_y=myY)
print ggplot(mtcars, aes(x='mpg')) + geom_histogram() + theme(title=txt, xlab=newTxt, ylab=myY)
# print ggplot(mtcars, aes(x='mpg')) + geom_histogram() + facet_wrap("cyl") + theme(title=txt, xlab=newTxt, ylab=myY)
# print ggplot(mtcars, aes(x='mpg')) + geom_histogram() + ggtitle("Hello!")

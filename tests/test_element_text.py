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

print ggplot(mtcars, aes(x='mpg')) + geom_histogram() + theme(title=txt, xlab=newTxt, ylab=myY)
print ggplot(mtcars, aes(x='mpg')) + geom_histogram() + ggtitle("Hello!")

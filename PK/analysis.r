library(dplyr)

df <- read.csv("../data/music.csv")

df.cont <- df %>% select(-carti)

pca <- prcomp(df.cont, scale=TRUE)

pca.df <- pca$x %>% data.frame()
pca.df$carti <- df$carti

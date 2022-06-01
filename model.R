install.packages('devtools')
devtools::install_github("mhtess/rwebppl")

setwd("~/codenames_rsa")

# load in the trimmed file as a df
data = readLines("25d_trimmed.txt")
data = as.data.frame(do.call(rbind, strsplit(data, split=" ")), stringsAsFactors = FALSE)
names(data) = c("word", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24")

# grab a random sample of rows (essentially uniformDraw)
random_sample <- data[sample(1:nrow(data), 25), ]



# test model to see if the library was working
my_model <- "
  var model = function () {
    var choice = uniformDraw(myDF)
    console.log(choice)
}
model()
"

rwebppl::webppl(my_model,
       data = data,
       data_var = "myDF")

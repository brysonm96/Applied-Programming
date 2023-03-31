#change directory
setwd("C:/Users/bryso/Documents/School/Applied Programming/Sprint 6")

#get CSV file
data <- read.csv("grocery_products.csv")

#search product function
search <- function(product_name) {
  
  product_rows <- which(data$Product_Name == product_name)
  
  #error message
  if (length(product_rows) == 0) {
    return(paste("No results found for", product_name))
  }
  
  #show information
  for (i in product_rows) {
    cat("\nProduct Name:", data[i, "Product_Name"])
    cat("\nPrice:", data[i, "Price"])
    cat("\nCategory:", data[i, "Category"])
    cat("\nID:", data[i, "ID"], "\n")
  }
}

#loop until done
while (TRUE) {
  #prompt the user
  product_name <- readline(prompt = "Enter a product name to search for (or type 'Finish' to exit): ")
  
  #if finished, exit loop
  if (product_name == "Finish") {
    break
  }
  
  #call the function with user input
  result <- search(product_name)
  
  #print result
  cat(result, "\n")
}

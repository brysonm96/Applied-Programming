grocery_list <- list()

#the loop
while (TRUE) {
  input <- readline(prompt = "Enter 'a' to add an item, 'r' to remove an item, or 'f' to finish: ")

  #finish
  if (input == "f") {
    
    break
    #add
  } else if (input == "a") {
    
    item <- readline(prompt = "Enter the name of the item you want to add to your grocery list: ")
    
    grocery_list <- c(grocery_list, item)
  } else if (input == "r") {
    #display grocery items 
    cat("Grocery list:\n")
    for (i in 1:length(grocery_list)) {
      cat(i, "-", grocery_list[[i]], "\n")
    }
    #the index input becomes the item removed
    index <- as.numeric(readline(prompt = "Enter the index of the item you want to remove: "))
    
    removed_item <- grocery_list[[index]]
    grocery_list <- grocery_list[-index]
    cat(paste("Removed item:", removed_item, "\n"))
  } else {

    #didn't recognize the input
    cat("Invalid input. Please enter 'a' to add, 'r' to remove, or 'f' to finish.\n")
  }
}

#display grocery list
cat("Final grocery list:\n")
if (length(grocery_list) > 0) {
  for (i in 1:length(grocery_list)) {
    cat(i, "-", grocery_list[[i]], "\n")
  }
} else {
  #if items are not greater than 0, displays no items
  cat("No items in the grocery list.\n")
}

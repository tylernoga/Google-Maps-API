NORTHEAST_LAT <- 40.881996 #Lat for NE Most point in NYC
NORTHEAST_LNG <- -73.796311 #LNG for NE Most point in NYC
SOUTHWEST_LAT <- 40.496974 #LAT for SE Most point in NYC
SOUTHWEST_LNG <- -74.256181 #LNG for SE Most point in NYC

DESIRED_GRID_LENGTH <- 10 #Create a 10x10 grid (100) unique ordinates
output <- c()
epsilon <- 0.0000001
intermediate_grid_length <- DESIRED_GRID_LENGTH - 1

lat_step_size <- (NORTHEAST_LAT - SOUTHWEST_LAT) / intermediate_grid_length
lng_step_size <- (NORTHEAST_LNG - SOUTHWEST_LNG) / intermediate_grid_length

for (lat in seq(SOUTHWEST_LAT - epsilon, NORTHEAST_LAT + epsilon, lat_step_size)) {
  for (lng in seq(SOUTHWEST_LNG - epsilon, NORTHEAST_LNG + epsilon, lng_step_size)) {
    output <- c(output, sprintf("%f,%f", lat, lng))
  }
}

cat(paste(output, collapse = ", "))
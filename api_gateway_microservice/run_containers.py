import os, time

# For debugging, should work at same time as setup_db
print("This is run_containers")

time.sleep(5)

print("special waited 5")

# spin up the db_server containers
#os.system("docker-compose up db_server")

# eventually this would be reading the output lines from the above command and
# when it sees that the dbsetup has completed it will kill db container

# spin up containers
# will print the test results
#os.system("docker-compose up)

# eventually this would be reading the output lines from the above command and
# when it sees tests have run successfully it will kill the container

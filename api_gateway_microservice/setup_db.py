import os, time

# For debugging, should work at same time as setup_db
print("this is setup_db")

time.sleep(7)

print("other_special waited 7")


# waits for the db_server to finish spinning up
#time.sleep(200)

# runs dbsetup while db_server is up and running
#os.system("bash dbsetup")
# Database Configuration

  

1. Run `docker pull postgres` to get the postgres docker image

2. Go back to api_gateway_microservice directory and run 'docker-compose up db_server'

3. Once the postgres container is spinned up - Open a new terminal in this directory

4. Run 'bash Scripts/Dbsetup'

	- This script does the following:

		1. Creates Pet Database

		2. Creates User Database

		3. Runs a python script to initialize petTable Schema and insert values

		4. Runs a python script to initialize user Schema and insert values

  

## TESTING DATABASE CONNECTION

1. Make sure the postgres container is spinned up and listening to calls

2. Also make sure that bash Dbsetup completed correctly

3. Run 'Python Scripts/testconnection.py'
	- This python file makes a select all on petTable schema. Should return 10 pets that were added.

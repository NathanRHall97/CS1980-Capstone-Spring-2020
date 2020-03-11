## How to use:
1. Install requirements from root folder Documentation `pip install -r requirements.txt`
2. from `codegen_example` directory, run server generator `python server_generator.py`
3. server generator will create a generated flask server file `generated_server.py`--run that server with `python generated_server.py`

## example:
```
charlie@KINKADE02-PC:codegen_example> python3 server_generator.py
Reading in server mustache template...
Reading in API documentation...
Parsing API operations...
Generating server code...
Writing server code to file...
All done!
charlie@KINKADE02-PC:codegen_example> ls
generated_server.py  mogwai.yaml  README  server_generator.py  templates
charlie@KINKADE02-PC:codegen_example> python3 generated_server.py
 * Serving Flask app "generated_server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

```

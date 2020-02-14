# Choosing a Python Test Framework

<h3>Options</h3>

When looking to select a Python test framework for this project, we considered 3 options.

1. Robot <br/>

	Pros:
	 - Keyword driven testing allows for highly readable test cases.
	 - Highly extensible with many APIs.
	 - Tabular data syntax makes structure visually appealing and intuitive. <br/>
	 
	Cons:
	 - Have to 'learn' new testing style.
	 - Inadequate parallel testing.
2. Pytest <br/>

	Pros:
	 - Very compact test suites.
	 - Simple syntax.
	 - Highly compatible with docker <br/>
	 
	Cons:
	 - Since pytest uses special routines, pytest is not compatible with any other testing frameworks.
3. Unittest (PyUnit) <br/>

	Pros:
	 - Similar to JUnit testing framework (we are familiar with).
	 - Output is produced very quickly and is concise.
	 - Flexible framework. <br/>
	 
	Cons:
	 - Less readable.
	 - Long and very specific test cases required.

For this project we agreed that due to its extra Docker support and compact test suites, Pytest is the best option for our test framework.

<h3>Our Selection: Pytest</h3>

<h3>Pytest Documentation</h3>

Here is the link to the [Pytest Documentation](https://docs.pytest.org/en/latest/contents.html). Any questions regarding the usage of the Pytest testing framework should be referred to this link.

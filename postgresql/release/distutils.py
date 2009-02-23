##
# copyright 2009, James William Pye
# http://python.projects.postgresql.org
##
"""
Python distutils data provisions module.

For sub-packagers, the `prefixed_packages` and `prefixed_extensions` functions
should be of particular interest. It is not recommended that sub-packagers
include the `scripts` keyword from py-postgresql in their setup() call.
If the distribution including ``py-postgresql`` uses the standard layout,
chances are that `prefixed_extensions` and `prefixed_packages` will supply the
appropriate information by default as they use `default_prefix` which is derived
from the module's `__package__`.
"""
import sys
import os
from .. import \
	__version__ as version, \
	__project__ as name, \
	__project_id__ as url
from distutils.core import Extension

LONG_DESCRIPTION = """
py-postgresql is a set of Python modules providing interfaces to various parts
of PostgreSQL. Notably, it provides a driver for querying a PostgreSQL database.

Sample PG-API Code
------------------

	>>> import postresql.driver as pg_driver
	>>> db = pg_driver.connect(user = 'mydbuser', host = 'localhost', port = 5432, database = 'mydbname')
	>>> db.execute("CREATE TABLE emp (emp_first_name text, emp_last_name text, emp_salary numeric)")
	>>> make_emp = db.prepare("INSERT INTO emp VALUES ($1, $2, $3)")
	>>> make_emp("John", "Doe", "75,322")
	>>> with db.xact:
	...  make_emp("Jane", "Doe", "75,322")
	...  make_emp("Edward", "Johnson", "82,744")
	...

There is a DB-API 2.0 module as well::

	postgresql.driver.dbapi20

However, PG-API is recommended as it provides greater utility.

Once you get it installed, try out the ``pg_python`` command::

	$ pg_python -h localhost -U theuser -d database_name

That should give you a Python console with the database connection bound to the
`db` name.

History
-------

py-postgresql is not yet another PostgreSQL driver, it's been in development for
years. py-postgresql is the Python 3.0 port of the ``pg_proboscis`` driver and
integration of the other ``pg/python`` projects.


More Information
----------------

http://python.projects.postgresql.org
"""

CLASSIFIERS = [
	'Development Status :: 5 - Production/Stable',
	'Intended Audience :: Developers',
	'License :: OSI Approved :: BSD License',
	'License :: OSI Approved :: MIT License',
	'License :: OSI Approved :: Attribution Assurance License',
	'License :: OSI Approved :: Python Software Foundation License',
	'Natural Language :: English',
	'Operating System :: OS Independent',
	'Programming Language :: Python',
	'Programming Language :: Python :: 3',
	'Topic :: Database',
]

subpackages = [
	'bin',
	'encodings',
	'protocol',
	'driver',
	'test',
	'documentation',
	'python',
	'release',
	# Modules imported from other packages.
	'resolved',
]
extensions_data = {
	'protocol.cbuffer' : {
		'sources' : [os.path.join('protocol', 'buffer.c')],
		'libraries' : (sys.platform == 'win32' and ['ws2_32'] or []),
	}
}

scripts = [
	'postgresql/bin/pg_dotconf',
	'postgresql/bin/pg_python',
	'postgresql/bin/pg_tin',
	'postgresql/bin/pg_withcluster'
]

try:
	# :)
	if __package__ is not None:
		default_prefix = __package__.split('.')[:-1]
	else:
		default_prefix = __name__.split('.')[:-2]
except NameError:
	default_prefix = ['postgresql']

def prefixed_extensions(
	prefix : "prefix to prepend to paths" = default_prefix,
	extensions_data : "`extensions_data`" = extensions_data,
) -> [Extension]:
	"""
	Generator producing the `distutils` `Extension` objects.
	"""
	pkg_prefix = '.'.join(prefix) + '.'
	path_prefix = os.path.sep.join(prefix)
	for mod, data in extensions_data.items():
		yield Extension(
			pkg_prefix + mod,
			[os.path.join(path_prefix, src) for src in data['sources']],
			libraries = data['libraries']
		)

def prefixed_packages(
	prefix : "prefix to prepend to source paths" = default_prefix,
	packages = subpackages,
):
	"""
	Generator producing the standard `package` list prefixed with `prefix`.
	"""
	prefix = '.'.join(prefix)
	yield prefix
	prefix = prefix + '.'
	for pkg in packages:
		yield prefix + pkg

def standard_setup_keywords(build_extensions = True, prefix = default_prefix):
	"""
	Used by the py-postgresql distribution.
	"""
	d = {
		'name' : name,
		'version' : version,
		'description' : 'PostgreSQL tools pacakges. Driver, API specifications, and cluster tools.',
		'long_description' : LONG_DESCRIPTION,
		'author' : 'James William Pye',
		'author_email' : 'x@jwp.name',
		'maintainer' : 'James William Pye',
		'maintainer_email' : 'python-general@pgfoundry.org',
		'url' : url,
		'classifiers' : CLASSIFIERS,
		'packages' : list(prefixed_packages(prefix = prefix)),
		'scripts' : scripts,
	}
	if build_extensions:
		d['ext_modules'] = list(prefixed_extensions(prefix = prefix))
	return d
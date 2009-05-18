##
# copyright 2009, James William Pye
# http://python.projects.postgresql.org
##
r"""
Changes
=======

0.9.0
-----

 * Extend `postgresql.open` to take keyword arguments.
 * Implement query libraries and connection categories[#1010581 & #1010618].
 * Implement ``clone()`` on Connections, Statements, and Cursors.
 * Refactor ``ps.load()`` into ``ps.load_chunks()`` and ``ps.load_rows()``.
 * Performance optimizations.
 * Refactor `postgresql.api.InterfaceElement`.
 * Refactor driver.pq3.Connection to use protocol.client3.Connection.
 * Refactor driver.pq3.Cursor into types selected by PreparedStatements.
 * Fix memory leak due to circular references and __del__. [Reported by Valentine Gogichashvili]
   Additionally, try to avoid circular references at that level.

0.8.1 released on 2009-04-30
----------------------------

 * Fix memory leak due to circular references and __del__. [Reported by Valentine Gogichashvili]
 * Fix encoding normalization. [Reported by Marc Silver]
 * Fix "method" decorator to return callable when val is None.
 * Fix startup of clusters in silent mode.

0.8.0 released on 2009-04-03
----------------------------

Differences from the original pg/python projects.

 * Integrate projects into a single package. Remove "codenames".
 * pg_greentrunk evolved into PG-API, postgresql.api.
 * Add new execution methods to statement objects: chunks, rows, declare.
 * Refactor connection negotiation code to use a generator. (xact3.Negotiation)
 * Remove sixbit confusion from postgresql.exceptions.
 * Integrate fcrypt module for crypt authentication.
 * Remove pytz dependency, always use UTC for timestamptz.
 * Remove netaddr dependency.
 * Improve DB-API interface by allowing subjective paramstyle. (psycopg2 compat)
 * Provide autocommit support on DB-API connections.
 * Add support for binary numeric.
 * Add proper support for sslmode and connect_timeout.
 * Conditionally DECLARE certain cursors WITH HOLD when outside of blocks.
 * Add typed support for fetches from db.cursor_from_id().
 * Change the test infrastructure to automatically create a cluster.
 * More improvements than I can remember.
"""

__docformat__ = 'reStructuredText'
if __name__ == '__main__':
	import sys
	if (sys.argv + [None])[1] == 'dump':
		sys.stdout.write(__doc__)
	else:
		try:
			help(__package__ + '.index')
		except NameError:
			help(__name__)

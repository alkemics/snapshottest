# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc

from snapshottest import Snapshot



snapshots = Snapshot()

snapshots['TestPyTestSnapShotTest.test_property_test_name 1'] = 'counter'

snapshots['TestPyTestSnapShotTest.test_property_test_name named_test'] = 'named'

snapshots['TestPyTestSnapShotTest.test_property_test_name 2'] = 'counter'

snapshots['test_pytest_snapshottest_property_test_name 1'] = 'counter'

snapshots['test_pytest_snapshottest_property_test_name named_test'] = 'named'

snapshots['test_pytest_snapshottest_property_test_name 2'] = 'counter'

# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['test_me_endpoint 1'] = {
    'url': '/me'
}

snapshots['test_unicode 1'] = u'p\xe9p\xe8re'

snapshots['test_datetime 1'] = GenericRepr(datetime.datetime(2017, 11, 19, 0, 0))

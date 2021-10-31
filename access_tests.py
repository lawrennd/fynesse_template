#!/usr/bin/env python

import nose, warnings

# THese tests should be checking the known access problems, such as whether an excel file has turned a gene to a date or has more than 1,048,576 rows.
nose.main("fynesse", defaultTest="fynesse/tests/access", argv=["", ""])

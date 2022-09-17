from PySide6 import QtCore

qt_resource_data = b"\
\x00\x00\x01i\
<\
svg xmlns=\x22http:\
//www.w3.org/200\
0/svg\x22 height=\x224\
8\x22 width=\x2248\x22><p\
ath d=\x22M15.2 40.\
2q-1.4 0-2.375-.\
975-.975-.975-.9\
75-2.375v-25.4h-\
2V9.7h7.9V8.25H3\
0.3V9.7h7.9v1.75\
h-2v25.4q0 1.35-\
.975 2.35t-2.375\
 1Zm19.25-28.75H\
13.6v25.4q0 .7.4\
75 1.15.475.45 1\
.125.45h17.65q.6\
 0 1.1-.5.5-.5.5\
-1.1ZM19.7 34.3h\
1.75V15.5H19.7Zm\
6.95 0h1.75V15.5\
h-1.75ZM13.6 11.\
45V38.45 36.85Z\x22\
/></svg>\
"

qt_resource_name = b"\
\x00\x04\
\x00\x06\xfa^\
\x00i\
\x00c\x00o\x00n\
\x00\x0c\
\x09>\x92\x07\
\x00i\
\x00c\x00o\x00n\x00_\x00n\x00e\x00w\x00.\x00s\x00v\x00g\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x0e\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x83KF<\x88\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()

{
	'targets': [
	{
		'target_name': 'brig',
		'sources': [
			'src/brig.cc',
			'src/eventdispatcher/eventdispatcher.cc',
			'src/qapplication.cc',
			'src/eventloop.cc',
			'src/qobject.cc',
			'src/qmlengine.cc',
			'src/qmlcontext.cc',
			'src/qmlcomponent.cc',
			'src/quickview.cc',
			'src/quickwindow.cc',
			'<!@(tools/genmoc.sh)'
		],
		'conditions': [
			['OS=="linux"', {
				'cflags': [
					'-std=c++11',
					'<!@(pkg-config --cflags Qt5Core Qt5Quick Qt5Qml Qt5Multimedia)'
				],
				'ldflags': [
					'<!@(pkg-config --libs-only-L --libs-only-other Qt5Core Qt5Quick Qt5Qml Qt5Multimedia)'
				],
				'libraries': [
					'<!@(pkg-config --libs-only-l Qt5Core Qt5Quick Qt5Qml Qt5Multimedia)'
				]
			}]        
		]
	}
	]
}

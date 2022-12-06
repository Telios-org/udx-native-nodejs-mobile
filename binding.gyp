{
  'targets': [{
    'target_name': 'udx',
    'include_dirs': [
      "<!(node -e \"require('napi-macros')\")",
    ],
    'sources': [
      './src/cirbuf.c',
      './src/endian.c',
      './src/fifo.c',
      './src/udx.c',
      './binding.c',
    ],
    'configurations': {
      'Debug': {
        'defines': ['DEBUG'],
      },
      'Release': {
        'defines': ['NDEBUG'],
      },
    },
    'conditions': [
      ['OS=="android" or OS=="ios"', {
        'cflags': ['-fPIC'],
        'ldflags': ['-fPIC']
      }, {
        # Refuse to build anything if OS is not android or iOS
        'type': "none"
      }],
    ],
    'xcode_settings': {
      'OTHER_CFLAGS': [
        '-O3',
      ]
    },
    'cflags': [
      '-O3',
    ],
  }]
}

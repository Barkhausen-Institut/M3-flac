def build(gen, env):
    env = env.clone()

    env['CPPFLAGS'] += ['-DHAVE_CONFIG_H', '-DFLAC__NO_DLL']
    env['CPPPATH'] += [
        'src/libs/flac',
        'src/libs/flac/src/libFLAC++',
        'src/libs/flac/src/libFLAC++/include',
        'src/libs/flac/src/libFLAC',
        'src/libs/flac/src/libFLAC/include',
        'src/libs/flac/include',
    ]

    # shut off warnings
    env['CFLAGS'] += [
        '-Wno-sign-conversion',
        '-Wno-incompatible-pointer-types',
        '-Wno-format',
    ]

    files = [
        'src/libFLAC++/metadata.cpp',
        'src/libFLAC++/stream_decoder.cpp',
        'src/libFLAC++/stream_encoder.cpp',
        'src/libFLAC/bitmath.c',
        'src/libFLAC/bitreader.c',
        'src/libFLAC/bitwriter.c',
        'src/libFLAC/cpu.c',
        'src/libFLAC/crc.c',
        'src/libFLAC/fixed.c',
        'src/libFLAC/float.c',
        'src/libFLAC/format.c',
        'src/libFLAC/lpc.c',
        'src/libFLAC/md5.c',
        'src/libFLAC/memory.c',
        'src/libFLAC/metadata_iterators.c',
        'src/libFLAC/metadata_object.c',
        'src/libFLAC/stream_decoder.c',
        'src/libFLAC/stream_encoder.c',
        'src/libFLAC/stream_encoder_framing.c',
        'src/libFLAC/window.c',
    ]

    lib = env.static_lib(gen, out='flac', ins=files)
    env.install(gen, env['LIBDIR'], lib)

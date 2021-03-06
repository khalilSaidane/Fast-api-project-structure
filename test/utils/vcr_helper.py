import vcr as vcrpy

vcr = vcrpy.VCR(
    path_transformer=vcrpy.VCR.ensure_suffix(".yaml"),
    cassette_library_dir="test/vcr_cassettes",
    record_mode='once',
    match_on=['uri', 'method'],
)

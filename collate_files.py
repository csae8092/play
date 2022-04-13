from acdh_collatex_utils.acdh_collatex_utils import CxCollate

out = CxCollate(
    glob_pattern="./werke/uber-den-traum/uber-den-traum__*.xml",
    glob_recursive=False,
    output_dir="./werke/uber-den-traum/collated",
    char_limit=False,
    chunk_size=10000,
).collate()

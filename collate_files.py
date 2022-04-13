import glob
import lxml.etree as ET

from acdh_collatex_utils.acdh_collatex_utils import CxCollate
from acdh_collatex_utils.post_process import merge_tei_fragments

input_glob = "./werke/uber-den-traum/uber-den-traum__*.xml"
output_dir = "./werke/uber-den-traum/collated"
werk_path = "uber-den-traum"

out = CxCollate(
    glob_pattern=input_glob,
    glob_recursive=False,
    output_dir=output_dir,
    char_limit=False,
    chunk_size=5000,
).collate()

files = glob.glob(f"{output_dir}/*.xml")
full_doc = merge_tei_fragments(files)

with open(f'{werk_path}.xml', 'w') as f:
    f.write(ET.tostring(full_doc, encoding='UTF-8').decode('utf-8'))